############################### baramki logiczne

# wiek = int(input("podaj swoj wiek: "))
# plec = input("podaj swoja plec: ")

# czy_moge_glosowac = wiek >= 18 and plec == "meszczyzna" ##### oba warunki musza byc spelnione
# print(czy_moge_glosowac)

# czy_moge_glosowac = wiek >= 18 or plec == "meszczyzna" ##### jeden z warunkow musi byc spelniont
# print(czy_moge_glosowac)


##################################################### datetime
# import datetime
#
# print(f"Obecnie mamy: {datetime.datetime.now()}") ### aby pobrac z biblioteki aktualna date i godzine

# current_year = datetime.datetime.now().year
# print(current_year)

# current_year = (datetime.datetime.now().astimezone())
# print(current_year)

# next_year = (datetime.datetime.now() + datetime.timedelta(days=365)).year ###podanie kolejnego roku w oparciu o dzisiejsza date
# print(next_year)


########################### inne
wiek = 20
print(wiek)
# wiek = wiek + 1

# wiek = wiek * 2
# print(wiek)

wiek += 1 #to jest taki sam zapis jak wiek = wiek + 1
print(wiek)

moje_imie = "Adam"
moje_imie += "!!!!!!"
print(moje_imie)