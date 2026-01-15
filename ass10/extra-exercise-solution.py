
class Product:
    def __init__(self, name, price):
        self.name = name
        # normalize price like in the messy version (negative -> 0.0)
        self.price = float(price)
        if self.price < 0:
            self.price = 0.0
        self.is_manufactured = False

    def manufacture(self):
        """Default manufacture behavior."""
        self.is_manufactured = True

    def get_price(self):
        return self.price

    def get_info(self):
        return f"Product: {self.name} | price={self.price:.2f} | manufactured={self.is_manufactured}"


class Electronics(Product):
    def __init__(self, name, price, warranty_months=None):
        super().__init__(name, price)
        self.warranty_months = 12 if warranty_months is None else warranty_months

    def manufacture(self):
        # electronics could have special steps; keep simple
        self.is_manufactured = True

    def get_info(self):
        return (
            f"Electronics: {self.name} | price={self.price:.2f} | "
            f"warranty={self.warranty_months}m | manufactured={self.is_manufactured}"
        )


class Furniture(Product):
    def __init__(self, name, price, material=None):
        super().__init__(name, price)
        self.material = "unknown" if material is None else material

    def manufacture(self):
        self.is_manufactured = True

    def get_info(self):
        return (
            f"Furniture: {self.name} | price={self.price:.2f} | "
            f"material={self.material} | manufactured={self.is_manufactured}"
        )


class Robot(Product):
    def __init__(self, name, price, payload_kg=None):
        super().__init__(name, price)
        self.payload_kg = 5 if payload_kg is None else payload_kg

    def manufacture(self):
        self.is_manufactured = True

    def get_info(self):
        return (
            f"Robot: {self.name} | price={self.price:.2f} | "
            f"payload={self.payload_kg}kg | manufactured={self.is_manufactured}"
        )


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


def product_from_dict(d):
    """Small helper to convert the original dict format into objects."""
    t = d["type"]
    if t == "electronics":
        return Electronics(d["name"], d["price"], d.get("warranty_months"))
    if t == "furniture":
        return Furniture(d["name"], d["price"], d.get("material"))
    if t == "robot":
        return Robot(d["name"], d["price"], d.get("payload_kg"))
    raise ValueError(f"Unknown type: {t}")


if __name__ == "__main__":
    # Same style of input as the messy starter code
    items = [
        {"type": "electronics", "name": "TV", "price": 499.99, "warranty_months": 24},
        {"type": "furniture", "name": "Chair", "price": 79.5, "material": "wood"},
        {"type": "robot", "name": "PickerBot", "price": 1200, "payload_kg": 12},
        {"type": "electronics", "name": "Radio", "price": -10},  # negative price -> 0.0
    ]

    factory = Factory()
    for d in items:
        factory.add_product(product_from_dict(d))

    factory.manufacture_all()

    for p in factory.get_inventory():
        print(p.get_info())
