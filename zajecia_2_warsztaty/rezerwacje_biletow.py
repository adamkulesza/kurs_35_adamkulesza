"""
Treść zadania

Napisz program do obsługi rezerwacji biletów grupowych na wydarzenie.

Działanie programu:

    Program pyta o liczbę osób w grupie.

    Dla każdej osoby pobiera liczbę biletów, które chce kupić (od 1 do 5).

    Jeśli użytkownik poda wartość spoza zakresu 1–5 lub wprowadzi nieprawidłową wartość, program kończy wprowadzanie danych.

    Na koniec program wyświetla podsumowanie:

        Łączną liczbę biletów,

        Kwotę do zapłaty (20 zł za bilet, zniżka do 15 zł za bilet obowiązuje, jeśli liczba transakcji bedzie wieksza od 5 i łączna liczba biletów wynosi co najmniej 10),

        Największą pojedynczą transakcję biletową,

       nie robimy tego podpunkty --------- Liczbę błędnych wpisów (czyli ile razy wprowadzono nieprawidłową wartość).

Przykłady

Przykład 1:

text
Liczba osób: 5
Bilety: 3, 2, 4, 1, 5

Podsumowanie:
Łączna liczba biletów: 15
Kwota do zapłaty: 225 zł (zniżka)
Największa transakcja: 5
Liczba błędnych wpisów: 0

Przykład 2:

text
Liczba osób: 6
Bilety: 2, 1, 0 (błąd)

Podsumowanie:
Łączna liczba biletów: 3
Kwota do zapłaty: 60 zł
Największa transakcja: 2
Liczba błędnych wpisów: 1

Przykład 3:

text
Liczba osób: 3
Bilety: 5, 6 (błąd)

Podsumowanie:
Łączna liczba biletów: 5
Kwota do zapłaty: 100 zł
Największa transakcja: 5
Liczba błędnych wpisów: 1
"""

liczba_osob = int(input("Podaj liczbe osob w grupie: "))
laczna_liczba_biletow = 0
najwieksza_liczba_biletow_w_tranzakcji = 0
tranzakcja_z_najwieksza_iloscia_biletow = None
for tranzakcja in range(liczba_osob):
    liczba_biletow_w_tranzakcji = int(
        input(f"Podaj liczbe biletow dla osoby {tranzakcja + 1}: ")
    )
    if liczba_biletow_w_tranzakcji < 1 or liczba_biletow_w_tranzakcji > 5:
        print("Nieprawidlowa wartosc. Wprowadzanie danych zakonczone.")
        break
    laczna_liczba_biletow += liczba_biletow_w_tranzakcji
    if liczba_biletow_w_tranzakcji > najwieksza_liczba_biletow_w_tranzakcji:
        najwieksza_liczba_biletow_w_tranzakcji = liczba_biletow_w_tranzakcji
        tranzakcja_z_najwieksza_iloscia_biletow = tranzakcja + 1
if liczba_osob >= 5 and laczna_liczba_biletow >= 10:
    cena_biletu = 15
    print("Cena pojedynczego biletu wynosi 15 zl - Masz zniszke 25%")
else:
    cena_biletu = 20
    print("Cena pojedynczego biletu wynosi 20 zl")

print(f"Liczba biletow: {laczna_liczba_biletow}")
print(f"Laczna cena biletow to: {laczna_liczba_biletow * cena_biletu} zl.")
print(f"Najwieksza tranzakcja to: {najwieksza_liczba_biletow_w_tranzakcji}")
print(
    f"Transakcja z najwieksza iloscia biletow: {tranzakcja_z_najwieksza_iloscia_biletow}"
)
