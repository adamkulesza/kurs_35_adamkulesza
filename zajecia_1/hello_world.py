# To jest komentarz
# print("Hello World")
####################### INTIGERS AND FLOATS (wartosci numeryczne)########################

# wiek = 20
# print(wiek)
# wiek1 = 20 + 5
# print(wiek1)
# odejmowanie = 20 - 8
# print(odejmowanie)
# wiek2 = 20 * 16
# print(wiek2)
# wiek3 = 20 / 5
# print(wiek3)
# modulo_z_dzielenia = 20 % 8
# print(modulo_z_dzielenia)


##########Aby zaokraglic jakiegos floata tobimy to w nastepujacy sposob
x = 10 / 3
print(x)
print(round(x, 2))  #### najczesciej stosowany sposob zaokraglania
print(f"{x:.2f}")

################## STRINGS (wartosci tekstowe) #######################
########znienne typu slowa##########

# # imie = "Adam"
# # print(imie)
# imie_i_nazwisko = "Adam Kowalskie"
# # print(imie_i_nazwisko)
# dane_osobowe = imie_i_nazwisko + " 20 lat"
# print(dane_osobowe)
# liczba_1 = 35
# liczba_2 = 82
#
# suma = liczba_1 + liczba_2
# # print(suma)
#
# dlugi_string = """
#     Son she said have I got a little story for you
#     What you thought was your daddy was nothing but a...
#     While you were sittin home alone at age thirteen
#     Your real daddy was dyin sorry you didnt see him,
# """

# print(dlugi_string)

# imie_i_nazwisko_z_enterem = "Michal\nKowal" #wstawi enter pomiedzy imie i nazwisko - beda zapisane w dwoch linijkach tekstowych
# print(imie_i_nazwisko_z_enterem)

# imie_i_nazwisko = "miCHaL KowAL"
# print(imie_i_nazwisko.lower()) #wsystkie litery male
# print(imie_i_nazwisko.upper())  #wszystkie litery wielkie
# print(imie_i_nazwisko.capitalize()) #pierwsza litera wielka reszta male

############################## BOOL (wartosci logiczne - True/False) #####################################

# wartosc_prawdziwa = True
# wartosc_falszywa = False
#
# print(wartosc_prawdziwa)
# print(wartosc_falszywa)

# wiek_adama = 32
# wiek_pawla = 32

# wiek_jest_rozny = wiek_pawla != wiek_adama
# wiek_jest_rowny = wiek_pawla == wiek_adama
# print(wiek_adama == wiek_pawla) #porownanie
# # print(wiek_pawla != wiek_adama) #rozne
# # print(wiek_adama < wiek_pawla) #czy cos jest mniejsze
# # print(wiek_adama > wiek_pawla) #czy cos jest wieksze
# # print(wiek_adama <= wiek_pawla) #mniejszy lub rowny
# # print(wiek_adama >= wiek_pawla) #wiekszy lub rowny
# print(wiek_jest_rozny)
# print(wiek_jest_rowny)

######################## NONE (zmienna nieokreslona - interpreter pythona nie wie jakiego typu to beda zmienne)#################################

##do alokowanie pamieci na pozniej
# zmienna_nieokreslona = None
# print(type(zmienna_nieokreslona)) #interpreter po uruchomieniu programu okresla to jako <class 'NoneType'>
#
# zmienna_nieokreslona = 20.5
# print(type(zmienna_nieokreslona)) #interpreter po uruchomieniu programu okresla to jako <class 'float'>
#
# zmienna_nieokreslona = 20 + 22
# print(type(zmienna_nieokreslona))

############################### FORMAT STRING ################################

# imie = "Pawel"
# nazwisko = "Kowal"
# print("twoje imie to: {}, a nazwisko to: {}".format(imie, nazwisko)) #stary zapis w pythonie
# print("twoje imie to: {imie_wartosc}, a nazwisko to: {nazwisko_wartosc}".format(imie_wartosc=imie, nazwisko_wartosc=nazwisko)) #stary zapis w pythonie

# print(f"Twoje imie to: {imie}, a nazwisko to: {nazwisko}")  #nowy zapis w pythonie3


###################### STANDARDOWE WEJSCIE ############################

# imie = input("Podaj imie jubilata: ")
# nazwisko = input("Podaj nazwisko Jubilata:")
# zyczenia = input("Wpisz swoje zyczenia: ")
# print(imie, nazwisko, zyczenia)

##### castowanie danych

# wiek = input("podaj date urodzenia: ")
# print(wiek)
# print(f"to sa twoje {2025 - int(wiek)} urodziny")
####aby okreslic ile brakuje ci lat do wieku 45 lat - (wiek) jest stringiem wiec musimy wymusic zeby wartosc (wiek) czytal jako intiger poprzez takie dzialanie int(wiek)

# dwadziescia_str = str(20) # zamiana intigera na stringa mimo ze jest to intiger
# print(dwadziescia_str)
# print(type(dwadziescia_str))
# print(bool(1)) #daje True
# print(bool(0)) #daje False
# print(bool("")) #daje False
# print(bool("dfzdfshfh")) #daje True
# print(bool("0")) #daje True


# imie = input("Podaj imie jubilata: ")
# nazwisko = input("Podaj nazwisko jubilata: ")
# imie_i_nazwisko_nadawcy = input("podaj imie i nazwisko nadawcy: ")
# zyczenia = input("Wpisz swoje zyczenia: ")
# wiek = input("Podaj date urodzenia: ")
# print(imie, nazwisko)
# print(f"Wszystkiego najlepszego z okazji {2025 - int(wiek)} urodzin")
# print(zyczenia)
# print(imie_i_nazwisko_nadawcy)
