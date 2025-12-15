from ui import get_float, show_results
from calc import calc_area, calc_price, calc_tax

def main():
    length = get_float("Enter length: ")
    width = get_float("Enter width: ")
    price_per_m2 = get_float("Enter price per m²: ")

    area = calc_area(length, width)
    price = calc_price(area, price_per_m2)
    tax = calc_tax(price)
    total = price + tax

    show_results(area, price, tax, total)

main()
