uczen_1 = "Michal"
uczen_2 = "Kasia"
uczen_3 = "Ania"
uczen_4 = "Krzysiek"

###### LISTA PIERWSZY SPOSOB ###########

lista_uczniow_klasy_4 = ["Michal", "Kasia", "Ania", "Krzysiek"]
lista_uczniow_klasy_4_ze_zmiennymi = [uczen_1, uczen_2, uczen_3, uczen_4]
lista_produktow_na_zakupy = ["jablka", "banany", "gruszki", "czeresnie"]
print(lista_produktow_na_zakupy)

# listy sa indeksowalne - kolejnosc jest po cos - kolejnosc ma znaczenie - kazdy element z listy ma swoj indeks
# i mozemy podajac indeks uzyskac konkretna informacje o elemencie z tej listy, ktory ma ten indeks
# indeksujemy od lewej - 0, 1, 2, 3 itd.
jablka = lista_produktow_na_zakupy[0] # w nawiasie kwadratowym [] podany jest indeks danej pozycji z listy
print(jablka)
#jezeli bedziemy chcieli wpisac indeks ktory nie istnieje w naszej liscie np(4) to wyskoczy nam blad


######## LISTA DRUGI SPOSOB ######################

lista_drugi_sposob = list()
print(lista_drugi_sposob)


############# listy moga przechowywac rozne typy danych
lista_naszych_zmiennych = ["Michal", 23, True, uczen_1, 2.22, []]


############## aby dodac cos do listy trzeba wykonac operacje dodawania .append - operacja .append dodaje element na koniec listy
lista_produktow_na_zakupy.append("jajka")
print(lista_produktow_na_zakupy)



###############innym sposobem dodawania jest operacja .insert - precyzujemy w ktory indeks wrzucic (int) i co mamy wrzucic
# jednakze, wowczas program musi przesunac wszystkie obiekty na inne indeksy co jest czasochlonne i moze
# nie byc oplacalne
lista_produktow_na_zakupy.insert(0,"mąka")
print(lista_produktow_na_zakupy)



############### przeszukiwanie listy po indeksie i wyszukiwanie wartosci danego indexu
print(lista_produktow_na_zakupy.index("banany")) # tak znajdujemy index danego obiektu w liscie
index_banany = lista_produktow_na_zakupy.index("banany") #
banany = lista_produktow_na_zakupy[index_banany]
print(banany)



######### listy sa obiektami iterowalnymi
####pierwszy sposob iterowania
for element_w_liscie in lista_produktow_na_zakupy:
    print(element_w_liscie)


jablka = None
for element_w_liscie in lista_produktow_na_zakupy:
    if element_w_liscie == "jablka":
        jabkla = element_w_liscie
print(jablka)

###drugi sposob iterowania - przeszukiwania
for index, element in enumerate(lista_produktow_na_zakupy):
    print(f"Element {index} to {element}")

# ########### listy mozemy indeksowac od konca
# print(lista_produktow_na_zakupy[-1])
#
#
# ###########updatowanie listy
# lista_produktow_na_zakupy[0] = "gruszki" #po takim wpisaniu on zamienia pierwsza pozycje "maka" na pozycje "gruszki" - przypisujemy mu nowa wartosc
# print(lista_produktow_na_zakupy)
#
# #######operacja usuniecia
# ##pierwszy sposob
# lista_produktow_na_zakupy.remove("gruszki") #funkcja .remove usuwa tylko pierwsza pozycje o danej nazwie z listy
# print(lista_produktow_na_zakupy)
#
# ##drugi sposob
# del lista_produktow_na_zakupy[0] #usuwa pozycje o danym indeksie (nie zawsze jest to bezpieczne bo nie zawsze wiemy o ilosci indeksow w liscie
# print(lista_produktow_na_zakupy)
#
# #aby usunac wiecej indeksow to robimy to w taki sposob
# del lista_produktow_na_zakupy[0], lista_produktow_na_zakupy[1] #tylko nalezy pamietac o tym ze python wykonuje wszystkie dziqlanai kolejno wiec w tym przypadku usunie 1 i 3 element z listy
# print(lista_produktow_na_zakupy)
#
#
#
# ######## sprawdzanie dlugosci listy (ilosci indeksow)
# print(len(lista_produktow_na_zakupy))
#
#
#
# ######## MUTOWALNOSC ZMIENNYCH - listy sa mutowalne - my nie zmienimy miejsca w pamieci tej naszej struktury
# # to jest to (id) zawsze bedzie takie samo bez wzgledu na to co zmienimy w tej liscie - id listy zawsze zostaje takie samo podczas pojedynczego dzialania programu
# lista_zakupyowa = ["jablka", "banany", "gruszki", "czeresnie"]
# print(id(lista_zakupyowa))
# lista_zakupyowa.append("maslo")
# print(lista_zakupyowa)
# print(id(lista_zakupyowa))
# lista_zakupyowa.insert(1, "kisiel")
# print(lista_zakupyowa)
# print(id(lista_zakupyowa))
#
#
# #tworzenie historii jako listy
# historia = ["Kupiłem 10kg maki", "sprzedalem fiata", "kupilem 2 kg jablek"]
# #jak sprawdzic historie od do - zeby liste pociac na mniejsze elementy trzeba zrobic to w taki sposob
# print(historia[1:2])
#
