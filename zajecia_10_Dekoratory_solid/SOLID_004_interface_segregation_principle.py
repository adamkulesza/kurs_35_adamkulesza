# I - interface segregation principle

# My w pythonie interfacow nie mamy - w innych jezykach programowania, no JAVA to tam interface sa

# Interfejsy to sa zbiory metod, ktore trzeba bedzie zaimplementowac, albo juz sa zaimplementowane, ktore pomprostu
# mozemy sobie wziac, z ktorych mozemy sobie te metody wywolywac.

# Natomiast co mowi nam Interface segregation??
# Ta zasada jest mocno powiazana z zasada liskov substytution. Poniewaz ona muwi tez nam o tym, ze nie powinnismy jako
# te klasy nadzredne zmuszac tych naszych klas podrzednych do implementowania jakichs metod.

# O co chodzi??

from abc import ABC, abstractmethod

# class Zwierze(ABC):
#     @abstractmethod
#     def plywaj(self):
#         pass
#
#     @abstractmethod
#     def lataj(self):
#         pass
#
#     @abstractmethod
#     def biegaj(self):
#         pass
#
# class Kangur(Zwierze):
#     def plywaj(self):
#         raise NotImplementedError("Kangur nie plywa!")
#
#     def lataj(self):
#         raise NotImplementedError("Kangur nie lata!")
#
#     def biegaj(self):
#         return "Kangur skacze!"
#
# class Ryba(Zwierze):
#     def plywaj(self):
#         return "Ryba plywa!"
#
#     def lataj(self):
#         raise NotImplementedError("Ryba nie lata!")
#
#     def biegaj(self):
#         raise NotImplementedError("Ryba nie biega!")


# my z punktu widzenia interfejsu mamy ten interfejs troszeczke za duzy.

# !!!!!!!!!!!!!!!!!U nas w pythonie interfejs to jest tylko i wylacznie klasa abstrakcyjna!!!!!!!!!!!!!!!!!

# Wiec co musieli bysmy zrobic aby to poskracac?? Znowu musieli bysmy ten nasz interfejs podzielic na troszke mniejsze
# interfejsy



# class Zwierze(ABC):
#     @abstractmethod
#     def rozmnoz_sie(self):
#         pass
#
# # nastepnie robimy sobie klase <LatajaceZwierze(Zwierze)> ktore dziedziczy po <Zwierze>
# class LatajaceZwierze(Zwierze):
#     @abstractmethod
#     def lataj(self):
#         pass
#
# # nastepnie robimy sobie klase <PlywajaceZwierze(Zwierze)> ktore dziedziczy po <Zwierze>
# class PlywajaceZwierze(Zwierze):
#     @abstractmethod
#     def plywaj(self):
#         pass
#
# # nastepnie robimy sobie klase <BiegajaceZwierze(Zwierze)> ktore dziedziczy po <Zwierze>
# class BiegajaceZwierze(Zwierze):
#     @abstractmethod
#     def biegaj(self):
#         pass
#
# # Co dzieki temu mamy??
# # kiedy napiszemy znowu klase <Kangur>
#
# class Kangur(BiegajaceZwierze):
#     def rozmnoz_sie(self):
#         return "Kangur rozmnaza sie!"
#
#     def biegaj(self):
#         return "Kangur skacze!"
#
#
# class Ryba(PlywajaceZwierze):
#     def rozmnoz_sie(self):
#         return "Ryba sklada jajka"
#
#     def plywaj(self):
#         return "Ryba plywa!"
#
# class Orzel(LatajaceZwierze):
#     def rozmnoz_sie(self):
#         return "Orzel sklada jaja!"
#
#     def lataj(self):
#         return "orzel lata wysoko!"



# dzieki temu mamy to podzielone w ten sposob na mniejsze czesci




# Co jeszcze innego mozemy miec w tym Interface segregation?
# mozemy miec to, ze nie mamy tego dokladnie podzielonego tylko mamy na przyklad:

class Plywajace(ABC):
    @abstractmethod
    def plywaj(self):
        pass

class Latajace(ABC):
    @abstractmethod
    def lataj(self):
        pass

class Biegajace(ABC):
    @abstractmethod
    def biegaj(self):
        pass

# dodajemy zwierze, ktore plywa i beiga

class Czlowiek(Biegajace, Plywajace):
    def biegaj(self):
        return "Czlowiek biegnie!"

    def plywaj(self):
        return "Czlowiek plywa!"

class Kaczka(Plywajace, Latajace):
    def plywaj(self):
        return "Kaczka plywa!"

    def lataj(self):
        return "Kaczka lata!"

# dzieki Interface segregation - mozemy zrobic zeby te interfacy byly jak najmniejsze i beda po sobie dziedziczyly, ale
# my bedziemy mogli je laczyc, dzieki temu ze w pythonie mamy multidziedziczenie. Czyli mozemy dziedziczyc wiecej niz po
# jednej klasie.