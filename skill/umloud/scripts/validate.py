#!/usr/bin/env python3
"""Render-check PlantUML and Mermaid diagrams.

Usage:
    python validate.py PATH [PATH ...] [--out DIR] [--format svg|png]
                       [--plantuml-jar JAR] [--chrome PATH] [--confluence]

Without --out, images go to a fresh system temp directory (not your project folder).

PATH can be a .puml / .plantuml / .mmd / .mermaid file, a Markdown file
(every ```plantuml and ```mermaid fenced block is checked), or a directory
(searched recursively for all of the above).

Renderers:
  PlantUML: `plantuml` on PATH, or pass --plantuml-jar /path/to/plantuml.jar (needs java;
            Graphviz `dot` is needed for class/component/use-case/deployment layouts).
  Mermaid:  `mmdc` on PATH (npm i -g @mermaid-js/mermaid-cli). If it can't find a browser,
            pass --chrome /path/to/chrome-or-chromium.

With --confluence, Mermaid sources are also checked for constructs older Confluence Mermaid apps reject (WARN lines).

Exit code 0 = everything rendered; 1 = at least one diagram failed; 2 = no renderer found.
Rendered images are written to --out, or to a new temp directory if --out is omitted; the path is printed on the last line.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Named limits (no magic numbers).
RENDER_TIMEOUT_SECONDS = 180
MAX_NAME_LENGTH = 120
ALLOWED_FORMATS = ("svg", "png")

PUML_EXT = {".puml", ".plantuml", ".pu", ".iuml"}
MMD_EXT = {".mmd", ".mermaid"}
FENCE = re.compile(r"^```(plantuml|puml|mermaid)\s*\n(.*?)^```", re.M | re.S)


def plantuml_cmd(jar=None):
    if jar and Path(jar).is_file() and shutil.which("java"):
        return ["java", "-Djava.awt.headless=true", "-jar", jar]
    if shutil.which("plantuml"):
        return ["plantuml"]
    return None


def mermaid_cmd():
    exe = shutil.which("mmdc")
    return [exe] if exe else None


def collect(paths):
    """Yield (label, kind, source_text)."""
    for p in paths:
        p = Path(p)
        files = [p] if p.is_file() else sorted(x for x in p.rglob("*") if x.is_file())
        for f in files:
            ext = f.suffix.lower()
            if ext in PUML_EXT:
                yield str(f), "plantuml", f.read_text(encoding="utf-8")
            elif ext in MMD_EXT:
                yield str(f), "mermaid", f.read_text(encoding="utf-8")
            elif ext == ".md":
                text = f.read_text(encoding="utf-8")
                for i, m in enumerate(FENCE.finditer(text), 1):
                    kind = "mermaid" if m.group(1) == "mermaid" else "plantuml"
                    line = text[: m.start()].count("\n") + 1
                    yield f"{f}:{line} (block {i})", kind, m.group(2)


def safe_name(label):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", label).strip("_")[-MAX_NAME_LENGTH:]


CONFLUENCE_UNSAFE = [
    (re.compile(r"^\s*note\s+for\b", re.M), "class 'note for' (newer Mermaid)"),
    (re.compile(r"^\s*class\s+\w+\[", re.M), "class id[\"label\"] (newer Mermaid)"),
    (re.compile(r"^\s*namespace\b", re.M), "namespace (newer Mermaid)"),
    (re.compile(r"^\s*(create|destroy)\s", re.M), "create/destroy participant (Mermaid >= 10.3)"),
    (re.compile(r"^\s*(title|accTitle|accDescr)\b", re.M), "title/accTitle (use a %% comment)"),
    (re.compile(r"^---\s*$", re.M), "front-matter block"),
    (re.compile(r"%%\{init", re.M), "%%{init}%% directive"),
    (re.compile(r"^\s*direction\s+\w+", re.M), "direction inside class/state diagram"),
    (re.compile(r"^```", re.M), "Markdown fence inside the Mermaid source"),
    (re.compile(r"-beta\b"), "beta diagram type"),
]


def confluence_warnings(src):
    first = src.strip().splitlines()[0] if src.strip() else ""
    out = []
    for rx, msg in CONFLUENCE_UNSAFE:
        if "direction" in msg and first.startswith(("flowchart", "graph")):
            continue
        if rx.search(src):
            out.append(msg)
    return out


def clean(err):
    return "\n".join(l for l in err.splitlines() if not l.startswith("Picked up JAVA_TOOL_OPTIONS"))


def render_plantuml(cmd, src, out_dir, name, fmt):
    if fmt not in ALLOWED_FORMATS:
        return False, f"unsupported format: {fmt}"
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / f"{name}.puml"
        f.write_text(src, encoding="utf-8")
        # Argument list, no shell; fmt is allow-listed above, paths are our own temp files.
        r = subprocess.run(cmd + [f"-t{fmt}", "-failfast2", "-o", str(out_dir.resolve()), str(f)],
                           capture_output=True, text=True, timeout=RENDER_TIMEOUT_SECONDS, shell=False)
        err = clean(r.stdout + r.stderr).strip()
        produced = (out_dir / f"{name}.{fmt}").exists()
        ok = r.returncode == 0 and produced
        if produced and fmt == "svg":
            svg = (out_dir / f"{name}.svg").read_text(encoding="utf-8", errors="ignore")
            if "Syntax Error" in svg or "syntax error" in svg.lower():
                ok, err = False, err or "PlantUML rendered a syntax-error image"
        return ok, err


def render_mermaid(cmd, src, out_dir, name, fmt, chrome=None):
    if fmt not in ALLOWED_FORMATS:
        return False, f"unsupported format: {fmt}"
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / f"{name}.mmd"
        f.write_text(src, encoding="utf-8")
        out = out_dir / f"{name}.{fmt}"
        args = cmd + ["-q", "-i", str(f), "-o", str(out)]
        cfg = Path(tmp) / "puppeteer.json"
        conf = {"args": ["--no-sandbox", "--disable-setuid-sandbox"]}
        if chrome and Path(chrome).is_file():
            conf["executablePath"] = chrome
        cfg.write_text(json.dumps(conf))
        args += ["-p", str(cfg)]
        # Argument list, no shell; fmt is allow-listed above, paths are our own temp files.
        r = subprocess.run(args, capture_output=True, text=True, timeout=RENDER_TIMEOUT_SECONDS, shell=False)
        err = (r.stdout + r.stderr).strip()
        return r.returncode == 0 and out.exists(), err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--out", default=None,
                    help="output dir (default: a new system temp dir, so nothing is written to the project)")
    ap.add_argument("--format", default="svg", choices=list(ALLOWED_FORMATS))
    ap.add_argument("--plantuml-jar", default=None, help="path to plantuml.jar (needs java)")
    ap.add_argument("--chrome", default=None, help="path to a Chrome/Chromium binary for Mermaid")
    ap.add_argument("--confluence", action="store_true",
                    help="warn about Mermaid constructs older Confluence Mermaid apps reject")
    a = ap.parse_args()

    if a.out:
        out_dir = Path(a.out)
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = Path(tempfile.mkdtemp(prefix="umloud-"))
    pu, mm = plantuml_cmd(a.plantuml_jar), mermaid_cmd()
    items = list(collect(a.paths))
    if not items:
        print("No diagrams found.")
        return 0

    failed = skipped = 0
    for label, kind, src in items:
        name = safe_name(label)
        cmd = pu if kind == "plantuml" else mm
        if cmd is None:
            skipped += 1
            print(f"SKIP  [{kind}] {label}  (renderer not installed)")
            continue
        fn = render_plantuml if kind == "plantuml" else render_mermaid
        extra = {"chrome": a.chrome} if kind == "mermaid" else {}
        ok, err = fn(cmd, src, out_dir, name, a.format, **extra)
        if ok:
            print(f"OK    [{kind}] {label}")
            if kind == "mermaid" and a.confluence:
                for w in confluence_warnings(src):
                    print(f"WARN  [mermaid] {label}: Confluence-unsafe: {w}")
        else:
            failed += 1
            print(f"FAIL  [{kind}] {label}\n      " + (err or "unknown error").replace("\n", "\n      "))

    total = len(items)
    print(f"\n{total - failed - skipped}/{total} rendered, {failed} failed, {skipped} skipped. Output: {out_dir}")
    if skipped == total:
        return 2
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
