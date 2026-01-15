from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_manufactured = False

    @abstractmethod
    def manufacture(self):
        pass

    def get_price(self):
        return self.price

    def get_info(self):
        return f"{self.name}, price: {self.price}, manufactured: {self.is_manufactured}"


class Electronics(Product):
    def __init__(self, name, price, warranty_months):
        super().__init__(name, price)
        self.warranty_months = warranty_months

    def manufacture(self):
        self.is_manufactured = True


class Furniture(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def manufacture(self):
        self.is_manufactured = True


class Factory:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def manufacture_all(self):
        for product in self.inventory:
            product.manufacture()

    def get_inventory(self):
        return self.inventory
