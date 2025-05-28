"""
Program do obsługi bazy szkolnej
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel,
wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.

Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
Polecenie "koniec" - Kończy działanie aplikacji.



Proces tworzenia użytkowników:

    Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji
(oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne,
jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, albo dwie, jeżeli zostanie
to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi
nauczyciel, aż do otrzymania pustej linii.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie
to poprawnie obsłużone), a także nazwę prowadzonej klasy.
    Polecenie "koniec" - Wraca do pierwszego menu.



Proces zarządzania użytkownikami:

    Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji
(oprócz "koniec") wyświetla to menu ponownie.
    Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów,
którzy należą do tej klasy, a także wychowawcę tejże klasy.
    Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a
także nauczycieli, którzy je prowadzą.
    Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które
prowadzi nauczyciel.
    Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których
prowadzi wychowawca.
    Polecenie "koniec" - Wraca do pierwszego menu..
"""


class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.klasa})"


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, lista_klas_nauczyciela):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasa_nauczyciela = lista_klas_nauczyciela

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.przedmiot})\nLista klas: {self.klasa_nauczyciela}"


class Wychowawca:
    def __init__(self, imie, nazwisko, numer_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_klasy = numer_klasy

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} ({self.numer_klasy}"


Szkola = {
    "uczniowie": [
        Uczen("Adam", "Kulesza", "1A"),
        Uczen("Lukasz", "Korolczuk", "1B"),
        Uczen("Marek", "Wojnowski", "1C"),
    ],
    "nauczyciele": [
        Nauczyciel("Magdalena", "Popowicz", "geografia", "1A, 1B, 1C"),
        Nauczyciel("Piotr", "Lehmann", "fizyka", "1B, 1C"),
        Nauczyciel("Agnieszka", "Gil", "matematyka", "1A, 1B, 1C"),
    ],
    "wychowawcy": [
        Wychowawca("Piotr", "Milo", "1A"),
        Wychowawca("Malgorzata", "Ferenc", "1B"),
        Wychowawca("Krzysztof", "Pac", "1C"),
    ],
}

###### 1
def wyszukaj_uczniow_klasy(numer_klasy):
    uczniowie_danej_klasy = []
    for uczen in Szkola.get("uczniowie"):
        if uczen.klasa == numer_klasy:
            uczniowie_danej_klasy.append(uczen)
    return uczniowie_danej_klasy

def wyszukaj_wychowawce_klasy(numer_klasy):
    wychowawca_danej_klasy = []
    for wychowawsca in Szkola.get("wychowawcy"):
        if wychowawsca.numer_klasy == numer_klasy:
            wychowawca_danej_klasy.append(wychowawsca)
    return wychowawca_danej_klasy

####### 2
def wyszukaj_nauczyciela_ucznia(imie, nazwisko):
    numer_klasy_ucznia = None
    for uczen in Szkola.get("uczniowie"):
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            numer_klasy_ucznia = uczen.klasa
            break
    if numer_klasy_ucznia:
        for nauczyciel in Szkola.get("nauczyciele"):
            if numer_klasy_ucznia in nauczyciel.klasa_nauczyciela:
                return nauczyciel.przedmiot

####### 3
def wyszukaj_numery_klas_nauczyciela(imie, nazwisko):
    for nauczyciel in Szkola.get("nauczyciele"):
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            return nauczyciel.klasa_nauczyciela

####### 4
def wyszukaj_klase_wychowawcy(imie, nazwisko):
    for wychowawca in Szkola.get("wychowawcy"):
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            return wychowawca.numer_klasy



while True:
    wybor_uzytkownika = input(
        "Wybierz opcje (podaj cyfre): \n"
        "1. Utworz - proces tworzenia uzytkownika.\n"
        "2. Zarzadzaj - proces zarzadzania uzytkownikami\n"
        "3. Zakoncz\n"
    )

    match wybor_uzytkownika:
        case "1":
            obiekt_do_dodanie = input(
                "Wybierz do dodania jedna z podanych opcji: \n"
                "1. Uczen.\n"
                "2. Nauczyciel.\n"
                "3. Wychowawca.\n"
                "4. Zakoncz.\n"
            )
            if obiekt_do_dodanie.strip() in ("1", "Uczen", "Ucznia", "uczen", "ucznia"):
                imie = input("Podaj imie ucznia: ")
                nazwisko = input("Podaj nazwisko ucznia: ")
                klasa = input("Podaj klase ucznia: ")
                nowy_uczen = Uczen(imie, nazwisko, klasa)
                Szkola["uczniowie"].append(nowy_uczen)
            elif obiekt_do_dodanie.strip() in (
                "2",
                "Nauczyciel",
                "Nauczyciela",
                "nauczyciel",
                "nauczyciela",
            ):
                imie = input("Podaj imie nauczyciela: ")
                nazwisko = input("Podaj nazwisko nauczyciela: ")
                przedmiot = input("Podaj prowadzony przedmiot: ")
                klasa_nauczyciela = []
                while True:
                    klasa = input("Podaj numer klasy: ")
                    if klasa:
                        klasa_nauczyciela.append(klasa)
                    else:
                        break
                nowy_nauczyciel = Nauczyciel(
                    imie, nazwisko, przedmiot, klasa_nauczyciela
                )
                Szkola["nauczyciele"].append(nowy_nauczyciel)
            elif obiekt_do_dodanie.strip() in (
                "3",
                "Wychowawca",
                "Wyychowawce",
                "wychowawca",
                "wychowawce",
            ):
                imie = input("Podaj imie wychowawcy: ")
                nazwisko = input("Podaj nazwisko wychowawcy: ")
                numer_klasy_wychowawcy = input("Podaj nazwe prowadzonej klasy: ")
                nowy_wychowawca = Wychowawca(imie, nazwisko, numer_klasy_wychowawcy)
                Szkola["wychowawcy"].append(nowy_wychowawca)
            else:
                break
        case "2":
            opcje_do_zarzadzania = input(
                "Wybierz opcje do zarzadzania z ponizszej listy: \n"
                "1. Klasa\n"
                "2. Uczen\n"
                "3. Nauczyciel\n"
                "4. Wychowawca\n"
                "5. Zakoncz\n"
            )
            match opcje_do_zarzadzania:
                case "1":
                    numer_klasy = input("Podaj numer klasy: ")
                    uczniowie_klasy = wyszukaj_uczniow_klasy(numer_klasy)
                    wychowawca_klasy = wyszukaj_wychowawce_klasy(numer_klasy)
                    print(f"\nUczniowie klasy {numer_klasy}: {uczniowie_klasy},\nWychowawca klasy: {wychowawca_klasy}\n")
                case "2":
                    imie_ucznia = input("Podaj imie ucznia: ")
                    nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
                    nauczyciel_i_przedmiot_dla_dla_ucznia = wyszukaj_nauczyciela_ucznia(imie_ucznia, nazwisko_ucznia)
                    print(nauczyciel_i_przedmiot_dla_dla_ucznia)
                case "3":
                    imie_nauczyciela = input("Podaj imie nauczyciela: ")
                    nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
                    nauczyciel_klasy = wyszukaj_numery_klas_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela)
                    print(f"\nNauczyciel {imie_nauczyciela, nazwisko_nauczyciela}\nUczy klasy {nauczyciel_klasy}\n")
                case "4":
                    imie_wychowawcy = input("Podaj imie wychowawcy: ")
                    nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ")
                    numer_klasy_wychowawcy = wyszukaj_klase_wychowawcy(imie_wychowawcy, nazwisko_wychowawcy)
                    uczniowie_klasy = wyszukaj_uczniow_klasy(numer_klasy_wychowawcy)
                    print(f"\nTen wychowawca jest wychowawca dla uczniow klasy {numer_klasy_wychowawcy}: {uczniowie_klasy}\n")
                case "5":
                    break

        case "3":
            break
