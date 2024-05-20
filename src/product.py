import uuid

class Product:
    def __init__(self, name, price, quantity):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.quantity = quantity
