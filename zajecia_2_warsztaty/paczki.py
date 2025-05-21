# ilosc_elementow = int(input("Podaj liczbe elementow do wyslania: "))
# if
# waga_elementu1
# if ilosc_elementow == 1:
#     element1_waga = int(input("Podaj wage pierwszego elementu: "))
#     print("Wysylasz 1 produkt.")
#     if element1_waga <= 20:
#         print("Wyslales 1 paczke")
#     else:
#         print("Nie mozesz wyslac tego elementu!! Paczka przekracza mase 20kg")

# waga_paczki = 20
# waga_elementow = int(input("Podaj wage elementu ")) <= 10 >= 1
# while waga_elementow > 10:
#     print("Element przekracza dopuszczalna maksymalna wage dla jednego elementu")


# ilosc_elementow = int(input("Podaj ilosc elementow: "))
# waga_wszystkich_elementow = 0
# for element in range(ilosc_elementow):
#     print(element)
#     waga_elementu = float(input(f"Podaj wage elementu {element + 1}: "))
#     waga_wszystkich_elementow += waga_elementu
#
# print(f"Waga wszystkich paczek wynosi: {waga_wszystkich_elementow} kg")

###################

# while paczka < 20:
#     if paczka == 20:
#         kolejny_element += element
#         print("Zapakowales 1 paczke")
#         continue #operacja ktora wywoluje kolejna iteracje petli
#     print(f"nie powinienes byc na emeryturze! Masz {paczka} lat.")

######################### moze dobra doroga???????

# ilosc_elementow = int(input("Podaj ilosc elementu: "))
# waga_wszystkich_elementow = 0
# for paczka in range(ilosc_elementow):
#     print(paczka)
#     waga_elementu = float(input("Podaj wage elemenu: "))
#     waga_wszystkich_elementow += waga_elementu
#
# print(f"Waga wszystkich elementow wynosi: {waga_wszystkich_elementow} kg")
# print(f"Masz {waga_wszystkich_elementow / 20} paczki")


############################### moze???????
# while True:
#     if paczka >= 20:
#         print("masz jedna paczke")
#         break # komenda przerywajaca wykonanie petli i wyjscie zupelnie z calosci petli
#         print("kod po breaku")
#     else:
#         element = float(input("Podaj wage kolejnego elementu: "))
# print("tu trafiamy po breaku!!")

ilosc_elementow = int(input("Podaj ilosc elementow: "))

ilosc_paczek = 1
paczka_z_najwieksza_pusta_waga = 20
numer_paczki_z_najwieksza_pusta_waga = None
waga_paczki = 0

waga_wszystkich_elementow = 0

for element in range(ilosc_elementow):
    waga_elementu = float(input(f"Podaj wage elementu {element + 1}: "))
    if waga_paczki + waga_elementu > 20:
        print("Przekroczona waga paczki. Skladamy kolejna paczke")
        if 20 - waga_paczki < paczka_z_najwieksza_pusta_waga:
            paczka_z_najwieksza_pusta_waga = waga_paczki
            numer_paczki_z_najwieksza_pusta_waga = ilosc_paczek
        waga_paczki = waga_elementu
        ilosc_paczek += 1
    else:
        waga_paczki += waga_elementu
    waga_wszystkich_elementow += waga_elementu


print(f"Waga wszystkich paczek wynosi: {waga_wszystkich_elementow} kg")
print(f"Wyslano {ilosc_paczek} packi")
print(
    f"Paczka z najwieksza pusta waga to paczna nr. {numer_paczki_z_najwieksza_pusta_waga}"
)
