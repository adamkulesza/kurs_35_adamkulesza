# Stworzmy sobie na potrzeby zajec jakas strukture <users> ktora bedzie lista naszych slownikow
from collections.abc import Iterable, Iterator

users = [{
        "name": "Jan Kowalski",
        "age": 30,
        "email": "jan.kowalski@gmail.com",
        "address": "Warszawa, Polska",
        "zip_code": "00-001",
        "city": "Warszawa",
        "country": "Polska"
    },
    {
        "name": "Anna Nowak",
        "age": 25,
        "email": "anna.nowak@gmail.com",
        "address": "Krakow, Polska",
        "zip_code": "31-001",
        "city": "Krakow",
        "country": "Polska"
    },
    {
        "name": "Piotr Wisniewski",
        "age": 40,
        "email": "piotr.wisniewski@gmail.com",
        "address": "Wroclaw, Polska",
        "zip_code": "50-001",
        "city": "Wroclaw",
        "country": "Polska"
}]

#   Mamy naszych 3 uzytkownikow, ktorych trzymamy w naszym systemie
#   Zalozmy sobie na potrzeby tego naszego programu, ze to nie sa uzytkownicy, ktorych aktualnie ja w systemie mam, tylko
# tych trzech uzytkownikow bedziemy sobie pobierac z innego pliku lub zewnetrznego API. To sa dane ktore przyjda.
#   Napiszmy sobie funkcje ktora bedzie nam tych usersow przygotowywala. Funkcja ktora bedzie nam dane urzytkownikow
# przeksztalcala w jeden adres - strukture, ktora bedzie nam bardziej przydatna.

def address_parser_for_users(userd):
    parsed_users = []
    for user in users:
        parsed_users.append({
            "name": user.get("name"),
            "age": user.get("age"),
            "email": user.get("email"),
            "full_address": user.get("address") + "," + user.get("zip_code") + " " + user.get("city") + "," + user.get("country")
        })
    return parsed_users

users_in_our_system = address_parser_for_users(users)
print(users_in_our_system)

#   Jaki problem wystepuje w momencie kiedy my to zrobimy????
# Przeparsowalismy sobie tych uzytkownikow, ale co musielismy zrobic to musielismy stworzyc liste <parsed_users = []> gdzie
# wrzucalismy tam te swoje dane, tych swoich uzytkownikow. Poniewaz funkcje maja tylko i wylacznie mozliwosc zwrocenia nam
# jednorazowo calej struktury.


# Nie moglismy tego zrobic w taki sposob. Bo zwroci nam to tylko jednego uzytkownika -  tworzac pusta liste i dodajac do
# niej kazdego uzytkownika powodujemy ze po zrobieniu raz tej funkcji z jednym uzytkownikiem wrzuca ja do pustej listy i
# zaczyna ponownie ta funkcje dla kolejnego uzytkownika.

# def address_parser_for_users(userd):
#     for user in users:
#         return{
#             "name": user.get("name"),
#             "age": user.get("age"),
#             "email": user.get("email"),
#             "full_address": user.get("address") + "," + user.get("zip_code") + " " + user.get("city") + "," + user.get("country")
#         }
#     return parsed_users
#
# users_in_our_system = address_parser_for_users(users)
# print(users_in_our_system)

#   W tym momencie, ktory mamy w tej naszej symulacji, nie jest to az tak problematyczne, poniewaz ta struktura, ta lista
# jest krotka. Mamy tylko i wylacznie 3 uzytkownikow ktorych dostalismy od naszego zewnetrznego dostawcy (czy to plik czy to API) i
# przetworzylismy ich sobie - wrzucilismy do listy. Wiec jezeli chodzi o objetosc pamieciowa tego naszego programu, nie
# jest to az tak problematyczne. Pamietajmy ze musimy my ta liste stworzyc i musimy do niej wrzucac.

#   W pythonie istnieje cos zupelnie nowego czego jeszcze nie znalismy co nazywa sie


#                                       GENERATOR


#   Generator bedzie pozwalal nam na to, zebysmy my nie musieli tworzyc takiej tymczasowej struktury w pamieci naszego
# programu - tylko bedzie umozliwial nam zwracanie kolejnych wartosci w momencie kiedy bedziemy na przyklad po czyms
# iterowac. Jak to dziala?
# Piszemy sobie kolejna funkcje

def address_parser_for_users_generator(users):

# na ten moment generator nie rozni sie niczym od naszej podstawowej funkcji ktora napisalismy

    for user in users:

# w tym momencie z pomoca przychodzi nam generator. Czym generatory roznia sie od tych naszych funkcji?
# Roznicas w sposobie zapisu w jezyku Python jest jedna. Do tej pory mielismy slowko kluczowe <return>, ktore zwracalo
# nam cos i my moglismy przypisac to do jakiejs zmiennej, jak robilismy to w pierwszej funkcji.
# W generatorach zamist slowka <return> mozemy uzyc slowka <yield>. Slowko to automatycznie z funkcji tworzy nam generator.
# Jaka jest roznica, ktora teraz nam nastapi? Do tej pory kiedy do pierwszej funkcji na koniec dopisalismy

#                   print(type(users_in_our_system))  otrzymywalismy ze jest to typ 'list'

# W momencie kiedy bedziemy mieli generatory i bedziemy do jakiejs zmiennej przypisywali wykonane jakiegos generatora,
# to defacto nie bedziemy mieli tego to co zwraca - on zwroci nam obiekt generujacy w takiej postaci

#                       <generator object address_parser_for_users_generator at 0x00000167DB16BC40>
# czyli nowa strukture

        yield {
            "name": user.get("name"),
            "age": user.get("age"),
            "email": user.get("email"),
            "full_address": user.get("address") + "," + user.get("zip_code") + " " + user.get("city") + "," + user.get("country")
        }
generator = address_parser_for_users_generator(users)

print(generator)

# Generator pozwala nam na to zebysmy nie musieli tworzyc tych tymczasowych struktur, do ktorych bedziemy musieli wrzucac
# bardzo duzo jakichs naszych struktur, tych naszych obiektow, zeby nam ta pamiec nie rosla.
#   Co jestesmy w stanie zrobic tym naszym generatorem?
#   Jestesmy na generatorach w stanie wykonac metode <next>, ktora bedzie nam zwracala wartosc, ktora mamy przy tym
# slowku <yield> dopiero teraz

# print(next(generator))

#   Jaka jest roznica? Roznica jest taka, ze jak wpiszemy znowu to samo <print(next(generator))> to automatycznie zostanie
# odczytana kolejna wartosc z naszej listy

# print(next(generator))
# print(next(generator))

#   Generatory sa w stanie zapamietywac na ktorej iteracji w pentli jestesmy, zapamietywac stan w ktorym aktualnie sie
# znajdujemy.
#   Osiagnelismy to ze tych danych, ktore trzymalismy w tej naszej liscie, juz w tej liscie nie trzymamy, nie zajmujemy
# pamieci i program nam nie puchnie, tylko my w biegu to sobie formatujemy i w biegu przekazujemy kolejne wartosci.

#   Generatory to obiekty iterowalne - mowi nam to to ze my mozemy wykonac na niej pentle <for>
# zakomentujmy <print(next(generator))> i napiszmy pentle for

for user in generator:
    print(user)

# po napisaniu takiej pentli <for> mamy wyswietlone wszystkie slowniki w liscie - i tak to wyglada po uruchomieniu programu

# {'name': 'Jan Kowalski', 'age': 30, 'email': 'jan.kowalski@gmail.com', 'full_address': 'Warszawa, Polska,00-001 Warszawa,Polska'}
# {'name': 'Anna Nowak', 'age': 25, 'email': 'anna.nowak@gmail.com', 'full_address': 'Krakow, Polska,31-001 Krakow,Polska'}
# {'name': 'Piotr Wisniewski', 'age': 40, 'email': 'piotr.wisniewski@gmail.com', 'full_address': 'Wroclaw, Polska,50-001 Wroclaw,Polska'}

#   Co jest jeszcze dosyc ciekawe w tych generatorach?? Bedzie nam to potrzebne do rozumienia kolejnej rzeczy ktorymi sa
# iteratort, to w momencie kiedy wykonamy metode <next> na generatorze.

# next(generator)

# to wyskoczy nam blad <StopIteration>. Co to oznacza? Oznacza na to, ze Generatory sa w stanie zwracac nam kolejne
# wartosci podczas iteracji, natomiast ta iteracja sie kiedys konczy, wiec takie randomowe wyrzucenie kolejnej wartosci
# <next(gerenrator)> bedzie skutkowalo nam tym, ze bedziemy musieli dostac ten blad. generatory pozwalaja nam na to
# zebysmy mielei pewnosc ze cos przestalo dzialac, ze skonczylismy iterowac, ze mamy ten nasz plik (100 000 linijek) i
# skonczylismy iterowac. Powinno nam to dzialac za pomoca pentli <for> ale nie zawsze dzialamy za pomoca pentli <for>
# Czasami mozemy dzialac klikajac ta metode <next>, bo chcemy strikte wykonac cos i chcemy manualnie zarzadzac tym naszym
# workflow. Wiec jezeli chcieli bysmy zarzadzac manualnie tm naszym workflowem nie poprzez pentle <for> ale poprzez
# wykonywanie reczne tej metody <next>

#   przejdz do pliku <generators_example>


# Do tego czasu tworzylismy sobie generatory, ktore byly funkcjami. Mozna je bylo zapisywac za pomoca funkcji. Roznily
# sie instrukcja <yield>, natomiast ta nasz skladnia nie roznila sie az tak bardzo od tych naszych funkcji.
#   Oprocz generatorow mamy cos bardzo podobnego co nazywa sie:

#                                               ITERATOR

#   Iteratory mozemy tworzyc dwojako:

lista_uczniow = ["jan", "Anna", "Piotr", "Kasia", "Tomek", "Ola", "Marek", "Zosia", "Krzysztof", "Ewa"]
print(type(lista_uczniow))

# jak sobie to wyprintujemy to dowiemy sie ze jest ona lista.
# Pamietamy ze listy sa obiektami iterowalnymi. wiec jezeli napiszemy:

print(isinstance(lista_uczniow, Iterable))

# to dostaniemy wartosc <True>
# oprocz obiektow iterowalnych i oprucz generatorow istnieje trzecia rzecz po ktorej mozemy iterowac, sa to:

#                                               iteratory

# Jak takie iteratory tworzymy???
#                                     Iteratory mozemy tworzyc dwojako:

#                                                   1.

# mozemy scastowac liste uczniow do iteratora. Zeby skastowac liste uczniow do iteratora musimy uzyc instrukcji <iter>
# kiedy napiszemy:
#                           lista_iterator = iter(lista_uczniow)
#                           print(type(lista_iterator))
#                           print(isinstance(lista_iterator, Iterator))
#
# to otrzymamy odpowiedz    <class 'list_iterator'>
#                           True

lista_iterator = iter(lista_uczniow)
print(type(lista_iterator))
print(isinstance(lista_iterator, Iterator))

# Po co my to w ogole robimy?? Robimy my tez po to zebysmy mogli na nich rownie dobrze wykonywac pentle <for>

for item in lista_iterator:
    print(item)

#                                   Generatory i Iteratory sa iterowalne

# Generator
# Generator to specjalny rodzaj iteratora, który:
# sama implementuje protokół iteratora (czyli <__iter__()> i <__next__()> są tworzone automatycznie)
# używa słowa kluczowego <yield> zamiast return
# pozwala łatwiej i krócej pisać iteratory


# Iterator
# Iterator to obiekt, który implementuje metody:
# __iter__() — zwraca obiekt iteratora (zwykle self)
# __next__() — zwraca następny element lub zgłasza wyjątek StopIteration, gdy elementy się skończą


# Kazdy Generator jest Iteratorem - ma StopIteration, ma ta metode <next> pisana w ten sposob
# nie kazdy Iterator jest generatorem - nie kazdy ma metode <next>, nie kazdy iterator w momencie kiedy bedziemy sobie
# po nim iterowali bedzie automatycznie mial te mechanike zakonczenia iteracji


#                           2. Iteratory mozemy tworzyc za pomoca klasy


# metoda magiczna                       __iter__(self)
# metody magiczne to takie metody, ktorych wywolanie bylo nie jawne - nie musielismy wywolywac metody __init__ tylko ta
# metoda __init__ sama nam sie dziala w pewnym momencie.
# ta metoda magiczna __iter__ pozwala nam zwrocenie jakiegos iteratora.
# Co jest bardzo wazne w metodzie magicznej __iter__ ktrora bedziemy mieli, bedziemy musieli zwrocic iterator <self>
# jak taki iterator zwrocic - musimy po prostu wykonac __iter__ na <self.data> - moglismy obiektu iterowalne parsowac na iteratory.

class MyIterator:
    def __init__(self, data: dict):
        self.data = data

    def __iter__(self):
        return iter(self.data.items())

# jak teraz zrobimy sobie:

my_iterator = MyIterator({"a": 1, "b": 2, "c": 3}) # slownik
# next(my_iterator)

# to po uruchomieniu tego programu wyskoczy nam blad <TypeError: 'MyIterator' object is not an iterator>

# ale jezeli zrobimy zamiast <next(my_iterator)> wpiszemy:
for item in my_iterator:
    print(item)

# program wyprintuje nam klucze
# a
# b
# c
# metody <next> nie mamy ale mamy mozliwosc iterowania po ty naszym obiekcie/slowniku
# jezeli napszemy:
#                   return iter(self.data.items())
# to wyprintuje nam
# ('a', 1)
# ('b', 2)
# ('c', 3)
# jezeli napszemy:
#                   return iter(self.data.values())
# to wyprintuje nam
# 1
# 2
# 3


# wiec defakto zrobilismy z tego obiekt iterowalny
#skoro nie mamy domyslnie tej metody next to musimy toa metode napisac - dopisujemy do funkcji na gorze

# 1. sposob stworzenia __next__
#Aby uzyc metody __next__ musimy stworzyc iterator

# class MyIterator:
#     def __init__(self, data: dict):
#         self.data = data
#         self.iterator = iter(self.data.items()) #### to jest iterator ktory stworzylismy aby nam metoda __next__ dzialala
#
#     def __iter__(self):
#         return self # zwracamy tutaj tylko <self> - mowi nam to to ze my zwracamy ten obiekt - czyli ten obiekt bedzie iteratorem ktory bedziemy zwracali w metodzie iter
#
#     def __next__(self):
#         return next(self.iterator)
#
# my_iterator = MyIterator({"a": 1, "b": 2, "c": 3}) # slownik
#
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# i w taki sposob wykorzystalismy metode __next__ w iteratorze

# 2. sposob stworzenia __next__
class MyIteratorVersion2:
    def __init__(self, data: dict):
        self.data = list(data.items()) # kastowanie do listy naszego slownika
        self.index = 0  # Poniewaz my nie bedziemy mogli magicznie generowac tego __nexta__ i liczyc na to ze ten __next__
                        # jest zaimplementowany w innej strukturze. Tutaj nie jestesmy w stanie tego zrobic.
                        # Wobec tego piszemy sobie metode __iter__

    def __iter__(self):
        return self # zwracamy obiekt na ktorym iterujemy. Jezeli chcielibysmy wykorzystac metode __next__, jezeli
                    # chcielibysmy iterowac po tym obiekcie i uzyc ten obiekt jako iterator, a nie iterowac po czyms
                    # zewnetrznym. Nastepnie robimy sobie metode __next__

    def __next__(self):
        if self.index < len(self.data): # jezeli <self.index> jest mniejszy od dlugosci <self.data> od dlugosci naszej list
            result = self.data[self.index] #czyli najpierw bedzie zero (0) (bo tyle wynosi self.index
            self.index += 1 # nastepnie zwiekszamy nasz index o 1 do momentu kiedy dojdzie do dlugosci naszej self.data
                            # o tym mowi <if self.index < len(self.data):
            return result

# na samym dole mozemy dpisac wielokrotnie <print(next(iterator_v2))>



iterator_v2 = MyIteratorVersion2({"a": 1, "b": 2, "c": 3})

print(iterator_v2.data)

print(next(iterator_v2))
print(next(iterator_v2))
print(next(iterator_v2))
print(next(iterator_v2)) # Po wyprintowaniu tego wyskakuje nam None a nie StopIterationError
print(next(iterator_v2)) # Po wyprintowaniu tego wyskakuje nam None a nie StopIterationError
print(next(iterator_v2)) # Po wyprintowaniu tego wyskakuje nam None a nie StopIterationError