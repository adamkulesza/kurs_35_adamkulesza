"""Aby zaimportowac funkcje z pliku <math_operations robimy:
importy - chcemy zaimportowac nasz modul <math_operations.py>

jezeli ten modul znajduje sie w tym samym katalogu to mozemu zwyczajnie napisac"""

# import math_operations
"""teraz mamy zaimportowany caly modul <match_operations.py> ale tam jest w srodku funkcja dodawania i funkcja odejmowania i
nie wiemy jeszcze gdzie np. dodawanie sie znajduje i aby okreslic jaka funkcje chcemy uzyc z naszego zaimportowanego
pliku musimy wpisac """

# print(math_operations.dodawanie(4, 5))
# print(math_operations.odejmowanie(25, 10))

"""Nie zawsze bedziemy chcieli importowac cale pliki - z plikow (modulow) mozemy importowac poszczegolne rzeczy
- moga to byc klasy, funkcje, zmienne - musza to byc obiekty w pythonie"""

from math_operations import dodawanie
from math_operations import * #ta gwiazdka powoduje ze wszystko z modulu <math_operations.py> zostanie zaimportowane
#                               ale wowczas jezeli mamy wczesniej jakis pojedynczy import z tego pliku to on przestanie dzialac



"""ALIAS - wowczas mozemy nadawac "ALIASY"" danym modulom - kiedy Aliasy maja sens - kiedy mamy dwa moduly z roznych katalogow o tej samej nazwie
wowczas trzeba nadac ALIAS zeby uzyskac unikatowe nazwy modulow"""
import zwierzeta as animals

pies = animals.Pies("Burek")
pies.szczekaj()


print(dodawanie(1,8))
print(odejmowanie(25, 13))

"""kiedy w tej chwili bede chcial zrobic odejmowanie to wyskoczy mi blad bo w tej chwili zaimportowalismy tylko dodawanie
Aby zaimportowac wiecej rzeczy z jednego modulu(pliku .py) to po przecinku dodajemy kolejna nazwe funkcji
(patrz powyzej, aby zaimportowac jednoczesnie dodawanie i odejmowanie kazda kolejna wpisujemy po przecinku"""



""""PROBLEMY!!!!!!!!!!!!!

- unikamy zapetlonego importowania np:
A do B
B do C
C do A
powstaje nam wtedy petla przy importowaniu co wurzuca nam blad"""


"""UNIKAC NADPISYWANIA za pomoca innych plikow importowanych - moze do tego dojsc na przyklad kiedy importujemy jeden
plik o tej samej nazwie a nastepnie importujemy inny plik o tej samej nazwie - wowczas pierwszy plik zostanie nadpisany!!!!!!!!!!!!"""
