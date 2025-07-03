#   Na poczet nauki dekoratorow przyjmijmy, ze musimy stworzyc jakis system zarzadzajacy nasza firma, w ktorym bedziemy
# mieli mozliwosc logowania godzin przez uzytkownikow, bedziemy mieli mozliwosc dodawania sobie jakichs urlopow przez
# uzytkownikow, bedziemy mieli mozliwosc wystawiania faktur, ksiegowosci itd.
# Zaluzmy sobie ze mamy tam swoich uzytkownikow.

uzytkownicy = [
    {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 30,
        "rola_w_firmie": "Programista"
    },
    {
        "imie": "Anna",
        "nazwisko": "Nowak",
        "wiek": 25,
        "rola_w_firmie": "Tester"
    },
    {
        "imie": "Piotr",
        "nazwisko": "Zielinski",
        "wiek": 35,
        "rola_w_firmie": "Menadzer"
    }
]

# Mamy 3 uzytkownikow - mozemy miec nieskonczenie wiele


# class Firma:
#     def __init__(self, uzytkownicy):
#         self.uzytkownicy = uzytkownicy
#         self.urlopy = [] # pusta lista gdzie uzytkownicy beda dodawac sobie urlopy
#         self.godziny = [] # pusta lista gdzie pracownicy beda wpisywali swoje godziny pracy
#
# # Do naszej firmy dodajemy opcje <dodaj urlop>
#
#     def dodaj_urlop(self, imie, nazwisko, data_rozpoczecia, data_zakonczenia):
#         for uzytkownik in self.uzytkownicy:
#             if uzytkownik['imie'] == imie and uzytkownik['nazwisko'] == nazwisko:
#                 urlop = {
#                     "imie": imie,
#                     "nazwisko": nazwisko,
#                     "data_rozpoczecia": data_rozpoczecia,
#                     "data_zakonczenia": data_zakonczenia
#                 }
#                 self.urlopy.append(urlop)
#                 return f"Urlop dla {imie} {nazwisko} zostal dodany."
#         return "Uzytkownik nie znaleziony"
#
#     def dodaj_godziny(self, imie, nazwisko, godziny):
#         for uzytkownik in self.uzytkownicy:
#             if uzytkownik['imie'] == imie and uzytkownik['nazwisko'] == nazwisko:
#                 godziny_record = {
#                     "imie": imie,
#                     "nazwisko": nazwisko,
#                     "godziny": godziny
#                 }
#                 self.godziny.append(godziny_record)
#                 return f"Godziny dla {imie} {nazwisko} zostaly dodane."
#         return "Uzytkownika nie znaleziono."
#
#     def wyplac_pieniadze(self, imie, nazwisko, kwota):
#         for uzytkownik in self.uzytkownicy:
#             if uzytkownik['imie'] == imie and uzytkownik['nazwisko'] == nazwisko:
#                 return f'Wyplacono {kwota} zl dla {imie} {nazwisko}'
#
# firma = Firma(uzytkownicy)


#   Co my tutaj w tych naszych metodach zarzadzajacych mamy?
#   Mianowicie mamy w tych naszych metodach pewien kod, ktory sie powiela. Za kazdym razem iterujemy sobie po tych
# naszych uzytkownikach i sprawdzamy czy ten uzytkownik, ktorego wybralismy, bedzie tym naszym uzytkownikiem. Jezeli on
# tym naszym uzytkownikiem bedzie to dodamy te nasze okreslone rzeczy. Jest to takie cos co musielibysmy dodawac dla
# kazdej metory, ktora bysmy tutaj mieli. Poniewaz w tym naszym systemie zarzadzania firma kluczowi sa ludzie, ktorymi
# zarzadzamy. Wiec my za kazdym razem musielibysmy prosic o tego naszego urzytkownika i musielibysmy sprawdzac kim on w
# ogole jest. Co to za uzytkownik, jakie nasze dane wprowadzil w tym naszym systemie.
#   Co jest najwazniejsze? Najwazniejsze jest to z punktu widzenia programistycznego, z punktu widzenia nas, ze my sie
# tutaj powtarzamy. A my jako programisci jestesmy leniwi i za kazdym razem chcemy tak zrobic zeby nasz kod byl
# najktutszy i zeby sie nie narobic. Chcielibysmy zeby tych powtorzen bylo jak najmniej.
#   Co mozemy zrobic??
#   To mozemy np dodac funkcje


# class Firma:
#     def __init__(self, uzytkownicy):
#         self.uzytkownicy = uzytkownicy
#         self.urlopy = [] # pusta lista gdzie uzytkownicy beda dodawac sobie urlopy
#         self.godziny = [] # pusta lista gdzie pracownicy beda wpisywali swoje godziny pracy
#
# # Dodajemy funkcje.
#
#     def zaloguj_uzytkownika(self, imie, nazwisko):
#         for uzytkownik in self.uzytkownicy:
#             if uzytkownik["imie"] == imie and uzytkownik["nazwisko"] == nazwisko:
#                 return uzytkownik
#         return None
#
# # Zamiast robic to w ten sposob ze mamy caly czas ta pentle for, mozemy zrobic to w ten sposob. Zmianiamy ponizsze
# # funkcje w taki sposob.
#
#     def dodaj_urlop(self, imie, nazwisko, data_rozpoczecia, data_zakonczenia):
#         uzytkownik = self.zaloguj_uzytkownika(imie, nazwisko)
#         if not uzytkownik:
#             return "Uzytkownik nie znaleziony."
#         urlop = {
#             "imie": imie,
#             "nazwisko": nazwisko,
#             "data_rozpoczecia": data_rozpoczecia,
#             "data_zakonczenia": data_zakonczenia
#         }
#         self.urlopy.append(urlop)
#         return f"Urlop dla {imie} {nazwisko} zostal dodany."
#
#     def dodaj_godziny(self, imie, nazwisko, godziny):
#         uzytkownik = self.zaloguj_uzytkownika(imie, nazwisko)
#         if not uzytkownik:
#             return "Uzytkownik nie znaleziony."
#         godziny_record = {
#             "imie": imie,
#             "nazwisko": nazwisko,
#             "godziny": godziny
#         }
#         self.godziny.append(godziny_record)
#         return f"Godziny dla {imie} {nazwisko} zostaly dodane."
#
#
#   def wyplac_pieniadze(self, imie, nazwisko, kwota):
#       for uzytkownik in self.uzytkownnicy:
#           if uzytkownik["imie"] == imie and uzytkownik["nazwisko"] == nazwisko
#               return f"Wyplacono {kwota} zl dla {imie} {nazwisko}"
#       return "Uzytkownik nie znaleziony."
#
# firma = Firma(uzytkownicy)

# Mielismy jakis nasz kod, ktory powtarzal soe wielokrotnie. Zamiast pisac go nieskonczenie wiele razy, wykonalismy go
# tylko i wylacznie jednorazowo. Bedziemy mieli przypisanie do jakiejs funkcji i bedziemy to sobie wywolywali:
#
#        uzytkownik = self.zaloguj_uzytkownika(imie, nazwisko)
#         if not uzytkownik:
#             return "Uzytkownik nie znaleziony."
#

# Mamy klase <Firma>, i mamy wszystkie definicje, kture sluza do obslugi tej firmy i mamy tego <zaloguj_uzytkownika>
# To zalogowanie sie uzytkownika i sprawdzenie czy my faktycznie takiego uzytkownika mamy jest dla nas kluczowe w tym
# naszym systemie. Jezeli ne bedzie takiego uzytkownika i uzytkownik sie nie zaloguje. Nie bedziemy wiedzielei kim on
# jest. To jako kolwiek operacja powinna byc zablokowana z naszej strony. To jest cos co jest dla nas kluczowe.

# To co my tu zrobilismy to defacto wywolalismy funkcje. natomiast na takie rozwazania, na takie sytuacje w ktorych my
# musimy sprawdzic najpierw czy cos zostalo zrobione, albo musimy dodac jakas logike do pewnych funkcji ( bo teraz
# <dodaj_urlop> to nie jest tylko i wylacznie dodawanie urlopu, ale <dodaj_urlop> ma w sobie tez sprawdzenie, czy
# uzytkownik jest zalogowany) wiec taka struktura, ktora tutaj mamy mozna zastosowac z pomoca naszego
#
#                                                   dekoratora
#
#   Czym takie dekoratory sa?
# Dekoratory to jest taki nasz SyntaxSugar, ktory robi bardzo podobne rzeczy tak jak w tej linijce
#               <uzytkownik = self.zaloguj_uzytkownika(imie, nazwisko)>
# Natomiast te rzeczy nie beda dzialy sie wewnatrz naszej funkcji tylko one beda opakowywaly nasza funkcje. bedzie to
# troszeczke czyms innym niz to co mamy po wyzej.


#   Jak takie dekoratory uzywac i jak takie dekoratory swoje wlasne pisac??
# Tydzien temu poznalismy juz czesc dekoratorow. Mielismy cos takiego jak class method, static method
# Metody statyczne sa to takie metody, ktore nie zmienialy stanu ani klasy ani obiektu. To bylu metody, ktore robily
# jakies operacje, natomiast one w zaden sposob nie pobieraly, ani nie wplywaly na stan tych naszych rzeczy

# @staticmethod
# def przywitaj_sie():
#     return "Witaj w systemie zarzadzania firma"

# ta metoda statyczna, ktora mamy powyzej jest udekorowana <@staticmethod> - to jest nasz wbudowany dekorator w pythona.
# Dekorator ten robi z funkcji <przywitaj_sie> zamiast zwyklej metody obiektu, robi metode statyczna. Wykonanie tego
# operatora i udekorowanie jakiegos obiektu nastepuje w ten sposob. Ta <@> ze sstaticmethod udekorowala ta nasza funkcje.


#   Mamy klase <Firma>, mamy urlopy i mamy godziny.
#   Zalozylismy sobie, ze nie chielibysmy zeby sprawdzanie tych uzytkownikow bylo wewnatrz tej funkcji. Chcielibysmy
# zeby ta logika (trzy linijki kodu:
#
#         uzytkownik = self.zaloguj_uzytkownika(imie, nazwisko)
#         if not uzytkownik:
#             return "Uzytkownik nie znaleziony."
#
# , ktora tutaj mamy, zeby byla na zewnatrz i byla opakowaniem tej naszej funkcji, a nie zeby byla funkcja. Chcemy dac
# ten dekorator.
# Jak takie dekoratory piszemy?

#   Dekoratory bedziemy zawsze definiowali jako funkcje. Funkcja logowania bedzie jako parametr swojej definicji, bedzie
# przyjmowala funkcje, ktora bedzie chciala ovrapowac. Natomiast wewnatrz definicji tego dekoratora bedziemy musieli
# zapisac jeszcze inna metode. To jest cos co mozemy robic w pythonie, czyli mozemy wewnatrz jednej metody definiowac
# inna metode. Tylko w dekoratorach definiujemy funkcje w funkcji.
#

def logowanie(func):
    def wrapper(*args, **kwargs): # co wrapper bedzie przyjmowal? Arkumenty (*args) i keyWordArgumenty (**kwargs)
        print("Sprawdzamy czy uzytkownik sie zalogowal...")
        print("Wyciaganie uzytkownika z bazy danych lub sprawdzenie sesji...")
        func(*args, **kwargs)
        print("Uzytkownik zalogowany!")
    return wrapper

# Taka definicja pozwoli nam teraz na to


class Firma:
    def __init__(self, uzytkownicy):
        self.uzytkownicy = uzytkownicy
        self.urlopy = [] # pusta lista gdzie uzytkownicy beda dodawac sobie urlopy
        self.godziny = [] # pusta lista gdzie pracownicy beda wpisywali swoje godziny pracy



    def zaloguj_uzytkownika(self, imie, nazwisko):
        for uzytkownik in self.uzytkownicy:
            if uzytkownik["imie"] == imie and uzytkownik["nazwisko"] == nazwisko:
                return uzytkownik
        return None

    @logowanie
    def dodaj_urlop(self, imie, nazwisko, data_rozpoczecia, data_zakonczenia):
        urlop = {
            "imie": imie,
            "nazwisko": nazwisko,
            "data_rozpoczecia": data_rozpoczecia,
            "data_zakonczenia": data_zakonczenia
        }
        self.urlopy.append(urlop)
        return f"Urlop dla {imie} {nazwisko} zostal dodany."

    @logowanie
    def dodaj_godziny(self, imie, nazwisko, godziny):
        godziny_record = {
            "imie": imie,
            "nazwisko": nazwisko,
            "godziny": godziny
        }
        self.godziny.append(godziny_record)
        return f"Godziny dla {imie} {nazwisko} zostaly dodane."

    @logowanie
    def wyplac_pieniadze(self, imie, nazwisko, kwota):
        print("Wyplacanie pieniedzy...")
        return f"Wyplacono {kwota} zl dla {imie} {nazwisko}"


firma = Firma(uzytkownicy)

# Teraz chcemy wyplacic pieniadze. zatem piszemy:
firma.wyplac_pieniadze("Jan", "Kowalski", 1000)
# Nie wyswietli sie nam tylko i wylacznie tan nasza funkcja <wyplac_pieniadze>, ktora tutaj mamy. Wyswietli sie nam
# rowniez to co mamy w dekoratorze. Poniewaz tak zadzialal dekorator.
# W dekoratorze zrobilismy jakas logike. Hipotetycznie sprawdzilismy czy uzytkownik sie zalogowal:
# <print("Sprawdzamy czy uzytkownik sie zalogowal...")>
# po czym wykonalismy ta nasz afunkcje:
# <func(*args, **kwargs)>
# po co sa te Argumenty i KeyWordArgumenty - Dekorator nie wie co dekoruje. On nie ma pojecia co w tym naszym koszyczku
# sie znajduje. Czy tam jest zestaw kaw, czy herbat to on o tym nie wie i on to zwyczajnie opakowuje i tez nie wiadomo
# jakie parametry bedzie mial. Dekorator nie moze dzialac zbytnio na zasadzie podania sztywnych parametrow. On musi miec
# dowolnosc, dlatego wlasnie , ze te funkcje, ktore bedziemy wywolywali, ktore wywolujemy w linijce <func(*args, **kwargs)
# to one beda mialy te parametry wlasnie rozne. To jest wlasnie to co jest problematyczne

# Po co nam to?
# Uzywamy tego glownie w sytuacjach kiedy mamy jakis kod, ktory nie tylko sie powtarza, tylko ze musi
# zostac wykonany przed jakims innym. Tutaj wlasnie sprawdzenie tego czy uzytkownik jest zalogowany jest idealnym
# przykladem.
# Jezeli mamy taki system firmowy, systemy bankowe to zanim wykonamy jakas operacje, zanim jakis klient banku wykona
# jakis przelew, to musimy faktycznie wiedziec czy to jest klient banku. Przy kazdej operacji , ktora klient banku
# bedzie robil, czy to bedzie wyplacal pieniadze, czy bedzie prosil o kredyt, czy bedzie robil cos innego online, my
# musimy miec pewnosc ze to jest ten klient.
# Wiec teraz jezeli bysmy mieli setki tysiecy jakichs funkcji, ktore by robily zupelnie inne rzeczy i w tych setkach
# tysiecy funkcji mielibysmy pisac ta sama logike, no to tego kodu byloby o wiele wiecej.
# Po to to glownie wykorzystujemy, zeby dodac jakas logike, zeby dopisac cos.
# To troche dziala jak ten nasze contekst managery, ze cos sie dzieje przed, ze cos sie dzieje po. Roznica jest taka ze
# ten contekst manager on tez dziala na roznych rzeczach, na roznym kodzie, tylko on nie dziala troche na funkcji. Tam
# nie ma funkcji tylko piszemy <with open....> i piszemy faktyczny kod. a my tutaj nie piszemy faktycznego kodu tylko
# wykonujemy jakas funkcje.