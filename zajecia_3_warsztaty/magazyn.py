"""Prosty system księgowy/magazyn
Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

saldo
sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

saldo -     Program pobiera kwotę do dodania lub odjęcia z konta.
sprzedaż -  Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie.
            Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje
            odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
zakup -     Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było.
            Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
konto -     Program wyświetla stan konta.
lista -     Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn -   Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
przegląd -  Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod
            indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać
            przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym
            poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
koniec -    Aplikacja kończy działanie.

Dodatkowe wymagania:

Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.
"""
from zajecia_3_warsztaty.ksiegozbior import tytul

lista_produktow = [{
    "nazwa": "kawa",
    "cena_zl": 10.99,
    "producent": "Illy",
    "waga_jednej_sztuki_w_kg": 1,
    "ilosc_na_stanie": 50,
    "ilosc": 300,
    "rok_produkcji": 2024,
    "numer_inednyfikacyjny_produktu": 12-58-3-78256
    },
    {
    "nazwa": "herbata",
    "cena_zl": 5.99,
    "producent": "PG",
    "waga_jednej_sztuki_w_kg": 0.3,
    "ilosc_na_stanie": 200,
    "ilosc": 500,
    "rok_produkcji": 2023,
    "numer_inednyfikacyjny_produktu": 15-33-3-78333
    },
    {
    "nazwa": "maka",
    "cena_zl": 7.50,
    "producent": "Mlyny_Stoislaw",
    "waga_jednej_sztuki_w_kg": 1,
    "ilosc_na_stanie": 500,
    "ilosc": 2000,
    "rok_produkcji": 2024,
    "numer_inednyfikacyjny_produktu": 17-22-9-7844
    },
    {
    "nazwa": "Proszek_do_pieczenia",
    "cena_zl": 2.50,
    "producent": "Mlyny_Stoislaw",
    "waga_jednej_sztuki_w_kg": 0.02,
    "ilosc_na_stanie": 100,
    "ilosc": 200,
    "rok_produkcji": 2025,
    "numer_inednyfikacyjny_produktu": 1-725-9-78
}]

saldo = 7000
historia = ["Sprzedaz produktu: Proszek_do Pieczenia, 2.50, 5 sztuk", "Zakup produktu: Herbata, 5.99, 3 sztuki"]
print("Program ksiegowy - WITAMY!")
while True:
    print("Wybierz jedna z ponizszych pozycji podajac cyfre danej pozycji")
    komenda = input("""
        1. Saldo
        2. Sprzedaż
        3. Zakup
        4. Konto
        5. Lista
        6. Magazyn
        7. Przeglad
        8. Koniec (wpisz "koniec")
Podaj cyfre: """)
    match komenda:
        case "1":
            print(saldo)
        case "3": #zakup
            nazwa = input("Podaj nazwe produktu: ")
            koszt = float(input("Podaj cene produktu: "))
            producent = input("Podaj producenta produktu: ")
            waga_jednej_sztuki_w_kg = float(input("Podaj wage pojedynczego produktu w kg: "))
            ilosc = int(input("Podaj ilosc produktu w sztukach: "))
            rok_produkcji = int(input("Podaj rok produkcji: "))
            numer_identyfikacyjny_produktu = input("Podaj numer identyfikacyjny produktu: ")

            if saldo -(koszt * ilosc) < 0:
                print("Nie mozesz kupic danego produktu. Koszt tranzakcji przekracza istniejacy budżet.")
                historia.append(f"Proba zakupu : {nazwa}, {koszt}, {ilosc} sztuk - nie powiodla sie")
                continue
            else:
                saldo -= (koszt * ilosc)
            znaleziono_produkt = False
            for produkt in lista_produktow:
                if produkt.get("numer_identyfikacyjny_produktu") == numer_identyfikacyjny_produktu:
                    znaleziono_produkt = True
                    produkt["ilosc_na_stanie"] += ilosc
                    break
            if not znaleziono_produkt:
                lista_produktow.append({
                    "nazwa": nazwa,
                    "cena": koszt,
                    "producent": producent,
                    "waga_jednej_sztuki_w_kg": waga_jednej_sztuki_w_kg,
                    "ilosc_na_stanie": ilosc,
                    "ilosc": ilosc,
                    "rok_produkcji": rok_produkcji,
                    "numer_identyfikacyjny_produktu": numer_identyfikacyjny_produktu
                })
                print(lista_produktow)
                historia.append(f"Zakup produktu: {nazwa}, {koszt}, {ilosc} sztuk")
                for index, element in enumerate(lista_produktow):
                    print(f"Lista produktow w magazynie: Ksiazka {index} na liscie ksiazek to: {element}")
                for index, element in enumerate(historia):
                    print(f"Historia Tranzakcji - Produkt {index} w historii zakupow to: {element}")
        case "5":
            print("Calkowity stan magazynu")
            for index, element in enumerate(lista_produktow):
                print(f"Lista produktow w magazynie: Produkt {index} na liscie produktow to: {element}")
        case "7":
            od = input("Podaj wartosc 'od' (numer tranzakcji): ")
            do = input("Podaj wartosc 'do' (numer transakcji): ")
            if od:
                od = int(od)
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do = len(historia)
            print(historia[od:do])
    if komenda in ("8", "koniec", "Koniec", "KONIEC"):
        print("Zakonczono dzialanie programu")
        break