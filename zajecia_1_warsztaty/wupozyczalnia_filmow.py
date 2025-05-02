"""
Wypozyczalnia filmow
wczytaj od uzytkownika:
- wiek (liczba calkowita)
- czy ma zgode od rodzicow (tak/nie)

Oblicz:
- ma dostep_18plus (wiek >= 18)
- ma_dostep_13plus (wiek >= 13 lub zgoda == "tak")

Wyswietl:
- "Film 18=", "Film 13+" albo "Tylko bajki" zaleznie od wieku i zgody , bez ifow.
"""
############## moja wersja ##########
# wiek = int(input("Podaj swoj wiek:"))
# zgoda_rodzicow = input("czy masz zgode rodzicow (Tak/Nie) :")
# czy_moge_wypozyczyc_filmy_18 = wiek >= 18 or zgoda_rodzicow.lower() == "tak"
# czy_moge_wypozyczyc_filmy_13 = wiek >= 13 or zgoda_rodzicow.lower() == "tak"
# print(czy_moge_wypozyczyc_filmy_18)
# print(czy_moge_wypozyczyc_filmy_13)



###################### program instruktora ############################
wiek = int(input("podaj swoj wiek: "))
zgoda = input ("czy masz zgode rodzica? (Tak/Nie): ")
zgoda = zgoda.lower()

zgoda_potwierdzona = zgoda == "tak"
ma_dostep_18plus = wiek >= 18
ma_dostep_13plus = wiek >= 13  or zgoda_potwierdzona

# print(f"Uzytkownik ma {wiek} lat.")
# print(f"urzytkownik na zgode rodzicow: {zgoda_potwierdzona}")
# print(f"Urzytkownik ma dostep do filmow 18+: {ma_dostep_18plus}")
# print(f"Urzytkownik ma dostep do filmow 13+: {ma_dostep_13plus}")
print("Film 18+" * ma_dostep_18plus + "Filmy 13+" * ma_dostep_13plus + "tylko bajki" * (not ma_dostep_13plus and not ma_dostep_18plus))