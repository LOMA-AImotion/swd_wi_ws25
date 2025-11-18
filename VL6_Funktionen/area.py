def area(height, width, print_result=False):

    print("Calculating area...")
    area = height * width
    if print_result:
        print(f"Area: {area}")
    return area

result = area(20, 1500)
print(f"Area: {result}")

result2 = area(10, 150, True)
print(f"Area 2: {result2}")

overall_area = result2 + result
