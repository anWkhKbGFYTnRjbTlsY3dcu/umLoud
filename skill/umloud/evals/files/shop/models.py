"""Tiny shop domain used as a fixture for the umloud evals."""


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def place_order(self, lines):
        return Order(self, lines)


class PremiumCustomer(Customer):
    def __init__(self, name: str, email: str, discount: float):
        super().__init__(name, email)
        self.discount = discount


class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self, customer: Customer, lines: list):
        self.customer = customer
        self.lines = lines

    def total(self) -> float:
        return sum(l.product.price * l.quantity for l in self.lines)
