ilosc_elementow = int(input("Podaj ilosc elementow: "))

ilosc_paczek = 1
paczka_z_najwieksza_pusta_waga = 20
numer_paczki_z_najwieksza_pusta_waga = None
waga_paczki = 0

waga_wszystkich_elementow = 0
for element in range(ilosc_elementow):
    waga_elementu = float(input(f"Podaj wage elementu {element + 1}: "))
    if waga_elementu < 1 or waga_elementu > 10:
        print(
            "Produkt poza dopuszczalnym zakresem wagi. Nie mozesz go dodac do paczki."
        )
    else:
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
print(f"Wyslano {ilosc_paczek} paczki")
print(
    f"Paczka z najwieksza pusta waga to paczna nr. {numer_paczki_z_najwieksza_pusta_waga}"
)
