# O - open, close principle -
# Na potrzeby tej zasady zalozmy sobie ze mamy klase - jakis sklep:

# class DiscountCalculator:
#     def calculate_discount(self, price: float, discount_type: str) -> float:
#         if discount_type == "percent":
#             return price * 0.1
#         elif discount_type == "fixed":
#             return 10.0
#         elif discount_type == "vip":
#             return price * 0.2
#         elif discount_type == "normal":
#             return 0.0

#   Co jest wazne. Zwroc uwage co dzieje sie tutaj w tym naszym kodzie. my bedac takimi programistami, naszego sklepu
# e-comersowego, pracujac nad naszym kodem bedziemy musieli za kazdym razem edytowac ta sama funkcje.
# <calculate_discount> bedzie zmieniac swoja forme w zaleznosciod tego pewnie w zaleznosci jakie promocje w naszym
# sklepie beda ( vip, normal, super, hiper, przyjaciele itd....). Tych elif bedzie bardzo duzo i trzeba je bedzie
# przekazywac.
#   Wiec zamias robic to w taki sposob i zamiast modyfikowac sobie jedna funkcje i pisac tysiace jakichs tam wartosci, to
# mozemy zrobic:
# - zaimportowc abc
# - tworzymy klase <DiscountStrategy(ABC)> i dodajemy metode abstarkcyjna

from abc import ABC, abstractmethod

class DiscountCalculator:
    def calculate_discount(self, price: float, discount_type: str) -> float:
        if discount_type == "percent":
            return price * 0.1
        elif discount_type == "fixed":
            return 10.0
        elif discount_type == "vip":
            return price * 0.2
        elif discount_type == "normal":
            return 0.0

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price: float) -> float:
        pass

# nastepnie dopisujemy klase <VipDiscount(discountStrategy):

class VipDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.2

# nastepnie dopisujemy <FixedDiscount(DiscountStrategy)> ktora dziedziczy po <DiscountStrategy>

class FixedDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return 10.0

# dpoisujemy <PercentDiscount(DiscountStrategy)> ktora dziedziczy po <DiscountStrategy>
class PercentDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.1

# teraz robimy sobie

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

# i teraz <calculate_discount> ma tylko dwie linijki
    def calculate_discount(self, price: float) -> float:
        return self.strategy.calculate_discount(price)

# Dzieki temu ten nasz <discount_calculator> nie bedzie rozszerzany w nieskonczonosc. To nie bedzie tak ze zaraz
# przyjdzie szef i bedziemy musieli zmienac funkcje caly czas. Wielkim plusem bedzie to ze bedziemy juz tylko dodawali
# klasy dla poszczegolnych promocji. A to jaka promocja zostanie wybrana , to juz nas nie interesuje bo do tej klasy
# <DiscountCalculator> bedziemy mogli podawac co bedziemy chcieli, bo to ona odpowiada za aktualnie uzywane promocje. To
# bedzie za nas to wszystko robilo.
# To jest zasada
#
#                               Open, close
#
# Mowi nam ona, ze ten nasz kod powinien byc otwarty na rozszerzanie. Dzieki tej klasie abstrakcyjnej <DiscountStartegy>
# bedziemy mogli powiekszac nasz kod o kolejne dzieci ktore tutaj mamy.
# A zamkniety powinien byc na modyfikacje. Nie powinnismy pisac tego kodu w taki sposob ze zmieniamy jakis wartosci
# nieskonczenie wiele razy, lecz tylko po prostu bedziemy dodawali i rozszerzali to wszystkp.
# Te nasze programy powinny wygladac jak budowle z klockow.