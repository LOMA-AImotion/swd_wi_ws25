def net_price(area, price_per_m2=1):
    return area * price_per_m2


def gross_price(area, price_per_m2=1, tax_rate=0.10):
    return net_price(area, price_per_m2) * (1 + tax_rate)


properties = [(10, 10), (15, 20), (8, 6)]  # (length, width)

price_per_m2 = 1      # €
tax_rate = 0.10       # 10%

for length, width in properties:
    area = length * width
    net = net_price(area, price_per_m2)
    gross = gross_price(area, price_per_m2, tax_rate)
    print(f"Area: {area} m² -> Net: {net:.2f}€ | Gross: {gross:.2f}€")
