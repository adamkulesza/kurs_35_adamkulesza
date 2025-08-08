
#CHCEMY ZEBY Z MODULU (pliku) file_handler ZAIMPORTOWAC TEN NASZ OBIEKT file_handler (mamy go tak nazwanego w ostatniej linijce kodu w pliku file_handler.py)
from file_handler import file_handler, save_temporary_data

# bedziemy dzialali w petli - while True:
# lista ksiazek - lista wszystkich ksiazek gdzie kazda ksiazka jest slownikiem



# while True:
#     print(
#         "\nWybierz jedna z ponizszych opcji (podajac tylko cyfre figurujaca przy danej opcj): "
#     )
#     komenda = input("""
#         1. Doladowanie
#         2. Wypozycz
#         3. Zakup
#         4. Biezacy_stan
#         5. Zestawienie
#         6. Szczegoly_ksiazki
#         7. Dziennik
#         8. Zakoncz
#     Podajac cyfrę: """)
#     match komenda:
#         case "1":
#             kwota = float(input("Podaj kwote o jaka chcesz zmienic saldo: "))
#             if saldo + kwota < 0:
#                 print(
#                     "Nie mozesz wykonac tej operacji i ustawic salda na wartosci ujemne."
#                 )
#             else:
#                 saldo += kwota
#             print(f"Saldo wynosi: {saldo}")
#             save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#         case "2":
#             isbn = input("Podaj nr. ISBN ksiazki do wypozyczenia: ")
#             ksiazka_znaleziona = False
#             for ksiazka in lista_ksiazek:
#                 if ksiazka.get("ISBN") == isbn:
#                     if ksiazka["ilosc_na_stanie"] <= 0:
#                         print("Nie ma tej ksiazki na stanie")
#                         break
#                     ksiazka["ilosc_na_stanie"] -= 1
#                     saldo += 10  # koszt wypozyczenia ksiazki
#                     historia.append(
#                         f"Wypozyczenie ksiazki: {ksiazka['tytul']}, wartosc ksiazki {ksiazka['autor']}, sztuk 1"
#                     )
#                     print(
#                         f"Wypozyczenie ksiazki: {ksiazka['tytul']}, {ksiazka['autor']}, sztuk 1"
#                     )
#                     ksiazka_znaleziona = True
#                     save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#                     break
#             if not ksiazka_znaleziona:
#                 print("Taka ksiazka nie istnieje w ksiegozbiorze")
#             for index, element in enumerate(lista_ksiazek):
#                 print(
#                     f"Lista Ksiazek: Ksiazka {index + 1} na liscie ksiazek to: {element}"
#                 )
#         case "3":
#             tytul = input("Podaj tytul ksiazki: ")
#             autor = input("Podaj autora ksiazki: ")
#             koszt = float(input("Podaj koszt zakupu ksiazki: "))
#             ilosc = int(input("Podaj ilosc egzeplarzy: "))
#             kategoria = input("Podaj kategorie ksiazki: ")
#             numer_isbn = input("Podaj numer ISBN ksiazki: ")
#             rok_wydania = int(input("Podaj rok wydania ksiazki: "))
#             if saldo - (koszt * ilosc) < 0:
#                 print(
#                     "Nie mozemy dokonac tego zakupu - wartosc zakupu przekracza wartosc salda."
#                 )
#                 historia.append(
#                     f"Proba zakupu ksiazki: {tytul}, {koszt}, {ilosc} sztuk - nieudana"
#                 )
#                 save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#                 continue
#             else:
#                 saldo -= koszt * ilosc
#             znaleziono_ksiazke = False  # dodanie obiektu juz istniejacego na liscie
#             for ksiazka in lista_ksiazek:  # dodanie obiektu juz istniejacego na liscie
#                 if (
#                     ksiazka.get("ISBN") == numer_isbn
#                 ):  # dodanie obiektu juz istniejacego na liscie
#                     znaleziono_ksiazke = (
#                         True  # dodanie obiektu juz istniejacego na liscie
#                     )
#                     ksiazka["ilosc_na_stanie"] += (
#                         ilosc  # dodanie obiektu juz istniejacego na liscie
#                     )
#                     break  # dodanie obiektu juz istniejacego na liscie
#             if not znaleziono_ksiazke:  # dodanie obiektu juz istniejacego na liscie
#                 lista_ksiazek.append(
#                     {
#                         "tytul": tytul,
#                         "autor": autor,
#                         "cena": koszt,
#                         "ilosc_na_stanie": ilosc,
#                         "ilosc": ilosc,
#                         "kategoria": kategoria,
#                         "ISBN": numer_isbn,
#                         "rok_wydania": rok_wydania,
#                     }
#                 )
#                 # print(f"Lista ksiazek: {lista_ksiazek}")
#                 saldo -= koszt * ilosc
#                 historia.append(f"Zakupiono ksiazke: {tytul}, {koszt}, {ilosc} sztuk")
#                 save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#                 for index, element in enumerate(lista_ksiazek):
#                     print(
#                         f"Lista Ksiazek: Ksiazka {index + 1} na liscie ksiazek to: {element}"
#                     )
#                 for index, element in enumerate(historia):
#                     print(
#                         f"Historia Tranzakcji - Ksiazka {index + 1} w historii zakupow to: {element}"
#                     )
#                 # print(f"Historia zakupow: {historia}")
#                 print(f"Saldo po zakupie ksiazki '{tytul}' wynosi {saldo} zl")
#         case "4":
#             print(f"W kasie jest {saldo} zl")
#         case "5":
#             for index, element in enumerate(lista_ksiazek):
#                 print(
#                     f"Zestawienie Ksiazek: Ksiazka {index + 1} w zestawieniu ksiazek to: {element}"
#                 )
#         case "6":
#             isbn = input("Podaj nr. ISBN ksiazki do wyszukania: ")
#             ksiazka_znaleziona = False
#             for ksiazka in lista_ksiazek:
#                 if ksiazka.get("ISBN") == isbn:
#                     ksiazka_znaleziona = True
#                     if ksiazka["ilosc_na_stanie"] <= 0:
#                         print("Nie ma tej ksiazki na stanie")
#                         break
#                     print(
#                         f"Ksiazka: {ksiazka['tytul']}, {ksiazka['autor']}, {ksiazka['ilosc_na_stanie']} sztuk istnieje na stanie"
#                     )
#                     break
#             if not ksiazka_znaleziona:
#                 print("Taka ksiazka nie istnieje w ksiegozbiorze")
#         case "7":
#             od = input("Podaj wartosc 'od' (numer tranzakcji): ")
#             do = input("Podaj wartosc 'do' (numer transakcji): ")
#             if od:
#                 od = int(od)
#             else:
#                 od = 0
#             if do:
#                 do = int(do)
#             else:
#                 do = len(historia)
#             print(historia[od:do])
#         case "8":
#             print("Zakonczono dzialanie programu.")
#             break

# file_handler.ksiegozbior = lista_ksiazek
# file_handler.saldo = saldo
# file_handler.historia = historia
# file_handler.save_ksiegozbior_file()
# file_handler.save_saldo_file()
# file_handler.save_historia_file()

def get_books():
    """Zwroc liste ksiazek z biblioteki"""
    return file_handler.ksiegozbior

def get_bookstore_state():
    """Returns the current state of the bookstore, including balance and history."""
    return {
        "saldo": file_handler.saldo,
        "historia": file_handler.historia,
        "ksiegozbior": get_books(),
    }

def create_new_book(book_form: dict):
    new_book = {
        "tytul": book_form.get("tytul"),
        "autor": book_form.get("autor"),
        "cena": float(book_form.get("cena",  0)),
        "ilosc_na_stanie": int(book_form.get("ilosc_na stanie", 0)),
        "ilosc": int(book_form.get("ilosc", 0)),
        "kategoria": book_form.get("kategoria"),
        "ISBN": book_form.get("isbn"),
        "rok_wydania": int(book_form.get("rok_wydania", 0))
    }
    file_handler.ksiegozbior.append(new_book)
    save_temporary_data(file_handler, file_handler.ksiegozbior, file_handler.saldo, file_handler.historia)

def update_book(isbn: str, book_form: dict):
    """Updates the book with the given ISBN using the provided book form."""
    # for book in lista_ksiazek:
    #     if book["ISBN"] == isbn:
    #         book.update(book_form)
    #         save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
    #         return book
    # return None
    pass

def change_saldo(amount: float):
    """Changes the current balance by the specified amount."""
    saldo = file_handler.saldo
    if saldo + amount < 0:
        raise ValueError("Cannot set balance to a negative value.")
    saldo += amount
    save_temporary_data(file_handler, file_handler.ksiegozbior, saldo, file_handler.historia)