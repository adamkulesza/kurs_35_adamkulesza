########## ZBIORY
zbior_kolorow = {"czerwony", "zielony", "zolty", "niebieski"}

## w zbiorach mozemy miec wartosci roznego typu - string, intiger, float, true/false, tuple/krotki (wszystkie ktore sa haszowalne)
zbior_rozny = {"czerwony", 222, False, 25.6, ("Adam", "Kowalski")}

## zbiory sa NIEMUTOWALNE
print(zbior_kolorow)
print(id(zbior_kolorow))
zbior_kolorow.add("czarny")
print(zbior_kolorow)
print(id(zbior_kolorow))
print(zbior_kolorow)

## zbior nie jest indeksowalny - nie jestesmy w stanie poznac indeksu danego obiektu w zbiorze

## zbiory sa UNIKALNE - czyli jezeli dodajemy cos co juz istnieje w zbiorze to nie zostanie wrzucony tam po raz drugi
## bo zbiory i wartosci w zbiorach musza byc haszowalne
## aby dodac cos yzywamy funkcji <.add> - po kazdym uruchomieniu kolejnosc jest przypadkowa
zbior_kolorow.add("zielony")
print(zbior_kolorow)

##aby usunac cos uzywamy funkcji <.remove>
zbior_kolorow.remove("niebieski")
print(zbior_kolorow)

## elementy sa dodawane w przypadkowe miejsca w zbiorze
zbior_kolorow.add("fioletowy")
print(zbior_kolorow)

## sa iterowalne - lecz przy kazdym uruchomieniu kolejnos jest przypadkowa
for element in zbior_kolorow:
    print(element)

### Castowanie ze zbioru na liste
### zmaiana naszego zbioru na liste - pamietamy o kolejnosci wykonywania dzialan wiec nasza lista bedzie miala taka forme jak wygladala nasza ostatnia wersja zbioru
lista_kolorow = list(zbior_kolorow)
print(lista_kolorow)
