szam =10
try:
    oszto = float(input(f"Mennyivel osszam el a {szam}-es számot?"))
    print(f"A két szám osztásának eredménye : {szam/oszto} ")

except ZeroDivisionError as e:
    print(e)
    print("ZeroDivisionError: 0-val nem osztunk")

except ValueError as e:
    print(e)
    print("ValueError: Not the right format")

oszto = float(input(f"Mennyivel osszam el a {szam}-es számot?"))
print(f"A két szám osztásának eredménye : {szam/oszto} ")
