############# for - iterowanie po liscie imion
from collections.abc import Iterable

# lista_uczniow = ["Adam", "Jan", "Michal", "Kasia", "Tomek"]
# print(isinstance(lista_uczniow, Iterable))
# for uczen in lista_uczniow:
#     print(uczen)

######### for - iterowanie po zakresie liczb

# for number in range(20):
#     print(number)

ilosc_paczek = int(input("Podaj ilosc paczek: "))
waga_wszystkich_paczek = 0
for paczka in range(ilosc_paczek):
    print(paczka)
    waga_paczki = float(input("Podaj wage paczki: "))
    waga_wszystkich_paczek += waga_paczki

print(f"Waga wszystkich paczek wynosi: {waga_wszystkich_paczek} kg")

"""
for <tymczasowa_zmienna> in <iterowalny_obiekt>:
    <blok_kodu>
"""