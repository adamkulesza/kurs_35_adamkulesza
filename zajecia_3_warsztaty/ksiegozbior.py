"""
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania nr ISBN. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu numeru ISBN.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne.
"""

# bedziemy dzialali w petli - while True:
# lista ksiazek - lista wszystkich ksiazek gdzie kazda ksiazka jest slownikiem


lista_ksiazek = [{
        "tytul": "Harry Potter i Kamien Filozoficzny",
        "autor": "J.K. Rowling",
        "rok_wydania": 1999,
        "cena": 39.99,
        "ilosc_na_stanie": 5,
        "kategoria": "fantazy",
        "ilosc": 5,
        "ISBN": "978-3-163148410-0",
    },
    {
        "tytul": "Wladca Pierscieni: Druzyna Pierscienia",
        "autor": "J.R.R. Tolkien",
        "rok_wydania": 1954,
        "cena": 49.99,
        "ilosc_na_stanie": 3,
        "kategoria": "fantazy",
        "ilosc": 3,
        "ISBN": "978-0-261-10221-7",
    },
    {
        "tytul": "Zbrodnia i Kara",
        "autor": "Fiodor Dostojewski",
        "rok_wydania": 1866,
        "cena": 29.99,
        "ilosc_na_stanie": 0,
        "kategoria": "klasyka",
        "ilosc": 2,
        "ISBN": "978-3-14-044913-6",
    }
]
saldo = 10000
historia = ["Sprzedaz ksiazki: Harry Potter i Kamien Filozoficzny, 39.99 5 sztuk", "Zakup ksiazki: Wladca Pierscieni: Druzyna Pierscienia, 49.99, 3 sztuki"]
print("Witaj w systemie zarzadzania ksiegozbiorem bibliotecznym!")
while True:
    print("Wybierz jedna z ponizszych opcji (podajac tylko cyfre figurujaca przy danej opcj): ")
    komenda = input("""
        1. Doladowanie
        2. Wypozycz
        3. Zakup
        4. Biezacy_stan
        5. Zestawienie
        6. Szczegoly_ksiazki
        7. Dziennik
        8. Zakoncz
    Podajac cyfrę: """)
    match komenda:
        case "1":
            kwota = float(input("Podaj kwote o jaka chcesz zmienic saldo: "))
            if saldo + kwota < 0:
                print("Nie mozesz wykonac tej operacji i ustawic salda na wartosci ujemne.")
            else:
                saldo += kwota
            print(f"Saldo wynosi: {saldo}")
        case "2":
            isbn = input("Podaj nr. ISBN ksiazki do wypozyczenia: ")
            ksiazka_znaleziona = False
            for ksiazka in lista_ksiazek:
                ksiazka_znaleziona = True
                if ksiazka.get("ISBN") == isbn:
                    if ksiazka["ilosc_na_stanie"] <= 0:
                        print("Nie ma tej ksiazki na stanie")
                        break
                    ksiazka["ilosc_na_stanie"] -= 1
                    saldo += 10 # koszt wypozyczenia ksiazki
                    historia.append(f"Wypozyczenie ksiazki: {ksiazka['tytul']}, wartosc ksiazki {ksiazka['autor']}, sztuk 1")
                    print(f"Wypozyczenie ksiazki: {ksiazka['tytul']}, {ksiazka['autor']}, sztuk 1")
                    break
            if not ksiazka_znaleziona:
                print("Taka ksiazka nie istnieje w ksiegozbiorze")
        case "3":
            tytul = input("Podaj tytul ksiazki: ")
            autor = input("Podaj autora ksiazki: ")
            koszt = float(input("Podaj koszt zakupu ksiazki: "))
            ilosc = int(input("Podaj ilosc egzeplarzy: "))
            kategoria = input("Podaj kategorie ksiazki: ")
            numer_isbn = input("Podaj numer ISBN ksiazki: ")
            rok_wydania = int(input("Podaj rok wydania ksiazki: "))
            if saldo - (koszt * ilosc) < 0:
                print("Nie mozemy dokonac tego zakupu - wartosc zakupu przekracza wartosc salda.")
                historia.append(f"Proba zakupu ksiazki: {tytul}, {koszt}, {ilosc} sztuk - nieudana")
                continue
            else:
                saldo -= (koszt * ilosc)
            znaleziono_ksiazke = False # dodanie obiektu juz istniejacego na liscie
            for ksiazka in lista_ksiazek: # dodanie obiektu juz istniejacego na liscie
                if ksiazka.get("ISBN") == numer_isbn: # dodanie obiektu juz istniejacego na liscie
                    znaleziono_ksiazke = True # dodanie obiektu juz istniejacego na liscie
                    ksiazka["ilosc_na_stanie"] += ilosc # dodanie obiektu juz istniejacego na liscie
                    break # dodanie obiektu juz istniejacego na liscie
            if not znaleziono_ksiazke: # dodanie obiektu juz istniejacego na liscie
                lista_ksiazek.append({
                    "tytul": tytul,
                    "autor": autor,
                    "cena": koszt,
                    "ilosc_na_stanie": ilosc,
                    "ilosc": ilosc,
                    "kategoria": kategoria,
                    "ISBN": numer_isbn,
                    "rok_wydania": rok_wydania
                })
                # print(f"Lista ksiazek: {lista_ksiazek}")
                saldo -= (koszt * ilosc)
                historia.append(f"Zakupiono ksiazke: {tytul}, {koszt}, {ilosc} sztuk")
                for index, element in enumerate(lista_ksiazek):
                    print(f"Lista Ksiazek: Ksiazka {index + 1} na liscie ksiazek to: {element}")
                for index, element in enumerate(historia):
                    print(f"Historia Tranzakcji - Ksiazka {index + 1} w historii zakupow to: {element}")
                # print(f"Historia zakupow: {historia}")
                print(f"Saldo po zakupie ksiazki '{tytul}' wynosi {saldo} zl")
        case "4":
            print(f"W kasie jest {saldo} zl")
        case "5":
            for index, element in enumerate(lista_ksiazek):
                print(f"Zestawienie Ksiazek: Ksiazka {index + 1} w zestawieniu ksiazek to: {element}")
        case "6":
            isbn = input("Podaj nr. ISBN ksiazki do wyszukania: ")
            ksiazka_znaleziona = False
            for ksiazka in lista_ksiazek:
                ksiazka_znaleziona = True
                if ksiazka.get("ISBN") == isbn:
                    if ksiazka["ilosc_na_stanie"] <= 0:
                        print("Nie ma tej ksiazki na stanie")
                        break
                    ksiazka["ilosc_na_stanie"] -= 1
                    print(f"Ksiazka: {ksiazka['tytul']}, {ksiazka['autor']}, istnieje na stanie")
                    break
            if not ksiazka_znaleziona:
                print("Taka ksiazka nie istnieje w ksiegozbiorze")
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
        case "8":
            print("Zakonczono dzialanie programu.")
            break