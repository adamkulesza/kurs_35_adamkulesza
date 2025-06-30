# Pracujemy w salonie samochodowym i mamy <Samochod>
# W salonie mozemy konfigurowac te nasze smochody i robimy sobie klase <Silnik> ktora jest klasa abstrakcyjna

from abc import ABC, abstractmethod

# class Silnik:
#     def __init__(self, moc):
#         self.moc = moc
#
#     def __str__(self):
#         return f"Silnik o mocy {self.moc} KM"
#
#     def uruchom_silnik(self):
#         return "Silnik uruchomiony."
#
#
#
# class Samochod:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
#
#     def __str__(self):
#         return f"{self.marka} {self.model}"

# Mamy dwie klasy - kalsa <Silnik> i klasa <Samochod>
# Co mozemy zrobic, to w klasie Samochod mozemy przetestowac brzmienie

class Silnik:
    def __init__(self, moc):
        self.moc = moc

    def __str__(self):
        return f"Silnik o mocy {self.moc} KM"

    def uruchom_silnik(self):
        return "Silnik uruchomiony."

    def podnies_obroty(self):
        return "Obroty silnika podniesione."
class Felga:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar

    def __str__(self):
        return f"Felga o rozmiarze {self.rozmiar} cali"


class Samochod:
    def __init__(self, marka, model, silnik: Silnik, felga:Felga = None):
        self.marka = marka
        self.model = model
        self.silnik = silnik
        self.felga = felga

    def __str__(self):
        return f"{self.marka} {self.model}"

    def przetestuj_brzmienie_silnika(self):
        print(self.silnik.uruchom_silnik())
        print(self.silnik.podnies_obroty())

# Na co nam to pozwala  - pozwala nam to na to, ze mozemy teraz sprecyzowac samochod, ktory bedzie Toyoya Corolla z moca silnika 150KM:

samochod = Samochod("Toyota", "Corolla", Silnik(150))
# mozemy tez miec samochod:
samochod_2 = Samochod("ford", "Focus", Silnik(180))

# co defakto tutaj zrobilismy??
#Uzylismy sobie:
#
#                                                       kompozycji
#
#   Na czym ta kompozycja polega?
#   My jako parametr do naszej funkcji inicjalizujacej przekazujemy sobie jakis inny obiekt <silnik: Silnik> przekazujemy
# i bedziemy trzymali jako nasz wewnetrzny parametr <self.silnik = silnik>. Nasze pole defacto tego obiektu.
# Trzymajac ten parametr jako pole, korzystajac z naszej kompozycji my bedziemy mogli w naszych metodach uruchamiac metode
# tego naszego silnika, czyli tego naszego pola <self.silnik.uruchom_silnik()>, ktore sobie zdefiniowalismy

# teraz jak sobie napiszemy:
samochod.przetestuj_brzmienie_silnika()
samochod_2.przetestuj_brzmienie_silnika()

# W tym momencie skorzystalismy z kompozycji - stworzylismy sobie obiekt, ktory sklada sie z innych obiektow

# Wyobrazcie sobie, ze nnp. oprocz tego silnika mamy klase <Felgi> - dodajemy powyzek ta klase
# i teraz mozemy napisac

felga_shimano = Felga(18)
felga_audi = Felga(19)
felga_continental = Felga(20)

samochod = Samochod("Toyota", "Corolla", Silnik(150), felga_shimano)

# Dzieki tej kompozycji jestesmy w stanie tworzyc obiekt z roznych naszych rzeczy. Budujemy z klockow. Dzieki naszemu
# konfiguratorowi nasz samochod mogłby byc za kazdym razem zbudowany z innych komponentow