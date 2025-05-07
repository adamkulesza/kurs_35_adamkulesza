# wiek = int(input("Podaj swoj wiek: "))
#
#
# while wiek < 65:
#     print(f"Nie powinienes jeszcze byc na emeryturze! Masz {wiek} lat.")
#     wiek += 1
# print(f"Masz {wiek} lat. Powinienes byc na emeryturze.")

############### nieskonczona petla

# wiek = int(input("Podaj swoj wiek: "))
#
# while wiek >= 65:
#     print("Powinienes byc na emeryturze!")

################ petla spelni sie pod konkretnym warunkiem gdy podamy imie "Michal"

# imie = input("Podaj swoje imie: ")
#
# while imie != "Michal":
#     print("Nie jestes michalem!")
#     imie = input("Podaj swoje imie: ")
# print("Witaj Michał")

#################### while True - break

imie = input("Podaj swoje imie: ")

while True:
    if imie == "Michal":
        print("Czesc Michal!")
        break # komenda przerywajaca wykonanie petli i wyjscie zupelnie z calosci petli
        print("kod po breaku")
    else:
        imie = input("Podaj swoje imie: ")
print("tu trafiamy po breaku!!")

###################### continue

# wiek = int(input("Podaj swoj wiek: "))
#
# while wiek < 65:
#     wiek += 1
#     if wiek == 18 or wiek == 25:
#         print("Masz 18 lat!")
#         continue #operacja ktora wywoluje kolejna iteracje petli
#     print(f"nie powinienes byc na emeryturze! Masz {wiek} lat.")

######################## nie zawsze chcemy cos wykonywac - pass

# wiek = int(input("Podaj swoj wiek: "))
#
# if wiek >= 18:
#     print("Masz 18 lat lub wiecej!")
# else:
#     pass
# print("moja kolejna instrukcja")

################# petle while
"""
while {warunek logiczny}:
    {blok kodu} wykonuje sie dopoki warunek logiczny jest spelniony
"""
