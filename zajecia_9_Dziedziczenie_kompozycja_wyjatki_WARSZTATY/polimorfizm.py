# Polimorfizm zasada ktora dziala przy dziedziczeniu

import math

# Zalozmy ze mamy klase:

# class FiguraGeometryczna:
#     def oblicz_pole(self):
#         return None
#
#     def oblicz_obwod(self):
#         return None
#
# def oblicz_obwod_zaawansowanej_figury():
#     pass
#
# def oblicz_pole_zaawansowanej_figury():
#     pass

# w tym naszym prostym zadaniu bedziemy sobie obliczali zlozona figure.
# Jak to mozemy zrobic??



# Mozemy to zrobic tak.
class FiguraGeometryczna:
    def oblicz_pole(self):
        return None

    def oblicz_obwod(self):
        return None

# Dopisujemy do funkcji <oblicz_obwod_zaawansowanej_figury()> nastepujaca rzecz:
# <obwod_figury = 0>
# i w nawiasie tej funkcji dopisujemy <figury: FiguraGeometryczna>
# a nastepnie do tej funkcji dopisujemy na dole:
# for figura in figury:
#    obwod_figury += figura.oblicz_obwod()
# robimy dokladnie to samo w funkcju <oblicz_pole_zaawansowanej_figury()>

def oblicz_obwod_zaawansowanej_figury(figury: list[FiguraGeometryczna]):
    obwod_figury = 0
    for figura in figury:
        obwod_figury += figura.oblicz_obwod()
    return obwod_figury

def oblicz_pole_zaawansowanej_figury(figury: list[FiguraGeometryczna]):
    pole_figury = 0
    for figura in figury:
        pole_figury += figura.oblicz_pole()
    return pole_figury

# Mamy te nasze dwie metody i mamy klase FiguraGeometryczna. Ta klasa ma dwie metody. Metoda <oblicz_obwod> i
# <oblicz_pole> (znajduja sie bezposrednio w definicji klasy) - te dwie metody nam nic nie zwracaja - zwracaja nam None.
# Co teraz mozemy zrobic?? Mozemy sobie stworzyc inne figury ktore takimi figurami juz beda. Piszemy:

# Trojkat
class Trojkat(FiguraGeometryczna):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return 0.5 * self.podstawa * self.wysokosc

    def oblicz_obwod(self):
        return self.podstawa + 2 * ((self.podstawa / 2) ** 2 + self.wysokosc ** 2) ** 0.5

# Kwadrat
class Kwadrat(FiguraGeometryczna):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok ** 2

    def oblicz_obwod(self):
        return self.bok * 4

# Okrag
class Okrag(FiguraGeometryczna):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return math.pi * self.promien ** 2  # math.pi oznacza wartosc PI = 3.14 - wstawilismy to tu po wczesniejszym
                                            # zaimportowaniu na gorze modulu matematycznego <import math>

    def oblicz_obwod(self):
        return 2 * math.pi * self.promien   # math.pi oznacza wartosc PI = 3.14 - wstawilismy to tu po wczesniejszym
                                            # zaimportowaniu na gorze modulu matematycznego <import math

# Jezeli uzywamy wartosci PI to mozemy zaimportowac modul matematyczny na samym poczatku piszac <import math> i
# zamiast 3.14 napisac <math.pi>

# Romb
class Romb(FiguraGeometryczna):
    def __init__(self, bok, wysokosc):
        self.wysokosc = wysokosc
        self.bok = bok

    def oblicz_pole(self):
        return self.bok * self.wysokosc

    def oblicz_obwod(self):
        return 4 * self.bok

# Wszystkie te figury maja metode <oblicz_pole> i <oblicz_obwod> zaimplementowane u siebie
# Mamy tez <oblicz_obwod_zaawansowanej_figury> gdzie przekazujemy w nawiasie parametr <figury> ktory bedzie lista <FiguryGeometryczne>
# i spodziewamy sie ze ta funkcja bedzie nam dzialala.

# Wpisujac teraz print :
print(oblicz_obwod_zaawansowanej_figury([Trojkat(3, 4), Kwadrat(5), Okrag(2), Romb(3, 4)]))
# teoretycznie powinnismy dostac blad - Dlaczego?????
# Dlatego , że mamy figure, ktora powinna byc figura geometryczna ( zerknij do <oblicz_obwod_zaawansowanej_figury> tam
# jest napisane w nawiasie <figury: list[FiguraGeometryczna]> i to swiadczy o tym ze ma to byc figura geometryczna) - nie jest
# to Trojkar, nie jest to Kwadrat, nie jest to Okrag - to jest nasz rodzic.

# Teraz jezeli my to uruchomimy to okazuje sie ze obwod tej figury zostal obliczony poprawnie. Dlaczego tak sie stalo??

# Oczekiwalismy rodzica czyli FiguryGeometrycznej a podajac dziecko (rozne figury w nawiasie) nie dostalismy zadnego bledu,
# na dodatek ten program nam dziala i zachowuje sie nam tak jak powinien. Za taki mechanizm odpowiada Polimorfizm

#                                           Polimorfizm

# Polimorfizm, ktory mowi nam o tym, ze taki obiekt klasy moze przyjmowac wiele form.
# O co w tym chodzi??
# Chodzi w tym o to ze jezeli my jako dzieci spelniamy wszystkie nasze zamierzone warunki to my mozemy zachowywac sie
# jako nasi rodzice.
# wiec jak napiszemy
print(oblicz_pole_zaawansowanej_figury([Trojkat(3, 4), Kwadrat(5), Okrag(2), Romb(3, 4)]))
# to otrzymamy poprawne pole.