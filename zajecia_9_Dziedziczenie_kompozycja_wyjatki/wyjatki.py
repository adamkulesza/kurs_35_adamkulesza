# Na jednej z pierwszysch lekcji pytalismy sie uzytkownika o wiek. to kastowalismy juz sonie input na "Podaj wiek".

# wiek = int(input("Podaj wiek: "))
# print(wiek)

# problem pojawial sie kiedy wiek podawalismy jako wyraz (string) a nie intiger (int)
# Co musielismy zrobic teoretycznie

# wiek = input("Podaj wiek: ")
# if isinstance(wiek, int):
#     wiek = int(wiek)
# else:
#     print("Podano nie prawidlowy wiek, oczekiwano liczby calkowitej.")

# W taki sposob moglismy uodpornic sie na to co defacto sie tutaj dzieje. Jednak problem jest taki ze uodpornilismy sie
# na jeden blad i prawda jest taka ze zabezpieczylismy sobie tylko i wylacznie jedna linijke kodu. i w taki sposob nie
# jestesmy w stanie zabezpieczyc wiecej linijek.

#Jaki jest inny sposob zebysmy mogli faktycznie ten program uruchomic??
#Wyobrazcie sobie ze mamy cos takiego

lista_uczniow = [{
    "imie": "Jan",
    "wiek": 20,
}, {
    "imie": "Anna",
    "wiek": 22,
}, {
    "imie": "Piotr",
    "wiek": 19,
}]
# i mu prosimy uzytkownika o podanie dwoch rzeczy

# wiek = int(input("Podaj wiek ucznia: "))
# numer_na_liscie = int(input("Podaj numer ucznia: "))

# zeby ten program nam faktycznie dzialal to chcieli bysmy finalnie dostac

# uczen = lista_uczniow[numer_na_liscie] if lista_uczniow[numer_na_liscie].get("wiek") == wiek else None

# takie wyrazenie moze nam powodowac kilka bledow - i chielibysmy sie przed tymi bledami zabezpieczyc, zamiast pisac
# setki instrukcji warunkowych mozemy uzyc dosc ciekawej skladni.




#                          Skladnia Try/Excepr

# Skladnia ta bedzie nas zabezpieczala przed roznymi wyjatkami, ktore mozemy dostac.

# try:    #   Blok try bedzie blokiem wykonywalnym ( wewnatrz tego bloku bedziemy pisac instrukcje tak jak by tego bloku nie
#         # bylo - instrukcja ta mowi nam "sprobuj" sprobuj to uruchomic"
#     wiek = int(input("Podaj wiek ucznia: "))
#     numer_na_liscie = int(input("Podaj numer ucznia: "))
#
#     uczen = lista_uczniow[numer_na_liscie] if lista_uczniow[numer_na_liscie].get("wiek") == wiek else None
#     print(uczen)
# #   Po bloku <try> bedziemy mieli blok <except>
# except Exception as e:  #   Blok <except bedzie wykonywany jezeli my trafimy sobie na jakis nasz wyjatek. Taki domyslny
#                         # wyjatek, wyjatek bazowy nazwwa sie <Exception>. To jest taki nasz globalny blad, po ktorym
#                         # dziedzicza wszystkie inne bledy, ktore my w tym pythonie mamy. <e> to bedie ten nasz blad
#                         # ktory bedziemy przekazywali i printowali
#     print(e)
#
#   Po uruchomieniu programu i wpisaniu "dwadziescia" program nam drukuje informacje o bledzie
# <invalid literal for int() with base 10: 'Dwadziescia'>
# a nie wyswietla bleduna czerwono. Jak by tego bloku try/except nie bylo to informacja o bledzie by sie pojawila.
#   W tym bloku <except> mozemy robic rozne rzeczy. bardzo czesto nie printujemy tylko przekazujemy ten nasz blad do
# jakichs logow, albo do jakichs zewnetrznych narzedzi. Te nasze programy duze, webowe maja zewnetrze na przyklad narzedzie
# do monitorowania, do obserwowania tej naszej aplikacji, no i wtedy jak trafimy na taki bloczek <except> to w naszym
# programie zewnetrznym pojawi sie informacja ze w danym miejscu jest blad o okreslonej nazwie.
#   Ta formule try/except mozemy wykorzystywac za kazdym razem - sprawdzac kazda czesc kodu czy nie wyskakuje nam blad i
# wrzucac ja nieskonczona ilosc razy. Mozemy zagniezdzac nawet te try/except


#   Takie lapanie wyjatkow jest czyms niezgodnym z zasadami PEP o ktorych byla mowa we wczesniejszych lekcjach, poniewaz
# nasz blad <Exception> jest naszym bledem bazowym, po ktorym dziedzicza wszystkie bledy. Czyli jezeli my bysmy zostawili
# ten kod w taki sposob, jaki mamy go tu napisanego, to bysmy byli bezpieczni na wszystkie beledy swiata, ktore w pythonie
# mozemy znalezc. Nie jest to poprawne poniewaz powinnismy okreslic specyficznie jakie beledy chcemy lapac. Wiec taki
# zapis nie jest do konca poprawnym.
#
#   Co powinnismy zamiast tego zrobic? Powinnismy napisac jakiego bledu sie spodziewamy
# blok except oznacza:
#                           "wylap", "oczekuj jakiegos bledu (specyficznego)"
# My nie wyczekujemy jakiegos globalnego bledu, ktory nie wiadomo czym bedzie, tylko musimy powiedziec jakiego specyficznie
# bledu sie spodziewamy, na jaki specyficzny blad chcemy sie zabezpieczyc.
# Na przyklad mozemy wpisac: <ValueError> zamiast Exception

try:
    wiek = int(input("Podaj wiek ucznia: "))
    numer_na_liscie = int(input("Podaj numer ucznia: "))

    uczen = lista_uczniow[numer_na_liscie] if lista_uczniow[numer_na_liscie].get("wiek") == wiek else None
    print(uczen)
# except ValueError as e:
#     print("Podano nieprawidlowa wartosc(wartosc powinna byc liczbowa):", e)

# Program zapyta sie nas najpierw o wiek
# Podaj wiek ucznia: 10 # wpisujemy 10
#
# nastepnie zapyta sie
# Podaj numer ucznia: 4 # wpisujemy 4

# Program wyrzuci nam blad, bo wartosc ktora podalismy (numer ucznia 4) powoduje IndexError.
# Jako ze ten blad nie jest ValueError a jest IndexError to tylko ValueError jest zabezpieczony przez blok try/except.
#
#   W tym momencie jestesmy jestesmy zabezpieczenie na jeden blad ValueError, ktory istnieje. co mozemy zrobic to mozemy
# zabezpieczyc ten nasz blok <try> na wiecej niz jeden blad i mozemy robic rozne rzeczy w zaleznosci od tego jaki ten
# blad bedzie. Jak to zrobic?
#   Blok <except> moze miec wiele tych except

# except IndexError as e:
#     print("Podano nie prawidlowy numer ucznia(indeks poza zakresem listy):", e)

#   Jezeli bysmy chcieli miec globalny error message, ale spodziewalibysmy sie wiecej niz jednego bledu i na przyklad
# chcielibysmy abu IndexError i ValueError mialy dokladnie to samo zachowanie, to nie ma sensu zwielokratniac exceptow.
# Mozemy polaczyc te nasze excepty w jeden. wpisujemy taki globalny except dla dwoch bledow:

except (ValueError, IndexError) as e:
    print("Wystapil blad:", e)

# Oprocz tych naszych dwoch wyrazen istnieje operacja <finally>
# Operacja <finally> "Koniec programu" bedzie operacja, ktora zostanie wykonana niezaleznie od tego czy kod rzuci nam
# blad ValueError czy IndexError, czy ten nasz kod przejdzie calkowicie. Uruchomi sie zawsze.
# Co my w tej instrukcji <finally mamy? To zazwyczaj mamy zamykanie jakichs polaczen. Na przyklad:
# Otwieramy polaczenie do bazy danych za pomoca kontext menadzera ale trafiamy na jakis blad. Ten program nam sie
# wukrzacza. To ten blok finally gwarantuje nam to ze pomimo tego ze tem blad dostaniemy dostaniemy, ktorego sie
# spodziewamy, to tak czy siak to polaczenie zostanie zakonczone. Nie wazne czy ten blad jest czy tego bledu nie bedzie
# to to polaczenie zostanie zawsze zakonczone.
finally:
    print("Koniec programu")