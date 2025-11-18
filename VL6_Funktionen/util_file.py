reduced_tax_items = [ "Book", "Bread", "Potatoes", "Personal Hygiene"]

def get_tax(name, price, amount):
    price_item = round(amount*price, 2)

    tax_rate = 0.19
    if name in reduced_tax_items:
       tax_rate = 0.07
    tax_item = round(tax_rate * price_item, 2)
    return price_item, tax_item

def greet_studis(student_group):
    print(f"Hello {student_group}, have fun today!")