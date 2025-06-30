# Hermetyzacja jest to zabezpieczanie zmiennych przed ingerencja z zewnatrz

# mamy klase <Zolnierz>

class Zolnierz:
    def __init__(self, imie, stopien, rodzaj_broni, dywizja):
        self.imie = imie
        self.stopien = stopien
        self.rodzaj_broni = rodzaj_broni
        self.dywizja = dywizja
        self.__dywizja = dywizja # zmienna prywatna
        self._nazwisko = "Nieznane"

    def set_dywizja(self, nowa_dywizja):
        self.__dywizja = nowa_dywizja

    def get_dywizja(self):
        return self.__dywizja

# Definicja  jaka mamy pozwala nam na to, że jezeli bysmy chcieli zrobic:

szeregowy = Zolnierz("jan", "Szeregowy", "Karabin", "1 dywizja Piechoty")
major = Zolnierz("Anna", "Major", "Pistolet", "2 Dywizja Zmechanizowana")

# moglismy z ktorego kolwiek miejsca w kodzie, zmieniac sobie wlasciwosci czy to wartosci tych pol poprzez robienie tego
# w ten sposob:

szeregowy.rodzaj_broni = "Karabin maszynowy"

print(szeregowy.rodzaj_broni) # printuje nam <Karabin maszynowy>


#!!!!!!!!!!!!!!!!!!!!!!
# Takie zmiany tych naszych pol z zewnatrz a nie z wewnatrz klasy jest czyms co nie do konca bysmy chcieli robic
# Co mozemy zrobic, to mozemy w roznych jezykach programowania dac ograniczniki z jakich poziomow jestesmy w stanie
# zmieniac te wlasciwosci te nasze pola. Mozemy dac stopien hermetycacji zamkniecia zmiany tej wlasciwosci
# Mozemy stworzyc sobie cos co nazywame jest:
#
#                                           zmienna prywatna

# Zmienne prywatne to sa zmienne, ktorych stan mogli bysmy zmieniac tylko i wylacznie poprzez nasze wewnetrzne metody.
# Zmienne prywatne okreslamy poprzez dwa podkreslniki na poczatku <__>
# dopisujemy wewnatrz klasy nowa zmienna prywatna i jej definicje, ktora jest zmiana wewnatrz klasy
# Po dopisaniu na gorze zmiennej prywatnej mozemy napisac

szeregowy.set_dywizja("3 Dywizja Pancerna")
print(szeregowy.get_dywizja())

# teraz zmiane dokonalismy wewnatrz klasy

# w Pythonie nie wszystko jest oczywiste i hermetyzacja w tym jezyku nie jest do konca czyms co dziala poniewaz te
# podwojne podkreslenia, ktore teoretycznie miały by oznaczac zmienne prywatne nie dzialaja. To jest tylko i wylacznie
# nasza tylko i wylacznie dobra praktyka programistyczna, ze oznaczamy to jako zmienne prywatne poniewaz ja bez problemu
# moge zrobic tak:

szeregowy.__dywizja = "4 dywizja Powietrzna"
print(szeregowy.__dywizja)

# I w tym momencie uzylismy zewnetrznej zmiennej poza klasa co nie do konca jest prawidlowe


#                                          Zmienne typu Protected
# Zmienne z jednym podkresnikiem <_>
# Zmienne typu Protected moga byc zmieniane i odczytywane teoretycznie na poziomie jednego modulu.