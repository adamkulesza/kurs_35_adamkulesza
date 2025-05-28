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

1. saldo -     Program pobiera kwotę do dodania lub odjęcia z konta.
2. sprzedaż -  Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie.
            Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje
            odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
3. zakup -     Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było.
            Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
4. konto -     Program wyświetla stan konta.
5. lista -     Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
6. magazyn -   Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
7. przegląd -  Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod
            indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać
            przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym
            poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
8. koniec -    Aplikacja kończy działanie.

Dodatkowe wymagania:

Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.
"""

# lista_produktow = [{"nazwa": "kawa", "cena_zl": 10.99, "ilosc_na_stanie": 10,"ilosc": 300,}, {"nazwa": "herbata", "cena_zl": 5.99, "ilosc_na_stanie": 200, "ilosc": 500,}, {"nazwa": "maka", "cena_zl": 7.50, "ilosc_na_stanie": 500, "ilosc": 2000,}, {"nazwa": "Proszek_do_pieczenia", "cena_zl": 2.50, "ilosc_na_stanie": 100, "ilosc": 200,}]

lista_produktow = [
    {
        "nazwa": "kawa",
        "cena": 10.99,
        "ilosc_na_stanie": 2,
        "ilosc": 300,
    },
    {
        "nazwa": "herbata",
        "cena": 5.99,
        "ilosc_na_stanie": 200,
        "ilosc": 500,
    },
    {
        "nazwa": "maka",
        "cena": 7.50,
        "ilosc_na_stanie": 500,
        "ilosc": 2000,
    },
    {
        "nazwa": "proszek_do_pieczenia",
        "cena": 2.50,
        "ilosc_na_stanie": 100,
        "ilosc": 200,
    },
]

saldo = 7000
historia = [
    "Sprzedaz produktu: Proszek_do Pieczenia, 2.50 zl, 5 sztuk",
    "Zakup produktu: Herbata, 5.99 zl, 3 sztuki",
]
print("Program ksiegowy - WITAMY!")
while True:
    print("Wybierz jedna z ponizszych pozycji podajac cyfre danej pozycji")
    komenda = input("""
        1. Saldo - wplaty/wyplaty
        2. Sprzedaż
        3. Zakup
        4. Konto - stan konta
        5. Lista -lista produktow
        6. Magazyn - stan magazynu dla konkretnego produktu
        7. Przeglad magazynu (od-do)
        8. Koniec (wpisz "koniec")
Podaj cyfre: """)
    match komenda:
        case "1":  # Zmiana salda - wplaty/wyplata
            kwota = float(input("Podaj kwotę jaka chcesz wpłacic/wyplacic z konta: "))
            if saldo + kwota <= 0:
                print(
                    "Nie można wykonac tej tranzakcji - wartosc konta nigdy nie moze byc ujemna - Nie możesz zadlużyc sklepu."
                )
            else:
                saldo += kwota
            print(f"Obecna suma na koncie wynosi {saldo}zl.")

        case "2":  # sprzedaz
            nazwa = input("Podaj nazwe produktu do kupienie: ")
            cena = float(input("Podaj cene sprzedazy: "))
            ilosc = int(input("Podaj ilosc w sztukach: "))
            produkt_znaleziony = False
            for produkt in lista_produktow:
                if produkt.get("nazwa") == nazwa:
                    if produkt["ilosc_na_stanie"] - ilosc < 0:
                        print(
                            "Nie mozna wykonac tej transakcji - za malo produktu w magazynie"
                        )
                        break
                    produkt["ilosc_na_stanie"] -= ilosc
                    saldo -= cena * ilosc  # koszt sprzedazy produktu
                    historia.append(
                        f"Sprzedaz produktu: {nazwa}, wartosc ksiazki {cena} zl, sztuk {ilosc}"
                    )
                    print(f"Sprzedaz produktu: {nazwa}, {cena} zl, sztuk {ilosc}")
                    produkt_znaleziony = True
                    break
            if not produkt_znaleziony:
                print("Brak odpowiedniej ilosci produktow, lub produkt nie istnieje.")
                historia.append(
                    f"Nieudana proba Sprzedazy produktu: {nazwa}, wartosc ksiazki {cena} zl, sztuk {ilosc} - brak towaru w magazynie"
                )
                print(
                    f"Sprzedaz produktu: {nazwa}, {cena} zl, sztuk {ilosc} - NIE POWIODLA SIE!!!!!!!"
                )

            print(f"Saldo wynosi: {saldo}")
            print("Lista produktow w magazynie")
            for index, element in enumerate(lista_produktow):
                print(
                    f"Lista produktow w magazynie: Ksiazka {index} na liscie ksiazek to: {element}"
                )
            print("Historia Tranzakcji")
            for index, element in enumerate(historia):
                print(
                    f"Historia Tranzakcji - Produkt {index} w historii zakupow to: {element}"
                )

        # TESTOWALEM INNY SPOSOB - ALE ODCZYTYWAL TYLKO PIERWSZY PRODUKT Z LISTY
        # case "2"
        # nazwa = input("Podaj nazwe produktu: ")
        # cena = float(input("Podaj cene produktu do sprzedaży: "))
        # ilosc = int(input("Podaj ilosc kupowanego produktu: "))
        # for produkt in lista_produktow:
        #     if produkt.get("ilosc_na_stanie") <= 0:
        #         print(f"Nie mozesz dokonac tranzakcji, Ilosc na stanie danego produktu wynosi {produkt['ilosc_na_stanie']}")
        #         historia.append(f"Proba zakupu: {nazwa}, {cena}, {ilosc} sztuk. Nie powiodla sie.")
        #         print(historia)
        #         continue
        # znaleziono_produkt = False
        # for produkt in lista_produktow:
        #     if produkt.get("nazwa") == nazwa:
        #         znaleziono_produkt = True
        #         produkt["ilosc_na_stanie"] -= ilosc
        #         saldo += (cena * ilosc)
        #         historia.append(f"Sprzedaz produktu: {nazwa}, cena {cena} zl za sztuke, {ilosc} sztuk")
        #         break
        #     else:
        #         znaleziono_produkt = True
        #         print("Brak produktu w magazynie. Nie mozna dokonac tranzakcji - !!!!!NIEPOWODZENIE!!!!!")
        #         historia.append(f"Proba sprzedazy produktu: {nazwa}, cena {cena} zl za sztuke, {ilosc} sztuka - !!!NIEPOWODZENIE!!!")
        #         break
        #
        #
        # print(f"Saldo wynosi: {saldo}")
        # print("Lista produktow w magazynie")
        # for index, element in enumerate(lista_produktow):
        #     print(f"Lista produktow w magazynie: Ksiazka {index} na liscie ksiazek to: {element}")
        # print("Historia Tranzakcji")
        # for index, element in enumerate(historia):
        #     print(f"Historia Tranzakcji - Produkt {index} w historii zakupow to: {element}")

        case "3":  # zakup
            nazwa = input("Podaj nazwe produktu: ")
            cena = float(input("Podaj cene produktu: "))
            ilosc = int(input("Podaj ilosc produktu w sztukach: "))

            if saldo - (cena * ilosc) < 0:
                print(
                    "Nie mozesz kupic danego produktu. Koszt tranzakcji przekracza istniejacy budżet."
                )
                historia.append(
                    f"Proba zakupu : {nazwa}, {cena}, {ilosc} sztuk - nie powiodla sie"
                )
                continue
            else:
                saldo -= cena * ilosc
            znaleziono_produkt = False
            for produkt in lista_produktow:
                if produkt.get("nazwa") == nazwa:
                    znaleziono_produkt = True
                    produkt["ilosc_na_stanie"] += ilosc
                    historia.append(
                        f"Zakup produktu: {nazwa}, cena {cena} zl za sztuke, {ilosc} sztuk."
                    )
                    print(
                        f"Dokonano zakupu {nazwa}, cena {cena} zl za sztuke, {ilosc} sztuk."
                    )
                    break
            if not znaleziono_produkt:
                lista_produktow.append(
                    {
                        "nazwa": nazwa,
                        "cena": cena,
                        "ilosc_na_stanie": ilosc,
                        "ilosc": ilosc,
                    }
                )
                historia.append(
                    f"Zakup produktu: {nazwa}, cena {cena} zl za sztuke, {ilosc} sztuk."
                )
                print(
                    f"Dokonano zakupu {nazwa}, cena {cena} zl za sztuke, {ilosc} sztuk."
                )
            print(f"Saldo wynosi: {saldo}")
            print("Lista produktow w magazynie")
            for index, element in enumerate(lista_produktow):
                print(
                    f"Lista produktow w magazynie: Ksiazka {index} na liscie ksiazek to: {element}"
                )
            print("Historia Tranzakcji")
            for index, element in enumerate(historia):
                print(
                    f"Historia Tranzakcji - Produkt {index} w historii zakupow to: {element}"
                )

        case "4":  # saldo
            print(saldo)

        case "5":  # Stan magazynu - lista_produktow
            print("Calkowity stan magazynu")
            for index, element in enumerate(lista_produktow):
                print(
                    f"Lista produktow w magazynie: Produkt {index} na liscie produktow to: {element}"
                )

        case "6":  # stan magazynu dla konkretnego produktu - trzeba podac nazwe
            nazwa = input("Podaj nazwe produktu: ")
            produkt_znaleziony = False
            for produkt in lista_produktow:
                if produkt.get("nazwa") == nazwa:
                    produkt_znaleziony = True
                    if produkt["ilosc_na_stanie"] <= 0:
                        print("Nie ma tego produktu na w magazynie - stan zero sztuk")
                        break
                    print(
                        f"Produkt: {produkt['nazwa']}, {produkt['producent']}, {produkt['ilosc_na_stanie']} sztuk w tej chwili znajduje sie na magazynie."
                    )
                    break
            if not produkt_znaleziony:
                print(
                    "Ten produkt nigdy nie zostal dodany do listy magazynu - nie istnieje w magazynie"
                )

        case "7":  # przeglad magazynu -od -do
            od = input("Podaj wartosc 'od' (numer tranzakcji) zaczynajac od zera: ")
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

    if komenda in ("8", "koniec", "Koniec", "KONIEC"):  # ZAKONCZENIE
        print("Zakonczono dzialanie programu")
        break
