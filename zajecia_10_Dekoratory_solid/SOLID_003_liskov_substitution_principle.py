# liskov


# Nasze dzieci, majac te programowanie obiektowe pamietajcie mamy dziedziczenie mamy rodzicow oraz dzieci.
# W tej zasadzie chodzi o to ze jezeli my bedziemy podmieniali dzieci na naszych rodzicow, czyli jest to cos co defakto
# robilismy w polimorfizmie, w polimorfizmie robilismy to tak ze mielismy te nasze figury geometryczne - przekazywalismy,
# ze chcemy miec figure geometryczna, na tomiast nie wiedzielismy do konca jaka to bedzie figura. Moglismy podac
# cokolwiek innego, czy to kwadrat, czy to trojkat czy cokolwiek. On implementowal te zasady ktore miał.

# liskov substitution:
# mowi o czyms bardzo podobnym poniewaz on nam mowi o tym, ze te obiekty klas potomnych one powinny byc wymienialne w
# miejsce klas bazowych bez zmiany poprawnosci dzialania programu. Czyli defakto te dzieci moga w 100% symulowac nam
# rodzicow.

from abc import ABC, abstractmethod

class Ptak:
    def lataj(self):
        return "Lece!"

class Golab(Ptak):
    def lataj(self):
        return "Gleboko latam."

class Sikorka(Ptak):
    def lataj(self):
        return "Szybko latam!"

class Strus(Ptak):
    def lataj(self):
        raise NotImplementedError("Strus nie lata")

# Mamy teraz zlamanie zasady liskov substitution - strus mimo ze jest ptakiem to nie lata.
# Wiec co mozemy zrobic aby ta zasade spelnic??
# importujemy sobie klasy abstarkcyjne
# piszemy sobie klase <Ptak(ABC)>

class Ptak(ABC):
    @abstractmethod
    # zamiqast <lataj> mamy <daj_glos>
    def daj_glos(self):
        pass

# oprocz tej klasy <Ptak> dajemy sobie klase <Latajacy>, ktory ptakiem tez jest

class LatajacyPtak(Ptak):
    @abstractmethod
    def lataj(self):
        pass

# dajemy jeszcze:

class NielatajacyPtak(Ptak):
    @abstractmethod
    def biegaj(self):
        pass

# I teraz dzieki temu, ze mamy podzielone na takie 3 klasy abstrakcyjne, 3 interfejsy, mozemy napisac ze kazdy z tych
# naszych ptakow jest ptakiem

class Golab(LatajacyPtak):
    def daj_glos(self):
        return "Gleboko glosuje!"

    def lataj(self):
        return "Gleboko laytam!"

# sikorka tez ptakiem bedzie

class Sikorka(LatajacyPtak):
    def daj_glos(self):
        return "Szybko glosuje!"

    def lataj(self):
        return "Szybko latam!"

# natomiast strus ptakiem tez jest (pamietajmy ze <NielatajacyPtak> dziedziczy po <Ptak>
# ale <LatajacyPtak> juz nie jest, wiec nie bedzie mial metody <lataj> tylko bedzie mial metode <biegaj>

class Strus(NielatajacyPtak):
    def daj_glos(self):
        return "Strus glosuje"

    def biegaj(self):
        return "Biegam szybko!"

# o to w tym chodzi, zeby te nasze dzieci, one byly w stanie implementowac, poprawnie te wszystkie metody naszych
# rodzicow, zeby one mogly byc przedstawiane jako rodzice. zebysmy my z zewnatrz ie widzieli zbytnio roznicy.