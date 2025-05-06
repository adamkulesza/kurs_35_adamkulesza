# imie = ("Adam")
# print(imie)

############################### if
# print("symulacja sklepu zabka: ")
# print("witaj w sklepie Żabka!")
#
# nazwa_produktu = input("Podaj nazwe produktu: ")
# cena_produktu = float(input("Podaj cene produktu: "))
# wiek_klienta = int(input("Podaj swoj wiek: "))
#
#
# print(f"chcesz kupić produkt: {nazwa_produktu} za cene: {cena_produktu} zl")
#
# if wiek_klienta >= 18:
#     print("Warunek wieku został spełniony.")
#     # print("dalej jestesmy w bbloku kodu")
#
# if wiek_klienta < 18:
#     print("Nie mozesz kupic tego produktu! Produkt dla pelnoletnich")



################# else
# print("symulacja sklepu zabka: ")
# print("witaj w sklepie Żabka!")
#
# nazwa_produktu = input("Podaj nazwe produktu: ")
# cena_produktu = float(input("Podaj cene produktu: "))
# wiek_klienta = int(input("Podaj swoj wiek: "))
#
#
# print(f"chcesz kupić produkt: {nazwa_produktu} za cene: {cena_produktu} zl")
#
# if wiek_klienta >= 18:
#     print("Warunek wieku został spełniony.")
# else:
#     print("Nie mozesz kupic tego produktu")


##########
# print("symulacja sklepu zabka: ")
# print("witaj w sklepie Żabka!")
#
# nazwa_produktu = input("Podaj nazwe produktu: ")
# cena_produktu = float(input("Podaj cene produktu: "))
#
# if nazwa_produktu.lower() == "piwo" or nazwa_produktu.lower() == "papierosy" or nazwa_produktu.lower() == "energetyk" or nazwa_produktu.lower() == "alkohol wysokoprocentowy":
#     print("Ten produkt jest przeznaczony dla osob pelnoletnich!")
#     wiek_klienta = int(input("Podaj swoj wiek: "))
#     if wiek_klienta >= 18:
#         print("Masz 18 lat - mozesz kupic ten produkt.")
#         print(f"Kupiłes produkt: {nazwa_produktu} za cene: {cena_produktu} zl")
#     else:
#         print("Nie mozesz kupić tego produktu - produkt dla pelnoletnich")
# else:
#     print("Ten produkt nie wymaga podania wieku")
#     print(f"Kupiłes produkt: {nazwa_produktu} za cene: {cena_produktu} zl")


############ elif
# zawod = input("Podaj swoj zawod: ")
# wiek = int(input("Podaj swoj wiek: "))
#
# if zawod.lower() == "policjant":
#     print(f"Do emerytury zostalo Ci {45 - wiek} lat pracy")
# elif zawod == "zolnierz":
#     print(f"Do emerytury zostalo Ci {50 - wiek} lat pracy")
# elif zawod == "nauczyciel":
#     print(f"Do emerytury zostalo Ci {60 - wiek} lat pracy")
# elif zawod == "praca biurowa":
#     print(f"Do emerytury zostalo Ci {65 - wiek} lat pracy")
# elif zawod == "programista":
#     print("Zapomnij o emeryturze")
# else:
#     print(f"Do twojej emerytury zostalo {65 - wiek} lat.")

############################ mach_case (nie dziala na zakresach (case < 20 - raki zapis nie zadziala a zadziala - case 20)
zawod = input("Podaj mi swoj zawod: ")
wiek + int(input("Podaj mi swoj wiek: "))

############
"""
warunek logiczny - wyrazene, które zwroci wartosc typu booleean (True/False)
if {warunek logiczny}
    {blok kodu}
"""