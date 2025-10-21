k = int(input("Bis zu welchem k soll ich die geraden Zahlen ausgeben? "))

for i in range(1, k+1):
    print(f"i: {i}, Typ: {type(i)}")
    if i % 2 == 0:
        print(f"{i} ist eine gerade Zahl")
    else:
        print(f"{i} ist keine gerade Zahl")