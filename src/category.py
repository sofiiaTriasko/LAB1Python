import uuid

class Category:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
