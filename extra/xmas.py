import random

ingredients = [
    [('sugar', 0.5), ('cocoa', 0.3), ('flour', 0.1), ('milk', 0.1)],
    [('flour', 0.3), ('hazelnuts', 0.2), ('milk', 0.2), ('cocoa', 0.15), ('cinamon', 0.15)]
] 

calendar = []

# Step 1: Ingredient waehlen
def get_random_ingredient():
    return random.choice(ingredients)

print(get_random_ingredient())
# Step 2: Calender zusammenstellen
def build_calendar():
    return [get_random_ingredient() for _ in range(24)]

calendar = build_calendar()
print(calendar)

# Step 3: Agg. Zutaten
def agg_calendar(c):
    total = {}
    for recipe in c:
        for ingredient, amount in recipe:
            total[ingredient] = total.get(ingredient, 0) + amount
    return list(total.items())

agg_calendar = agg_calendar(calendar)
print("----")
print(agg_calendar)

# Step 4: sortieren
def sort_calendar(agg_c):
    return sorted(agg_c, key=lambda x: x[1], reverse=True)

sorted_calendar = sort_calendar(agg_calendar)
print("###")
print(sorted_calendar)


# Step 5: % Werte? 
sum_cal = sum(sorted_calendar)

# Step 6: String 
def as_string(c):
    return ", ".join(name for name, _ in c)

print(as_string(sorted_calendar))