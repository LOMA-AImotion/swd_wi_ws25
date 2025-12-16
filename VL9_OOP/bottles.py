class Bottle:
    def __init__(self, content, type, amount):
        self.content = content
        self.type = type
        self.amount = amount

    def get_sugar(self):
        sugar_per_100ml = 0    
        if self.content == "coke":
            sugar_per_100ml = 10 
        elif self.content == "wine":
            sugar_per_100ml = 6
        return sugar_per_100ml * (self.amount / 100)

b1 = Bottle("empty", "PET", 0)
b2 = Bottle("water", "PET", 500)
b3 = Bottle("coke", "PET", 500)

bottles = [b1, b2, b3]

for b in bottles:
    print(f"Content: {b.content}; Sugar: {b.get_sugar()}")
