"""
Exercise: Refactoring Procedural Code Using Inheritance

The following Python program processes different kinds of products in a factory.
Products are represented as dictionaries, and their behavior is implemented using a
large if / elif statement based on a "type" field.

This implementation contains a lot of duplicated code and mixes different
responsibilities in a single function.

Your task is to refactor the program using object-oriented programming, in
particular classes and inheritance, in order to improve readability,
extensibility, and maintainability.
"""



def manufacture_all(items):
    """
    items: list of dicts. Each dict has a 'type' key and other fields.
    Marks items as manufactured and returns a list of human-readable info strings.
    """
    infos = []

    for item in items:
        if item["type"] == "electronics":
            # manufacture
            if item.get("is_manufactured") is None:
                item["is_manufactured"] = False

            # electronics-specific rule
            if item.get("warranty_months") is None:
                item["warranty_months"] = 12

            item["is_manufactured"] = True

            # pricing / info
            price = float(item["price"])
            if price < 0:
                price = 0.0

            info = (
                f"Electronics: {item['name']} | price={price:.2f} | "
                f"warranty={item['warranty_months']}m | manufactured={item['is_manufactured']}"
            )
            infos.append(info)

        elif item["type"] == "furniture":
            # manufacture
            if item.get("is_manufactured") is None:
                item["is_manufactured"] = False

            # furniture-specific rule
            if item.get("material") is None:
                item["material"] = "unknown"

            item["is_manufactured"] = True

            # pricing / info
            price = float(item["price"])
            if price < 0:
                price = 0.0

            info = (
                f"Furniture: {item['name']} | price={price:.2f} | "
                f"material={item['material']} | manufactured={item['is_manufactured']}"
            )
            infos.append(info)

        elif item["type"] == "robot":
            # manufacture
            if item.get("is_manufactured") is None:
                item["is_manufactured"] = False

            # robot-specific rule
            if item.get("payload_kg") is None:
                item["payload_kg"] = 5

            item["is_manufactured"] = True

            # pricing / info
            price = float(item["price"])
            if price < 0:
                price = 0.0

            info = (
                f"Robot: {item['name']} | price={price:.2f} | "
                f"payload={item['payload_kg']}kg | manufactured={item['is_manufactured']}"
            )
            infos.append(info)

        else:
            raise ValueError(f"Unknown type: {item['type']}")

    return infos


if __name__ == "__main__":
    items = [
        {"type": "electronics", "name": "TV", "price": 499.99, "warranty_months": 24},
        {"type": "furniture", "name": "Chair", "price": 79.5, "material": "wood"},
        {"type": "robot", "name": "PickerBot", "price": 1200, "payload_kg": 12},
        {"type": "electronics", "name": "Radio", "price": -10},  # bad price on purpose
    ]

    for line in manufacture_all(items):
        print(line)
