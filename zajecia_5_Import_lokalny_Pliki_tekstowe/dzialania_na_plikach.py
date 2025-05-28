"""Zebysmy otwierali sobie polaczenia z takimi plikami, zebysmy mogli odczytywac jakies zewnetrzne pliki typu .txt, .csv, .json,
rozne inne pliki nie pythonowe mozemy skorzystac z takich specjalnych funkcji do otwierania po prostu tych plikow.
I aby otworzyc taki plik piszemy:"""

file = open("piosenka.txt") #otwieramy polaczenie do pliku

"""zeby odczytac jakies rzeczy z tego pliku - mozna je czytac w calosci albo linijka po linijce

- odczytywanie w calosci - robimy to w nastepujacy sposob"""
# print(file.read())

"""
- odczytywanie linijka po linijce - robimy to w nastepujacy sposob - otrzymujemy odczyt z pierwszej linijki"""
# print(file.readline())
"""polaczenie z plikiem jest caly czas otwarte - wiec po wpiszaniu po raz kolejny <print(file.readline()) otrzymamy
odczyt juz z drugiej linijki"""
# print(file.readline())

"""mozemy tez zrobic odczytanie w taki sposob - to dzialanie tez bedzie nam odczytywalo plik poniewaz ta funkcja open to
taki generator"""

# for line in file:
#     print(line)
#
# """TRZY ROZNE RODZAJE ODCZYTYWANIA"""
file.read()
# file.readline()
# print(file.readlines()) #zwroci nam piosenke w postaci listy tych naszych linijek
file.close()

"""Jezeli polaczenie jest do pliku otwarte i on juz caly plik odczytal a my chcemy zeby jeszcze raz odczytal to on nam
wyrzuci pusta linijke - Dlaczego? bo juz wszystko przeczytal i nie ma nic do odczytania - wewnatrz tego polaczenia mamy
juz wszystko odczytane.
Zeby przeczytal cos na nowo to co wobec tego mozemy zrobic? To mozemy zamknac polaczenie i otworzyc je na nowo.
KLUCZOWE JEST ZEBY TE POLACZENIA ZAMYKAC"""


def oblicz_sume_wydatkow(plik):
    file = open(plik)
    suma = 0
    for line in file:
        kwota = int(line)
        suma =+kwota
        file.close()

# oblicz_sume_wydatkow("piosenka.txt")

"""CONTEXT MANAGER
- ta struktura implementuje takie dwie metody <enter> oraz <exit> i pozwalac ona bedzie nam jako
programistom na robienie jakich kolwiek operacji, ktore beda sie nam podobaly, czy to bedzie rzutowanie na inta, czy to
bedzie cokolwiek innego
NAJWAZNIEJSZE JESTTO ZE CONTEXT MANAGERY BEDA NAM AUTOMATYCZNIE OTWIERAC I ZAMYKAC POLACZENIA NIE MARTWIAC SIE O TO
CZY TEN KOD SIE WYWALI"""
"""Skladnia uzycia"""
# with open("piosenka.txt") as file:
#     for line in file:
#         print(line)

"""Jak takie CONTEXT MANAGERY sie pisze???
wyjscie z kolegami na piwo - najpierw piszemy klase - zeby ta nasza klasa byla context managerem musi ona miec dwie metody
- metoda __enter__
- metoda __exit__
CONTEXT MANAGER bedzie w srodku poniedzy enter a exit"""

# class WyjscieZKolegamiNaPiwo:
#     def __enter__(self):
#         print("Prosimy zone o pozwolenie")
#         print("Obiecujemy, ze nie wrocimy za pozno")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Prosimy zone o wybaczenie")
#         print("Kupujemy kwiaty")
#         print("Obiecujemy, ze to ostatni raz")
#
# with WyjscieZKolegamiNaPiwo() as piwo:
#     print("Idziemy na piwo")
#     print("Pijemy piwo")
#     print("Wracamy do domu")

"""Wiedzac juz teraz czym CONTEKST MANAGERY sa staraj sie otwierac polaczenia za pomoca context managerow"""
"""Aby zapisac musimy uzyc metody <plik.write>
Nalezy pamietac ze metoda <open> moze miec cos po przecinku. To co jest po tym przecinku mowi nam w jakim trybie
bedziemy te pliki otwierali - domysnie mamy tryb <r>
Aby to zmienic trzeba w nawiasie po nazwie pliku dodac przecinek i wpisac w cudzyslowiu odpowiednie oznaczenie.

w       tworzymy plik od nowa - oznacza, ze tworzy ci plik jak nie ma i do tego kursor jest na poczatku pliku - do nowego zapisu bez czytania
w+      to samo tylko z czytaniem
a       tworzy plik i kursor na koncu(mozemy dopisywac) nie mozemy czytac
a+      tworzy plik, kursor na koncu plus mozemy odczytywac
r       otwiera plik do odczytu
r+      otwiera plik do odczytu i zapisu - kursor na początku
a+ od r+ różni się tym, że w a+ tworzymy plik jak go nie mamy
"""

"""Nadpisywanie pliku "w" """
# with open("piosenka.txt", "w") as plik:
#     nowy_text = "Dodatkowa linijka\n"
#     plik.write(nowy_text)

"""Dopisywanie linijki na koncu pliku "a" """
# with open("piosenka.txt", "a") as plik:
#     nowy_text = "\nDodatkowa linijka"
#     plik.write(nowy_text)
#
"""Aby miec zarowno odczytywanie i zapisywanie tego pliku to korzystamy z modu "w+" """
# with open("piosenka.txt", "w+") as plik:
#     for linia in plik:
#         print(linia)
#     nowy_text = "Dodatkowa linijka\n"
#     plik.write(nowy_text)

"""Kolejnym modem aby miec zarowno odczytywanie i zapisywanie tego pliku to korzystamy z modu "r+" linijka na poczatku"""

# with open("piosenka.txt", "r+") as plik:
#     for line in plik:
#         print(line) #wszystkie linie z pliku zostana wyprintowane
#     nowy_tekst =  "<<<Dodatkowa linijka\n" #dodatkowa linijka zostala dopisana na koncu pliku piosenka.txt
#     plik.write(nowy_tekst) #plik zostal zapisany

"""tworzy plik, kursor na koncu plus mozemy odczytywac - ten mode "a+" jezeli otwieramy jakis plik ktorego nie ma,
to on go automatycznie stowrzy"""
with open("piosenka1.txt", "a+") as plik:
    nowy_tekst = "\n<<<<Linijka dodatkowa\n"
    plik.write(nowy_tekst)
    for linia in plik:
        print(linia)