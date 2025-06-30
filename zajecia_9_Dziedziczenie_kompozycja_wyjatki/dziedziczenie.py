# # Mamy cos takiego jak kalsy. wiec zdefiniujmy sobie:
# class Zwierze:
#     def __init__(self, imie):
#         self.imie = imie
#
#     def przedstaw_sie(self):
#         return f"Jestem {self.imie}."
#
#     def daj_glos(self):
#         return "Zwierze wydaje dzwiek."
#
# # Zalozmy ze robimy aplikacje dla ogrodu botanicznego wiec robimy kolejne klasy dla innych zwierzat:
#
# class Lew:
#     def __init__(self, imie):
#         self.imie = imie
#
#     def przedstaw_sie(self):
#         # return f"Jestem lew o imieniu {self.imie}."
#         return f"Jestem zwierzeciem o imieniu {self.imie}."
#
#     def daj_glos(self):
#         return "Roar"
#
# class Pies:
#     def __init__(self, imie):
#         self.imie = imie
#
#     def przedstaw_sie(self):
#         # return f" Jestem pies o imieniu {self.imie}."
#         return f"Jestem zwierzeciem o imieniu {self.imie}."
#
#     def daj_glos(self):
#         return "Hau hau!"
#
# class Ryba:
#     def __init__(self, imie):
#         self.imie = imie
#
#     def przedstaw_sie(self):
#         # return f"Jestem ryba o imieniu {self.imie}"
#         return f"Jestem zwierzeciem o imieniu {self.imie}."
#
#     def daj_glos(self):
#         return "Glub glub!"
#
# krol_lew = Lew("Simba")
# print(krol_lew.przedstaw_sie())
#
# pies_domowy = Pies("Burek")
#
# zlota_rybka = Ryba("Zlotko")
from asyncio import gather


# Mamy nasz eobiekty i rozne klasy podefiniowana.
# Jaki problem definicji tyc klas aktualnie mamy?????????
# problemem jest ze kazda z tych klas ma jeden do jeden ta sama metode <__init__>. A teraz w tym momencie zmienilismy
# wszystkie metody <przedstaw_sie> na takie same. Dlugosc powielonego kodu jest duza. Mamy duzo wspolnych czesci.
# Wiemy tez ze Lew, Pies i Ryba sa Zwierzetami.
# Mozemy czesci wspolne naszego kodu wyniesc do rodzica.
# Mozemy sobie pomyslec o tym ze w programowaniu jestesmy w stanie zrobic wszystko w postaci drzewa genealogicznego.
# Na ten moment Lew, Pies i ryba sa na tym samym poziomie - czyli to sa bracia i siostry.
# Natomiast wiemy, że to nasze Zwierze jest czyms wyzej zdefiniowanym. Mozemy to zwierze wyniesc troche wyzej i zamiast
# takiej plaskiej struktury, ktora mamy mozemy sobie zrobic strukture beardziej drzewiasta.
#Jak to napisac?
# Chcielibysmy zeby Lew Pies i Ryba dziedziczyli po tym zwierzeciu. Checmu zeby Zwierze bylo poziom wyzej.
# !!!!!!!!!!!Zeby stwierdzic, ze Pies, Lew oraz Ryba sa potomkami tego naszego Zwierzecia to w momencie definicji naszej
# klasy w nawiasach okraglych po nazwie bedziemy wpisywali nazwe klasy po ktorej ta klasa dziedziczy <class Lew(Zwierze)> itd.
# Pies, Lew oraz ryba beda dziedziczyli po naszym Zwierzeciu. Dodatkowo mozemy usunac wszystkie funkcje ktore sie
# powtarzaja i zostawic tylko w tej klasie nadrzednej


# class Zwierze:
#     def __init__(self, imie):
#         self.imie = imie
#
#     def przedstaw_sie(self):
#         print("Przedstaw sie")
#         print("Witaj w ZOO w Nowym Yorku!!")
#         return f"Jestem {self.imie}."
#
#     def daj_glos(self):
#         return "Zwierze wydaje dzwiek."
#
#
# class Lew(Zwierze):
#     def __init__(self, imie):
#         self.imie = imie
#
#     def daj_glos(self):
#         return "Roar"
#
# class Pies(Zwierze):
#     def __init__(self, imie):
#         self.imie = imie
#
#     def daj_glos(self):
#         return "Hau hau!"
#
# class Ryba(Zwierze):
#     def __init__(self, imie):
#         self.imie = imie
#
#     def daj_glos(self):
#         return "Glub glub!"
#
# krol_lew = Lew("Simba")
# print(krol_lew.przedstaw_sie())
#
# pies_domowy = Pies("Burek")
# print(pies_domowy.przedstaw_sie())
#
# zlota_rybka = Ryba("Zlotko")
# print(zlota_rybka.przedstaw_sie())

# I teraz jezeli cos dopiszemy do klasy <Zwierze> automatycznie zostanie dodane do klas ktore po nim dziedzicza np.
# Jezeli dpoiszemy w klasie <Zwierze> do funkcji <Przedstaw_sie> takie dwa printy
# print("Przedstaw sie")
# print("Witaj w ZOO w Nowym Yorku!!")
# to automatycznie zostana one dodane do wszystkich klas ktore dziedzicza po klasie <Zwierze>




# Jezeli na przyklad w ktorejs klasie ktora dziedziczy po kalsie <Zwierze> jednak zostawimy metode <Przedstaw_sie> to ta
# metoda nadpisze nam dziedziczona metode i spowoduje ze dana klasa bedzie unikatowa

class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("Przedstaw sie")
        print("Witaj w ZOO w Nowym Yorku!!")
        return f"Jestem {self.imie}."

    def daj_glos(self):
        return "Zwierze wydaje dzwiek."


# class Lew(Zwierze):
#     def __init__(self, imie):
#         self.imie = imie
#
#     def przedstaw_sie(self):
#         print("Jestem krolem Dżungli!")
#         return f"Jestem lwem o imieniu {self.imie}."
#
#     def daj_glos(self):
#         return "Roar"
#
# class Pies(Zwierze):
#     def __init__(self, imie):
#         self.imie = imie
#
#     def daj_glos(self):
#         return "Hau hau!"
#
# class Ryba(Zwierze):
#     def __init__(self, imie):
#         self.imie = imie
#
#     def daj_glos(self):
#         return "Glub glub!"
#
# krol_lew = Lew("Simba")
# print(krol_lew.przedstaw_sie())
#
# pies_domowy = Pies("Burek")
# print(pies_domowy.przedstaw_sie())
#
# zlota_rybka = Ryba("Zlotko")
# print(zlota_rybka.przedstaw_sie())


# W pythonie mozemy miec wiecej niz jednego rodzica
# Nastepnie mozemy miec babcie i dziadka dla kazdego z rodzicow
# Jak to dziala
# Zrobmy sobie ze Ryba nie dziedziczy po klasie <Zwierze>
# Stworzmy sobie kolejna klase <Rekin>, ktory dziedziczy po klasie <Ryba> i dziedziczy po klasie <Zwierze>

class Lew(Zwierze):
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("Jestem krolem Dżungli!")
        return f"Jestem lwem o imieniu {self.imie}."

    def daj_glos(self):
        return "Roar"

class Pies(Zwierze):
    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        return "Hau hau!"

class Ryba:
    def __init__(self, imie, gatunek="ryba"):
        self.imie = imie
        self.gatunek = gatunek

    def plywaj(self):
        return "Plywam w wodzie."

    def przedstaw_sie(self):
        return f"Jestem ryba o imieniu {self.imie}, jestem {self.gatunek}."

class Rekin(Ryba, Zwierze):
    def __init__(self, imie, gatunek="rekin"):
        Zwierze.__init__(self, imie)
        Ryba.__init__(self, imie, gatunek)

# krol_lew = Lew("Simba")
# print(krol_lew.przedstaw_sie())
#
# pies_domowy = Pies("Burek")
# print(pies_domowy.przedstaw_sie())
#
# zlota_rybka = Ryba("Zlotko")
# print(zlota_rybka.przedstaw_sie())

rekin_bialorybi = Rekin( "Rekin", "bialy")

print(rekin_bialorybi.przedstaw_sie())
# wyprintowal nam metode przedstaw_sie dziedziczona po klasie <Ryba> - decyduje o tym algorytm RMO
# Ten algorytm mowi nam ze kolejnosc klas po ktorych dziedziczymy (ktore znajduja sie w nawiasie) ma znaczenie. Od lewej
# strony beda dla nas najwazniejsze rzeczy.


#       Mama                           Tata
#           \                           /
#                        Syn

# Jak ten algorytm dziala?
# Jezeli mamy drzewko Syn - Mama - Tata
# Ten algorytm sprawdza czy w obiekcie <Syn> cos mamy jezeli w tym obiekcie czegos brakuje to nastepnie stpawdza obiekt <Mama>
# Jezeli w obiekcie mama czegos nie mamy to sprawdza obiekt <Tata>
# ale nie zawsze mamy drzewko tylko dwopoziomeowe jak tutaj


#Zrobmy sobie teraz cos innego. dodajmy klase <Plywajace> i usuwany przedstaw sie z klasy <Ryba> i Ryba dziedziczy po <Plywajace>

class Lew(Zwierze):
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("Jestem krolem Dżungli!")
        return f"Jestem lwem o imieniu {self.imie}."

    def daj_glos(self):
        return "Roar"

class Pies(Zwierze):
    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        return "Hau hau!"

class Plywajace:
    def przedstaw_sie(self):
        return "Jestem zwierzeciem wodnym."

class Ryba:
    def __init__(self, imie, gatunek="ryba"):
        self.imie = imie
        self.gatunek = gatunek

    def plywaj(self):
        return "Plywam w wodzie."


class Rekin(Plywajace):
    def __init__(self, imie, gatunek="rekin"):
        Zwierze.__init__(self, imie)
        Ryba.__init__(self, imie, gatunek)

# krol_lew = Lew("Simba")
# print(krol_lew.przedstaw_sie())
#
# pies_domowy = Pies("Burek")
# print(pies_domowy.przedstaw_sie())
#
# zlota_rybka = Ryba("Zlotko")
# print(zlota_rybka.przedstaw_sie())

rekin_bialorybi = Rekin( "Rekin", "bialy")

print(rekin_bialorybi.przedstaw_sie())

#Jezeli mamy drzewko takie to algorytm zachowuje sie w taki sposob, ze najpierw metode <przedstaw sie sprawdzamy w klasie <rekin>
# Tam tego nie znajdujemy, wiec sprawdzana jest klas <ryba>. Tam ta metoda nie zostala znaleziona. Wiec sprwadzana jest
# klasa <plywajace> i tak juz ta metoda jest odnaleziona. Zawsze ten algorytm najpierw sprawdza klasy po lewej stronie.

# 3 Plywajace
#        \
#        2 Ryba          3  Zwierze
#            \                /
#                 1 Rekin


# Czyli kolejnos sprawdzania klas dziedziczenia przez algorytm

# 4 PrababciaM    5 PradziadekM
#         \             /
#            3  BabciaM         6 DziadekT         8 BabciaT    9 DziadekT
#                 \                 /                   \            /
#                      2  Mama                             7  Tata
#                            \                                 /
#                                         1 Syn

