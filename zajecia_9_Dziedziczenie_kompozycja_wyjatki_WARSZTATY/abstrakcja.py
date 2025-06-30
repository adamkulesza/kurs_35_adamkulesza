# Przywolajmy na chwile nasz program z figurami geometrycznymi

from abc import ABC, abstractmethod

# class FiguraGeometryczna:
#     def oblicz_pole(self):
#         return None
#
#     def oblicz_obwod(self):
#         return None
#
# # W momencie kiedy pisalismy sobie wiele klas poszczegolnych figur typu
#
# class Trojkat(FiguraGeometryczna):
#     def __innit__(self, podstawa, wysokosc):
#         self.podstawa = podstawa
#         self.wysokosc = wysokosc
#
#     def oblicz_pole(self):
#         return 0,5 * self.podstawa * self.wysokosc

#   Moglismy napisac funkcje <oblicz_pole> i <oblicz_obwod> wewnatrz klasy <Trojkat>, bo ta klasa dziedziczy po klasie
# <FiguraGeometryczna> i dzieki temu program nam zadziala, bo jako, ze klasa Trojkat nie posiada funkcji <oblicz_obwod>
# wiec dziedziczy ta funkcje z klasy <FiguraGeometryczna>.
# Nie jest to cos co do konca bysmy chcieli.
#   My majac klase <FigutaGeometryczna>, ktora defacto nie powinna byc jakas taka, faktycznie rzecza. Bo majac na mysli
# figura geometryczna kazdy z nas mysli trojkat albo kolo, albo kwadrat. Majac w glowie figura geometryczna mamy w glowie
# caly zboir figur, natomiast sama w sobie figura geometryczna nie jest rzecza ( nie jest tak jakby scisle zdefiniowana).
# Figura geometryczna to nie jest rzecz. Natomiast mamy zbior figur geometrycznych ktore juz faktycznie mozemy nazwac, i
# ktore maja swoje specyficzne rzeczy.
#   Do takich rozwiazan, w ktorych my defacto nie mamy takiego bytu, bo taki byt nie istnieje, ale wiemy ze istnieje iles
# tam bytow, ktore sa w tej grupie, sluza nam:
#
#                                   Klasy abstrakcyjne
#
# Bo Figura geometryczna jako samo w sobie slowo dla nas jako dla ludzi jest defacto abstrakcja.
# My to sobie nazwalismy. Stworzylismy sobie jakas grupe. Powiedzielismy ze to jest figura geometryczna, natomiast to
# jest defacto trojkat.
# My mozemy sprawic zeby faktycznie ta figura geometryczna byla abstrakcja i co wiecej my wiedzac, ze ta figura
# geometryczna jest abstrakcja, mozemy na kazdej figurze, ktora jest w tym zbiorze, czyli de facto trojkacie, kole,
# rombie, kwadracuie ect mozemy wymusic to, zeby one mialy zaimplementowane jakies rzeczy, zeby faktycznie ta figura
# geometryczna byly.
#   Kazda figura geometryczna jezeli my sobie o nich pomyslimy musi spelniac jakies dwa warunki:
#   1. musi miec jakis swoj obwod
#   2. musi miec swoje jakies pole
#
#
#   I teraz mozemy zaimplementowac sobie FigureGeometryczna jako klase abstrakcyjna
#   Zeby zdefiniowac ta klase jako klase abstrakcyjna musimy zaimportowac na gorze programu  z modulu <abc> dwie rzeczy:
#   1. ABC, ktore bedzie nam mowilo ze to jest klasa abstrakcyjna
#   2. abstractmethod
#   w taki sposob <from abc import ABC, abstractmethod>
#   I teraz zeby ta klase abstarkcyjna stworzyc musimy zrobic pierwsza rzecz
#   Pierwsza rzecz: definicja klasy musi dziedziczyc po klasie abstrakcyjnej. Piszemy <class FiguraGeometryczna(ABC):>
#   Mozemy teraz te nasze dwie metody <oblicz_pole> i <oblicz_obwod> udekorowac do bycie metodami abstrakcyjnymi poprzez
#   dodanie @abstractmethod
#   My w tym momencie zebysmy mieli obiekty typu Trojkat to piszemy ponizej <trojkat = Trojkat(podstawa=1, wysokosc=2)>

# class FiguraGeometryczna(ABC):
#
#     @abstractmethod
#     def oblicz_pole(self):
#         return None
#
#     @abstractmethod
#     def oblicz_obwod(self):
#         return None
#
# class Trojkat(FiguraGeometryczna):
#     def __init__(self, podstawa, wysokosc):
#         self.podstawa = podstawa
#         self.wysokosc = wysokosc
#
#     def oblicz_pole(self):
#         return 0,5 * self.podstawa * self.wysokosc
#
# trojkat = Trojkat(podstawa=1, wysokosc=2)

# I w tym momencie wyskakuje blad
# <TypeError: Can't instantiate abstract class Trojkat without an implementation for abstract method 'oblicz_obwod'>
#
# Zdefiniowanie takich klas abstrakcyjnych bedzie wymagalo na kazdym dziecku, ktore bedzie chcialo dziedziczyc po tej
# naszej abstrakcyjnej klasie, bedzie wymagalo zdefiniowania i napisania faktycznego kodu do nadpisania tych obydwu metod.
# dopiero w tym momencie kiedy dopiszemy <oblicz_obwod> ten nasz trojkat bedzie nam dzialal.

# class FiguraGeometryczna(ABC):
#
#     @abstractmethod
#     def oblicz_pole(self):
#         return None
#
#     @abstractmethod
#     def oblicz_obwod(self):
#         return None
#
# class Trojkat(FiguraGeometryczna):
#     def __init__(self, podstawa, wysokosc):
#         self.podstawa = podstawa
#         self.wysokosc = wysokosc
#
#     def oblicz_pole(self):
#         return 0,5 * self.podstawa * self.wysokosc
#
#     def oblicz_obwod(self):
#         return self.podstawa + 2 * ((self.podstawa / 2) ** 2 + self.wysokosc ** 2) ** 0.5
#
# trojkat = Trojkat(podstawa=1, wysokosc=2)

# Teraz ta klasa abstrakcyjna wymusza na wszystkich swoich dzieciach pewne zachowania. Wymusza na nich w tym momencie to,
# ze one beda musialy zaimplementowac ta metode.
#
#
#
#   Kiedy to jest przydatne??
#   Wyobrazcie sobie ze macie jakis sklep e-comersowy i mamy klase <Payment> i w naszym sklepie mamy rozne rodzaje
# platnosci. Czy to jakies przelewy24, czy to jakis blik, czy karta, czy przelew tradycyjny, czy co kolwek innego.
# Cala nasza logika sklepu skupia sie na tym, ze my musimy wykonac metode <process_payment> z tej naszej platnosci.
# Majac to napisane w ten sposob:

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

# teraz bardzo prosto bedziemy mogli sobie zrobic tak

class BlikPayment(Payment):
    def process_payment(self, amount: float) -> str:
        return f"processing BLIK payment of {amount} PLN"

class CardPayment(Payment):
    def process_payment(self, amount: float) -> str:
        return f"Processing card payment of {amount} PLN"

class PayPallPayment(Payment):
    def process_payment(self, amount: float) -> str:
        return f"Processing payPall payment of {amount} PLN"

# bedziemy mogli dodawac te nasze platnosci tylko poprzez rozszerzanie tych naszych funkcjonaknosci w tym naszym systemie,
# a nie poprzez modyfikacje kodow w stu roznych miejscach. Po stronie korowej logiki tego sklepu, tej naszej biznesowej
# my po prostu musimy wykonac metode <process_payment> a to jak ta metode <process_payment> beda wykonywac poszczegolne
# klasy to bedzie zalezalo od tych klas. My tylko i wylacznie bedziemy oczekiwali ze ten <prosess_payment> nam faktycznie
# przejdze, a to jak ta metoda bedzie to robila, czy to bedzie np. kod BLIK z 6 cyframi, czy to bedzie karta, czy to
# bedzie przekewy24 to juz totalnie nie powinno nas interesowac, to znaczy nie interesuje tej korowej czesci logiki
# naszego sklepu poniewaz wlasnie za to bedzie odpowiadalo to wszystko co powyzej npisalismy.