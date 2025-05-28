# Abysmy mogli, abysmy mieli pewnosc, że wszystkie klucze w tej naszej strukturze, do ktorej chcemy chcieli przekazywac,
#   bedziemy chcieli tworzyc jakies obiekty takie rzeczywiste, abysmy mieli pewnosc, że te wszystkie klucze sa takie same
#   mozemy skorzystac z czegos takiego jak KLASY i OBIEKTY


###########################################
# przyklad - do tej pory ksiegarnie modlismy zrobic tak ale gdy ktos chcial dodac kolejna ksiazke i zrobil literowke w
#   kluczu to podczas wyszukiwania danej ksiazk za pomoca funkcji wystepowal blad
ksiazki = [
    {
        "tytul": "Harry potter",
        "autor": "J.K. Rowling",
        "rok_wydania": 1997,
        "gatunek": "fantazy",
    },
    {
        "tytul": "Wladca Pierscieni",
        "autor": "J.R.R. Tolkien",
        "rok_wydania": 1954,
        "gatunek": "fantazy",
    },
]


def dodaj_ksiazke(tytul, autor, rok_wydania, gatunek):
    ksiazka = {
        "tytul": tytul,
        "autor": autor,
        "rok_wydania": rok_wydania,
        "gatunek": gatunek,
    }
    ksiazki.append(ksiazka)
    print(f"Dodano ksiazke: {tytul} autorstwa {autor}.")


# dodanie ksiazki z kluczem z literowka
ksiazki.append(
    {
        "tytuł": "Wiedzmin",
        "autor": "Andrzej Sabkowski",
        "rok_wydania": 1990,
        "gatunek": "fantazy",
    }
)


# wyszukiwanie ksiazki za pomoca funkcji
def wyszukiwanie_ksiazki(tytul):
    for ksiazka in ksiazki:
        if ksiazka["tytul"] == tytul:
            return ksiazka


dodaj_ksiazke("Gra Endera", "Orson Scott Card", 1985, "sci-fi")

# to jest zamiast <print(ksiazki)>
for index, element in enumerate(ksiazki):
    print(f"Historia - Produkt {index} w historii zakupow to: {element}")

# print(ksiazki)

############ mozemy to zrobic poprawnie uzywajac KLAS <class>
# Jak zdefiniowac KLASE
# class - do definicji klasy uzywamy slowka kluczowego <class>
# class Ksiazki - po spacji wpisujemy nazwe klasy - w tym przypadku <Ksiazki>
# class Ksiazki: - po nazwie otwieramy blok kodu <dwokropkiem> :
# wewnatrz bloku kodu bedziemy mogli definiowac rozne klasy
# w tych naszych klasach jest jedna kluczowa metoda - metoda <__init__> odpowiadajaca za inicjalizacje obiektow klasy
#       inicjalizacja obiektow klasy to - jest nic innego jak upieczenie cisata z przepisu, <__init__> to sa skladniki
#       tego naszego dania - to sa klucze i wartosci w tym naszym slowniku

# class Ksiazki:
#   def __init__(self): - w nawiasach okraglych przekazujemy parametry metody - slowko <self> bedzie nam mowilo ze
#                           bedziemy cos chcieli modyfikowac cos na obiektach tej klasy. <self> jest tylko informacja
#                           co chcemy zrobic i nie przekazujemy tego dalej

# class Ksiazki:
#   def __init__(self, tytul, autor, rok_wydania, gatunek):   - po <self> przekazujemy wartosci ktore mozna przyrownac
#                                                               do wartosci wewnatrz slownika wartosci te musza miec
#                                                               swoje domyslne nazwy

# class Ksiazki:
#   def __init__(self, tytul, autor, rok_wydania, gatunek):   - wewnatrz tej funkcji <__init__> bloku kodu tej funkcji
#       self.nazwa = tytul                                      bedziemy te wartosci przypisywani do kluczy. Zeby stworzyc
#       self.autor = autor                                      klucz musimy uzyc slowka <sel.nazwa_kulucza>
#       self.rok_wydania = rok_wydania
#       self.gatunek = gatunek
#

# Do tego momentu stworzylismy przepis na nasze ciasto - czyli definicja naszej ksiazki
# Zeby to ciasto zrobic to musimy wywołac i stworzyc obiekt tej naszej ksiazki
# Zeby stworzyc obiekt naszej ksiazki to do naszej zmiennej bedziemy przypisywali wywolanie tej naszej klasy czyli <Ksiazka()>
# <Ksiazka> to jest nazwa klasy - w nawiasach okraglych bedziemy przekazywali parametry ktore przekazalismy do metody <__init__>
# class Ksiazki:
#   def __init__(self, tytul, autor, rok_wydania, gatunek):
#       self.nazwa = tytul
#       self.autor = autor
#       self.rok_wydania = rok_wydania
#       self.gatunek = gatunek
# ksiazka = Ksiazka("Wedzmin", "Andrzej Sabkowski", "1990", "fantazy")

# !!!!!!!!!!!!!!!!!!!!!!funkcje to sa funkcje ktore nie zaleza od klasy i od obiektu - definiujemy je na poziomie
#                       globalnym maxymalnie do lewej strony


# !!!!!!!!!!!!!!!!!!!!!!metody to sa funkcje ktore sa zdefiniowane wewnatrz klas - klasa to jest przepis na nasze ciasto
class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, gatunek):
        self.nazwa = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek

    def __str__(self):
        return f"{self.nazwa} ({self.rok_wydania}) - {self.autor} [{self.gatunek}]"  # druga z takich specjalnych metod
#                                                                                   wykonywana kiedy bedziemy printowani
#                                                                                   nasza ksiazke zebyscie wiedzieli co
# przypadkowa nazwa = nazwa klasy                                                    jest czym
ksiazka = Ksiazka("Wedzmin", "Andrzej Sabkowski", "1990", "fantazy")
print(ksiazka)


# abysmy pobrali jakas wartosc przypisana do naszego pola (w slowniku był <nazwa klucza>) <nazwa> to printujemy - print(ksiazka.nazwa)
print(ksiazka.nazwa)
print(ksiazka.gatunek)


# zeby zmienic wartosc pola (w slowniku to byla wartosc klucza)
ksiazka.autor = "Adam Kulesza"
print(ksiazka)


# aby dokladac jakies wartosci i pola - TO NIE JEST ZMIANA DEFINICJI KALASY TYLKO DODANIE CZEGOS INNEGO
#                                 GLOWNY PRZEPIS NIE ZOSTAL ZMIENIONY DLATEGO NIE PRINTUJE NAM TEGO JAKO CZESC HISTOTII
#                                 Nie robmy tego tak mimo ze mozemy!!!!!!!
ksiazka.isbn = "12-884-6110-59-1"
print(ksiazka.isbn)

# Mozna twozyc sbie nieskonczenie wiele obiektow
# ksiazka_2 = Ksiazka("Harry Poter i Wiezien Askabanu", "J.K. Rowling", 1997, "fantazy")
#
# lista_ksiazek = [ksiazka, ksiazka_2,
#                  Ksiazka("Wladca Pierscieni", "J.R.R. tolkien", 1954, "fantazy"),
#                  Ksiazka( "Zlodziejska ksiazka", "Markus Zusak", 2005, "powiesc")]


#################################################
#################################################
auto = {
    "marka": "Audi",
    "model": "A4",
    "rok_produkcji": 2020,
    "przebieg": 15000,
    "aktualny_bieg": "neutralny",
    "silnik_wlaczony": False,
    "predkosc": 0,
    "rodzaj_opon": "letnie",
}
# chcemy wlaczyc silnik i przejechac 3 km
# najpierw wlaczamy silnik


def wlacz_silnik(auto):
    if auto["silnik_wlaczany"]:
        print("Silnik juz jest wlaczony.")
    else:
        auto["silnik_wlaczany"] = True
        print("Silnik zostal wlaczony")


# nie zawsze wiemy ze silnik jest wlaczony
# zeby przejechac 5 kilometrow to musze zrobic tak


class Auto:
    def __init__(
        self,
        marka,
        model,
        rok_produkcji,
        przebieg,
        aktualny_bieg,
        silnik_wlaczony,
        predkosc,
        rodzaj_opon,
    ):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.aktualny_bieg = aktualny_bieg
        self.silnik_wlaczony = silnik_wlaczony
        self.predkosc = predkosc
        self.rodzaj_opon = rodzaj_opon

    # co my teraz mozemy tu zrobic - np zmienic opony
    def zmien_opony(self, nowy_rodzaj_opon):
        self.rodzaj_opon = nowy_rodzaj_opon
        print(f"Zmieniono opony na {nowy_rodzaj_opon}")

    # mozemy wewnatrz klas definiowac swoje wlasne funkcje, swoje wlasne metody, ktore moga mi robic rozne obliczenia
    # dzieki temu ja wiem ze te metody beda dzialaly dokladnie tak samo na kazdym z tych aut i bede mial pewnosc, ze kazde
    # auto bedzie wygladalo w ten sposob a nie ze bede mial cokolwieg innego - bo mozemy przekazac do tego <wlacz_silnik>
    # ten powyzszy slownik <auto> ktory ma wlaczony silnik albo zaraz przekazac inny slownik ktory tego silnika nie bedzi
    # mial waczonego

    # to <self> wewnatrz tej funkcji bedzie pozwalalo nam na zmiane stanu obiektu tej klasy
    def wlacz_silnik(self):
        if self.silnik_wlaczony:
            print("Silnik juz jest wlaczony.")
        else:
            self.silnik_wlaczony = True
            print("silnik zostal wlaczony.")


auto = Auto("Audi", "A4", 2020, 15000, "neutralny", False, 0, "letnie")

auto.wlacz_silnik()
print(auto.silnik_wlaczony)
# Ja w ten sposob zmodyfikowalem tę moja wartosc za pomoca jakiejs metody
# bez problemu mozemy robic wowczas takie rzeczy

if auto.silnik_wlaczony:
    print("Silnik jest wlaczony.")
else:
    print("Silnik jest wylaczony.")
