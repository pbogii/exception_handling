
try:
    szam = int(input("kérlek adj meg egy számot!"))
    print(f"a szám négyzete:{szam ** 2}")

except ValueError:
    print("Not the right format")
