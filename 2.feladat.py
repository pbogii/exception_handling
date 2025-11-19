#Írj egy programot, ami a felhasználótól
#  három egész számot számot kér be egyesével,
#  ezeket eltárolja egy listában,
#  majd a képernyőre kiírja a lista tartalmát!
#  Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet,
#  és ismétlődjön meg a bekérés!

haromszam = []
for i in range(3):
    while True:
        try:
            szam = int(input("Kérlek adj meg egy számot! "))
            haromszam.append(szam)
            break

        except ValueError as e:
            print(e)
            print("ValueError: Nem számot adtál meg")

print(f"A litában ezek a számok vannak {haromszam}")