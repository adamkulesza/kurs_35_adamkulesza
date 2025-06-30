# class Programista:
#     def __init__(self, imie, jezyk_programowania):
#         self.imie = imie
#         self.jezyk_programowania = jezyk_programowania

#   To co my powyzej zrobilismy to zdefiniowalismy sobie klase i kazdy obiekt tej klasy (klasa jest naszym przepisem na
# cos, a obiekt jest nasza instancja a obiekt jest tym ciastem, ktore sobie zrobilismy), kazdy z tych obiektow, ktore
# bedziemy mielei, bedzie mial nasze dwa pola ( bedzie mial pole <imie> i pole <jezyk>) - jest to zdefiniowane w klasie i
# kazdy z obiektow bedzie ial dwie metody, ktore napisalismy ponizej.

    # def zmien_imie(self, nowe_imie):
    #     self.imie = nowe_imie

    # def zmien_jezyk(self, nowy_jezyk):
    #     self.jezyk = nowy_jezyk

# Piszemy dalej ze:

# pierwszy_programista = Programista("Jan", "Python")
# drugi_programista = Programista("Anna", "Java")

# I teraz jak napiszemy sobie ID dla obu programistow to oba ID beda rozne

# print(id(pierwszy_programista)) # drukuje pierwsze ID
# print(id(drugi_programista)) # drukuje drugie ID

# to sa dwa rozne obiekty w naszej pamieci, ktore sobie stworzylismy
# wiec jezeli teraz sobie wpiszemy:

# print(pierwszy_programista.jezyk_programowania) #wydrukuje nam <Python>
# print(drugi_programista.jezyk_programowania) # wydrukuje nam <Jawa>

# Wszystko co powyzej robilismy, robilismy za kazdym razem na poziomie obiektu.
#   W Pythonie mozemy definiowac zmienne wewnatrz klasy nie tylko na poziomie obiektu, czyli na poziomie metody __init__,
# mozemy definiowac je tez na poziomie klasy. Poniewaz wszystko w pythonie jest obiektem. Wiec my mozemy zdefiniowac
# sobie jakies zmienne klasowe.
#   Jak zmienne klasowe bedziemy definiowali wewnatrz takiej klasy?
# definiujemy je w prosty sposob  piszac nastepujace rzeczy, ktore beda wspolne dla obu programistow.

class Programista:

    jezyk = "polski" # dodajemy aby zdefiniowac zmienne klasowe
    leniwy = True # dodajemy aby zdefiniowac zmienne klasowe

    def __init__(self, imie, jezyk_programowania):
        self.imie = imie
        self.jezyk_programowania = jezyk_programowania

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie

    def zmien_jezyk(self, nowy_jezyk):
        self.jezyk = nowy_jezyk
# 3.
    @classmethod
    def zmien_bycie_leniwym(cls):
        if cls.leniwy:
            cls.leniwy = False
        else:
            cls.leniwy = True

# 5.
    @staticmethod
    def przywitaj_sie():
        print("Przywitaj sie")

pierwszy_programista = Programista("Jan", "Python")
drugi_programista = Programista("Anna", "Java")

# print(id(pierwszy_programista))
# print(id(drugi_programista))
#
# print(pierwszy_programista.jezyk_programowania)
# print(drugi_programista.jezyk_programowania)
#
# # I teraz jak sobie wyprintujemy to dostane te wlasciwosci z naszej klasy:
# print(pierwszy_programista.jezyk) # dostaniemy "polski"
# print(drugi_programista.jezyk) # dostaniemy "polski"
# print(pierwszy_programista.leniwy) # dostaniemy True
# print(drugi_programista.leniwy) # dostaniemy True

# A teraz jezeli zakomentujemy sobie wszystkie powyzsze printy i wyprintuje ID - to zarowno pierwszy obiekt jak i drugi
# obiekt maja ta sama wartosc i wskazuja dokladnie na te same zmienen w pamieci naszego programu
# print(id(pierwszy_programista.jezyk)) # To samo ID A
# print(id(drugi_programista.jezyk)) # To samo ID A
# print(id(pierwszy_programista.leniwy)) # To samo ID B
# print(id(drugi_programista.leniwy)) # To samo ID B

# Jezeli chialbym znienic wartosc dla drugiego programisty. Na przyklad drugi programista przestal byc leniwy to piszemy,
# to normalnie mogłbym napisac:
# drugi_programista.leniwy = True


# 2.
# Programista.leniwy = False

# 4.
# pierwszy_programista.zmien_bycie_leniwym()

# Co by tu nam spowodowalo? Spowodowalo nam to  ze wartosc ID zmieni sie tylko u drugiego programisty
# print(pierwszy_programista.leniwy)
# print(drugi_programista.leniwy)
# print(id(pierwszy_programista.leniwy))
# print(id(drugi_programista.leniwy))
# Dlaczego ona zmienila se tylko u drugiego programisty??
# Zmienila sie tylko i wylacznie u drugiego programisty dlatego, ze dzieje sie to poprzez mechanizm dziedziczenia.
# My w tym momencie nie nadpisalismy wartrosci <leniwy>. Nadal wartosc <leniwy = True> tylko my stworzylismy nowe pole,
# nowa zmienna zmienna w tym drugim programiscie. Okreslilismy ze to polaczenie <drugi_programista.leniwy> ma inna wartosc


#   Co mozemy w tej chwili zrobic?? Wiedzac ze wszystko w pythone jest obiektem to mozemy zadzialac w troche inny sposob.
# Zamiast zmieniac ta wartosc na jednym naszym obiekcie (obiekty sa wypadkowymi tych naszych klas), to zanmiast
# <drugi_programista.leniwy = False> ( to jest nadpisywanie na poziomie obiektu)
# mozemy napisac (przejdz do punktu # 2. powyzej)
# <Programista.leniwy = False> -  takim zapisem zmienilismy calkowicie wartosc <leniwy> na poziomie calej klasy (nadpisywanie na poziomie klasy)

#!!!!!!!!!!!!!!!!!!!!!!!!Wlasciwosci naszych obiektow sa wazniejsze niz wlasciwosci klas!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Tak wyglada relacja pomiedzy klasami a obiektami - obiekty dziedzicza po klasach


#                               Funkcje Klasowe
#
#
#   Co musieli bysmy zrobic, zeby za pomoca tego naszego drugiego programisty zmienic ta nasz zmienna <leniwy>. Mozemy to
# zrobic poprzez napisanie specjalnej metody klasowej. Zakomentujmy sobie powyzej
# <drugi_programista.leniwy = True>
# i
# <Programista.leniwy = False>
#   Metode klasowa bedziemy oznaczali <@classmethod> i piszemy ja na gorze jako kolejna metode - przejdz na gore do punktu # 3.
# I teraz gdy napisalismy nasza metode klasowa i w punkcie # 4.  napiszemy <pierwszy_programista.zmien_bycie_leniwym()>
# to po uruchomieniu okazuje sie ze zmienilismy wartosc <leniwy> True na False - ale zmienilismy to za pomoca obiektu <pierwszy_programista>
# dla wszystkich obiektow, ktore sa obiektami tej naszej klasy.


#                              Funkcje statyczne
#
#
#   Oprocz tych naszych metod klasowych (korzystaja z tego zmiany tych naszych wlasciwosci klasy a nie obiektu czyli:) mamy tez
# jezyk = "polski"
# leniwy = True)
# mamy tez inny rodzaj funkcji, wewnatrz naszych klas. Sa to funkcje statyczne:
# Piszemy na gorze w punkcie # 5.

#   Czym sa funkcje statyczne???
# Nie zawsze metody, ktore mamy zdefiniowane wewnatrz klasy beda oddzialywaly na nasz stan, ktory mamy.
# Czym jest stan - stan jest to albo zmienne klasowe
#    jezyk = "polski"
#    leniwy = True
# albo zmienne obiektu ta ktore mamy zdefiniowane w inicie: imie, jezyk_programowania - tam moga byc zdefiniowane rozne wlasciwosci
# nie wszystkie metody beda musialy ten stan zmieniac. I nie wszystkie metody, ktore bedziemy miec zdefiniowane beda
# kozrystaly z tego stanu.
#   Funkcje statyczne uzywamy wtedy kiedy nie potrzebujemy uzywac tego naszego stanu.
# Po co staramy sie uzywac funkcji statycznych?
# komentujemy sobie wszystkie powyzsze printy i wywolanie funkcji klasowej
# I napiszemy:

print(id(pierwszy_programista.przywitaj_sie))
# bez wywolania tej metody - tylko patrzymy sobie na ID tej metody i robimy:
print(id(drugi_programista.przywitaj_sie))
# To zobaczymy ze to sa dwie takie same metody o tym samym ID
#   Posiadajac 50 obiektow danej klasy i wiedzac o tym ze jakas nasza metoda nie bedzie mi oddzialywala na stan czy to
# klasy czy to obiektu, mozemy napisac nasza metode statyczna, ktora bedzie jedna i ta sama metoda dla wszystkich obiektow.
# Ona nie bedzie miala wielu alokacji w pamieci, czyli nie bedziemy tworzyli 10 dzieci. Czyli bedziemy mieli jedno dziecko np.
# Jeden rodzic bedzie cos trzymal i mowi: - ty chcesz cos wykorzystac moj synu. To ty masz. Ty curko. No to masz i wszyscy beda mieli.
# Nie bedzie to tak ze bedziecie mieli 10 takich samych zabawek dla 10 dzieci. bedziecie mieli jedna zabawke i bedziecie
# ja dobrze rozdysponowywac. Dzieki temu bedziemy mogli zaoszczedzic miejsce w pamieci.



#                                   Zmienne klasowe
#
#   Wszystko jest obiektem.
# - Klasy moga miec swoje wlasciwosci
# - Mozemy miec jakies statyczne metody
# Ale!!!!! mozemy zrobic cos totalnie abstralcynjego piszac:
# maszyna_ai jest Programista
maszyna_ai = Programista # w tym momencie do maszyna_ai przypisalismy klase

# pozwala mi to na to ze moge powiedziec ze czat_gpt jest maszyna_ai
chat_gpt = maszyna_ai("ChatGPT", "Python")
print(chat_gpt.imie)
print(chat_gpt.jezyk_programowania)

# My jestesmy nie tylko w stanie tworzyc obiekty jakichs klas, ale do zmiennej mozemy przypisywac klasy.
# Jest to wlasciwos pythona ktora mowi nam o tym ze wszystko w pythonie jest obiektem

# mozemy tez zrobic:
glupie_wywolanie = chat_gpt.przywitaj_sie
glupie_wywolanie()
# w tym momencie przypisalismy do jakiejs zmiennej nie wywolanie funkcji, nie to co mamy w returnie, tylko przypisalismy funkcje