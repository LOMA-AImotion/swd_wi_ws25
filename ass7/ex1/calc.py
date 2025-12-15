
TAX_RATE = 0.19   # hardcoded tax rate

def calc_area(length, width):
    return length * width

def calc_price(area, price_per_m2):
    return area * price_per_m2

def calc_tax(price):
    return price * TAX_RATE
