try:
    szam =10
    oszto = float(input(f"Mennyivel osszam el a {szam}-es számot?"))

    print(f"A két szám osztásának eredménye : {szam/oszto} ")

except ZeroDivisionError:
    print("0-val nem osztunk")