#### FUNKCJE


# miasto = "warszawa", 20 #to jest krotka
# print(f"Moje miasto to {miasto[0]}")  #przy nazwie krotki <miasto> podalismy indeks (zeto w nawiasie kwadratowym) aby wyswietlil tylko nazwe <warszawa> ktora ma indeks 0
# temperatura_f = miasto[1] * 9 / 5 + 32 # przy nazwie krotki <miasto> podalismy indeks [1] (temperatura w celsiuszach) zeby dalsze dzialania dzialaly na ta wartosc 20*9 / 5 + 32 = 68 stopni Farhenhita
# print(f"Temperatur w {miasto[0]} wynosi {temperatura_f} F")
#
# praga = "Praga", 25
# print(f"Stolica czech to {praga[0]}")
# print(f"Temperatura w miescie {praga[0]} wynosi: {praga[1] * 9 / 5 + 32} stopni F")
#
# sztokholm = "Sztokholm", 30
# temperatura_f = sztokholm[1] * 9 / 5 + 32
# print(f"Stolica Szwecji to {sztokholm[0]}")
# print(f"Temperatura w miescie {sztokholm[0]} wynosi {temperatura_f} stopni F")

#### w powyzszych programach caly czas powtarzalismy nasze dzialania!!!!!!!!!!!!!!!!!!!
#########################################################################################


# #### JAK TO UPROSCIC!!!!!!!!!!!!!!!!!!!!
# #### mozna napisac petle
# miasto = [('Warszawa', 25), ('Krakow', 20), ('Wroclaw', 15), ('Gdansk', 10), ('Poznan', 5)] #lista [] w ktorej znajduja sie krotki ()
# for miasto, temperatura in miasto:
#     temp_f = temperatura * 9 / 5 + 32                                                        #:.2f - zaokragla nam danego floata do 2 (2f) miejsca po przecinku
#     print(f'Temperatura w {miasto} wynosi {temperatura} stopni Celsiusza, co odpowiada {temp_f:.2f} stopniom Fahrenheita')


########ZEBYSMY NIE MUSIELI SIE POWTARZAC I WYKONYWAC W KOLKO TYCH SAMYCH OPERACJI MOZEMY UZYC CZEGOS TAKIEFO JAK
########FUNKCJE
# funkcja to jest opakowania w ktorym bedziemy trzymac kod ktory bedzie sie wykonywal i potem bedziemy tylko ta funkcje zwracali
# takie opakowanie na chipsy
################################################################################################################################
# Jak zrobic funkcje
# - trzeba ja zdefiniowac <def>
# - pozniej nadajemy <nazwe>
# - po nazwie w nawiasach zwyklych () beda pojawiac sie parametry funkcji - parametry funkcji to nic innego jak tymczasowe zmienne takie same jak mielismy w iteracji - tymczasowe parametry
#   do wykorzystania wewnatrzfunkcji
# - nastepnie blok funkcji
# - na koniec musimy wywolac nazwe funkcji z nawiasami okraglymi (nawiasy okragle to jest to cos co wywoluje funkcje o danej nazwie) - w nawiasach okraglych podajemy parametry tej naszej funkcji
#   to co nam te parametry okresli czyli nazwa miasta ma oznaczac konkretne miasto a temperatura_w_celciuszach konkretna temperature
# - kolejnosc parametrow tej funkcji i kolejnosc ich wywolywania nie moze byc przypadkowa

# def obliczanie_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta, temperatura_w_celciuszach):
#     print(f"Obliczanie temperatury w Fahrenhaitach dla miasta: {nazwa_miasta}")
#     temperatura_fahrenheit = temperatura_w_celciuszach *9/5+32
#     print(f"Temperatura w {nazwa_miasta} wynosi {temperatura_w_celciuszach} stopni Celcjusza, co odpowiada {temperatura_fahrenheit} stopni Fahrenheita")
#
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Olecko", 20)
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Warszawa", 25)
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Koszakin", 22)
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Zakopane", 17)


########################################
# Funkcja nie zawsze musi miec parametry

# def przywitaj_sie():
#     print("Hello world")
#
# przywitaj_sie()
# # Ta funkcja dziala bez parametrow

#########################################
# def obliczanie_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta, temperatura_w_celciuszach):
#     print(f"Obliczanie temperatury w Fahrenhaitach dla miasta: {nazwa_miasta}")
#     temperatura_fahrenheit = temperatura_w_celciuszach *9/5+32
#     print(f"Temperatura w {nazwa_miasta} wynosi {temperatura_w_celciuszach} stopni Celcjusza, co odpowiada {temperatura_fahrenheit} stopni Fahrenheita")
#
# #przy wywolywaniu danej funkcji mozemy w miejsce parametru odrazu definiowac czym ten parametr ma byc
# obliczanie_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta="Olecko", temperatura_w_celciuszach=35)
#
# ################################
# #czego nie mozna robic????????
# # - taki sposob ze najpierw definiujemy parametr a pozniej wpisujemy wartosc drugiego parametru - Nie
# # jak definiujemy czym jest parametr to pozostale wartosci tez definiujemy
# # NIE NIE NIE
# # obliczanie_temperatury_w_fahrenheit_dla_miasta(nazwa_miasta="Krakow", 20)
#
#
# # Ale na odwrot juz tak - ze najpierw wpisujemy parametr funkcji a nastepnie dla kolejnego parametru definiujemy ten parametr
# # TAK TAK TAK
# obliczanie_temperatury_w_fahrenheit_dla_miasta("Krakow", temperatura_w_celciuszach=17)
# obliczanie_temperatury_w_fahrenheit_dla_miasta(temperatura_w_celciuszach=29, nazwa_miasta="Mielno") # przy definiowaniu parametrow funkcji kolejnosc nie odgrywa roli


###############definicji funkcji mozemy pisac w naszym programie nieskonczenie wiele
###     return - funkcja ta przekazuje nam wynik tej zmiennej dalej

# def sprawdz_czy_uzytkownik_jest_dorosly(wiek):
#     if wiek >= 18:
#         print("Uzytkownik jest pelnoletni.")
#         return True
#     else:
#         print("Uzytkownik nie jest pelnoletni.")
#         return False
#
# print("Witaj w naszej żabce")
#
#
# cena_zakupow = 0
#
# while True:
#     nazwa_produktu = input("Podaj nazwe produktu: ")
#     if nazwa_produktu == "":
#         break
#     cena_produkt = float(input("Podaj cene produktu: "))
#     if nazwa_produktu in ("alkohol", "papierosy", "energetyk"):
#         wiek = int(input("Podaj swoj wiek: "))
#         pelnoletni = sprawdz_czy_uzytkownik_jest_dorosly(wiek)
#         if not pelnoletni:
#             print("Nie mozesz kupic tego produktu.")
#             continue
#     cena_zakupow += cena_produkt
#
# print(cena_zakupow)


###################
# RETURN - przekazuje informacje (wynik danej funkcji) - jezeli w naszej funkcji jest jakis okreslony rezultat
#          w tym przypadku rezultat <wynik> to on ten rezultat przekazuje dalej kiedy zdefiniujemy dana funkcje

# def dodawanie(x, y):
#     wynik = x + y
#     wynik += 1
#     mnozenie = wynik * 10
#     return mnozenie

# wynik_dodawania = dodawanie(2, 3)
# print(wynik_dodawania)


###########
# Jak dziala nam RETURN wewnatrz funkcji - działa jak <break> wewnatrz petli


def sprawdzenie_emerytury(wiek, pensja, pozycja):
    wiek_do_emerytury = 65 - wiek
    if wiek_do_emerytury < 0:
        print("Jestes juz na emeryturze")
        # return pensja #<return> wewnatrz funkcji dziala jak <break> wewnatrz petli
        print("Obliczylismy emeryture dla osoby na emeryturze")
    print("Obliczamy emeryture")
    if pozycja == "programista":
        emerytura = pensja * 0.01
        print(f"Emerytura dla zawodu {pozycja} w wieku {wiek} wynosi {emerytura} zl")
    elif pozycja == "nauczyciel":
        emerytura = pensja * 0.80
        print(f"Emerytura dla zawodu {pozycja} w wieku {wiek} wynosi {emerytura} zl")
    else:
        emerytura = pensja * 0.50
        print(f"Emerytura dla zawodu {pozycja} w wieku {wiek} wynosi {emerytura} zl")
    print("Obliczylismy emeryture dla osoby pracujacej")
    return emerytura


emerytura = sprawdzenie_emerytury(wiek=67, pensja=5000, pozycja="klucznik")
print(emerytura)
