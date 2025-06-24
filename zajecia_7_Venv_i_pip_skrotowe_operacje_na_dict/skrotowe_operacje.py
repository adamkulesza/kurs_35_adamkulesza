############ Operacje (instrukcje) warunkowe ##############
# # program pytajacy uzytkownika o wiek - tak zeby sprawdzic czy uzytkownik jest pelnoletni
#
# wiek = int(input("Podaj swoj wiek: "))
#
# if wiek >= 18:
#     pelnoletni = True
# else:
#     pelnoletni = False
#
# print(pelnoletni)
#
# #     W pythonie takie pojedyncze instrukcje warunkowe, w ktorych mamy tylko i wylacznie dwa wyjscia, czyli nie mamy
# # zadnego <elif>, Mamy tylko i wylacznie rozgalezienie ze tylko albo lewy zbior albo prawy zbior, mozemy zapisac w
# # prostrzej postaci.


# #                                       Jak skracac takiego <ifa>???
# #     Zwroc uwage ze w obu przypadkach przypisujemy jakas wartosc do naszej pewnej zmiennej <pelnoletni>. Wiec teraz zebysmy
# # mogli to teraz skrocic to usimy znowu przypisac ta wartosc
#
# wiek = int(input("Podaj swoj wiek: "))
# pelnoletni_skrot = True if wiek >= 18 else False
# print(pelnoletni_skrot)
#
# # nazwa_zmiennej = <pierwsza_wartosc> if <warunek_na_pierwsza_warrtosc> else <druga_wartosc>




########### List Comprehensions ###########
# # zaluzmu ze mamy liste uczniow od uzytkownika ktory nie jest biegly w pisaniu na klawiaturze
#
# lista_uczniow = ["Jan", "Anna", "Piotr", "kaSia", "marek"]
#
# #     My w systemie naszym szkolnym chcielibysmy zeby wszyscy uczniowie mieli poprawne napisane imie.
# # Mozemy zrobic prosty program - mozemy zrobic tak:
#
# poprawna_lista_uczniow = []
# for uczen in lista_uczniow:
#     poprawna_lista_uczniow.append(uczen.capitalize())
#
# print(poprawna_lista_uczniow)

# #       Co tutaj zrobilismy? to defakto z jednej struktury danych stworzylismy druga - po prostu ja przeksztalcilismy.
# #       Takie cos mozemy tez wykonac za pomoca czegos co nazywa sie <List Comprehensions>. My mozemy juz zaladowac na
# # samym poczatku dane do jakiejs naszej struktury (narazie robimy to tylko i wylacznie do listy) bez uzywania petli <for>
# # i bez iteracji takiej jak zrobilismy powyzej (bez robienia ze najpierw tworzymy sobie pusta liste a pozniej dodajemy po kolei)
# #       Zeby to zrobic musimu uzyc <List Comprehension>
#
# lista_uczniow = ["Jan", "Anna", "Piotr", "kaSia", "marek"]
# poprawna_lista_uczniow_comprehension = [uczen.capitalize() for  uczen in lista_uczniow]
# print(poprawna_lista_uczniow_comprehension)
#
# # nazwa_zmiennej = [,wartosc, ktora zapisujemy w liscie> for <tymczasowa_zmienna> in <ITERABLE - struktura iterowalna, ktora iterujemy>]
#
# #       Po co my uzywamy tego zamias petli <for>
# # 1. Mamy mniej kodu
# # 2. Szybkosc dzialania tego (NAJWAZNIEJSZA RZECZ)
#
# #       Takie list comprechension mozemy robic np. dla wkadratow liczb
# kwadraty_liczb = [x**2 for x in range(10)]
# print(kwadraty_liczb)


# lista_uczniow = ["Jan", "Anna", "Piotr", "kaSia", "marek"]
# #       W jezyku polskim najczesciej imiona zenskie koncza sie na litere "A" Wiec moglibysmy z tej listy uczniow sprobowac
# # za pomoca list comprehension polaczonego z instrukcjami warunkowymi ktore sa w jednej linijce stworzyc liste dziewczynek
# # w naszej szkole. Do <listy dziewczynek> bedziemy dodawali naszego
# #                               <uczen.capitalize for uczen in lista_uczniow>
# # w tym momencie otrzymamy liste wszystkich uczniow - wiec musimy liste_uczniow przefiltrowac tak aby wylowic same dziewczynki
# #       Filtrowanie w list comprehension mozemy zrobic za pomoca tych naszych <ifowych> operacji dodajemy
# #                               <if uczen.lower().endswith("a")>
# #                                       mozna tez zrobic
# #                               <if uczen.lower()[-1] == "a">
# lista_dziewczynek = [uczen.capitalize() for uczen in lista_uczniow if uczen.lower().endswith("a")]
# lista_chlopcow = [uczen.capitalize() for uczen in lista_uczniow if not uczen.lower().endswith("a")]
# print(lista_dziewczynek)
# print(lista_chlopcow)
#
# #Nazwa_zmiennej = [<wartosc,ktora zapisujemy w liscie. for <tymczasowa_zmienna> in <ITERABLE -obielt iterowalny> if <warunek po ktorym bedziemy filtrowali nasze dane>]





############## Dict Comprehensions ######################
#       Zasada dzialania <Dict Comprechension jest dokladnie taka sama jak <List Comprechension> - wiec mogli bysmy sobie zrobic

lista_uczniow = ["Jan", "Anna", "Piotr", "kaSia", "marek"]
slownik_uczniow = {uczen: uczen.capitalize() for uczen in lista_uczniow}
print(slownik_uczniow)

# nazwa_zmiennej = {klucz: wartosc for <tymczasowa_zmienna in <ITERABLE - obiekt iterowalny}
#
#       Jaka jest roznica miedzy <List Comprehension> a <Dict Comprehension> roznica jest taka, ze w <Dict...> musi byc
# slownik (struktura w nawiasach klamrowych), druga rzecz jest taka ze w <List...> mielismy na poczatku <wartosc, ktora zapisujemy w liscie>
# Nalezy pamietac ze list sa tymi struktorami tylko i wylacznie posiadajacymi wartosc, one sa indeksowalne, natomiast one
# nie maja kluczy. Wiec zebysmy mogli zrobic <Dict Comprehension> to musimy podac zarowno <klucz> jak i <wartosc>.
#       Kiedy takie <Dict Comprechension> moze byc stosane kiedy chcemy przeksztalcic strukture na jakas inna, jak
# dostraniemy jakies wartosci od uzytkownika wtedy mozemy <dict Comprehension> stworzyc taki inny zapis i w momencie,
# w ktorym mamy jakies dane, mamy jakas strukture wczesniej i chcemy ta strukture przeksztalcic do slownika (cos iterowalnego przeksztalcic na slownik)

slownik_uczniow_1 = {index: value for index, value in enumerate(lista_uczniow)}
print(slownik_uczniow_1)

# moze byc tez z warunkiem jak przy <list...>

slownik_uczniow_2 = {index: value for index, value in enumerate(lista_uczniow) if value.lower().endswith("a")}
print(slownik_uczniow_2)



# Przyklad po co jest Dict Comprehension
# Chcielibysmy przeksztalcic ta nasza strukture na strukture gdzie bedziemy mieli Jan: Kowalski - zeby np mozna bylo na
# tej strukturze latwiej pracowac
lista_uczniow_nowa_struktura = [{
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 18
}, {
    "imie": "Anna",
    "nazwisko": "Nowak",
    "wiek": 17
}, {
    "imie": "Piotr",
    "nazwisko": "Zielinski",
    "wiek": 19
}]

slownik_uczniow_nowa_struktura = {uczen["imie"]: uczen["nazwisko"] for uczen in lista_uczniow_nowa_struktura}
print(slownik_uczniow_nowa_struktura)