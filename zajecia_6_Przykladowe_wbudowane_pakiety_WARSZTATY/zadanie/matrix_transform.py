"""
**Zadanie: Transformacja Macierzy**
Napisz program, ktory przetworzy plik CSV zaierajacy tablice liczb i zastosuje serie transformacji okreslonych przez
uzytkownika. Program powinien odczytywac pliki wejsciowy, zastosowac zadane transformacje, a nastepnie zapisac go do
zadanego pliku wyjsciowego.
Uruchomienie pliku przez terminal:
python matrix_transform.py <plik wejsciowy> <plik_wyjsciowy> <transform_1> <transform_2> ... <transform_n>
- <plik_wejsciowy> - nazwa pliku, z ktorego odczytane zostana dane, np. data.csv
- <plik_wyjsciowy> - nazwa pliku, do ktorego zostanie zapisany wynik, np. result.csv
- <transformacja_x. - Transformacja w postaci "operacja, parametry" - operacja moze byc np. 'add', 'mult', 'div', a
parametry beda okreslaly wartosc do zastosowania transformacji (np. dla 'add' beda to wartoasci dodane dla kazdej komorki
w danej kolumnie lub wierszu).
Operacje transformacji:
- add,row,index,value - Dodaje wartosc do kazdego elementu w wierszu o zadanym indeksie.
- add,col,index,value - Dodaje wartosc do kazdego elementu w kolumnie o zadanym indeksie.
- mul,row,index,value - Pomnoz kazdy element w wierszu przez wartosc.
- mul,col,index,value - Pomnoz kazdy element w kolumnie przez wartosc.
"""

import sys
from file_handler import FileHandler
arguments = sys.argv[1:]

# 1.
# dzieki temu mozemy wyeksportowac argumenty ktore wpiszemy w terminalu <python matrix_transform.py 123k jdsfd i0i123 3422k>
# dzieki temu w terminalu pojawia sie nam te argumenty w takiej postacie ['matrix_transform.py', '123k', 'jdsfd', 'i0i123', '3422k']
# Pierwszy argument ,matrix_transform.py, jest nam nie potrzebny wiec aby go pominad dopisujemy na gorze [1:]
#                   arguments = sys.argv[1:]
# teraz po wpisaniu w terminalu <python matrix_transform.py 123k jdsfd i0i123 3422k> otrzymalismy
#                   ['123k', 'jdsfd', 'i0i123', '3422k']
print(arguments)

#       Zebysmy mogli uruchamiac plik z poziomu terminala i zebysmy nadal i zebysmy mieli te nasze poszczegolne parametry to
# musimy wejsc w nazwe pliku (prawy gorny rog pycharma) i przejsc w <Edit Configurations...> nastepnie te parametry
# ktore potrzebujemy wpisujemy w pole Script parameters <in.csv out.csv add,row,0,10 mult,col,1,3>
# teraz po uruchomieniu trojkacikiem automatycznie w terminalu wyswietlaja sie te nasze parametry.
#       Wszystkie te wartosci w naszej liscie beda od siebie odseparowane w tej naszej liscie za pomoca przecinka i spacji
# jezeli wpiszemy je w polu script parameters ze spacja - musimy miec spacje zeby miec osobne wartosci w tej naszej liscie

#       Mamy argumenty pobrane. Nastepnym krokiem bedzie napisanie obslugi tego pliku - plik file_handler.py -> przejdz
# do file_handler.py


# # 3. Tlumaczenie jak zrobic liste w liscie ( nie wykorzystujemy tego potem w filehandlerze - jest to tylko do zrozumienia!!!!!!!!!!
# # przeszlismy z pliku file_handler.py
# # tworzymy listy w liscie
#
# temp_matrix = [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]]
#
# # teraz jak juz mamy nasz plik .csv - nasza macierz zapisana jako listy w liscie zeby dostac sie do tej 1 musimy napisac
# # pierwsza wartosc w nawiasie to jest rzad - druga wartosc w nawiasie to jest kolumna
# value_1 = temp_matrix[0]
#
# # Musimy w filehandlerze zapisac wartosci z pliki in.csv do tej naszej struktury
# # przechodzimy do pliku file_handler.py


# 5. przeszlismy z file handlera z punktu 4
# na gorze wpisujemy <from file_handler import FileHandler>
# a na dole pliku piszemy <     file_handler = FileHandler(input_file_path=arguments[0], output_file_path=arguments[1])
#                               print(file_handler.data)>
# nastepnie przechodzimy do file_handler.py do punktu 6. aby napisac kolejna funkcje

file_handler = FileHandler(input_file_path=arguments[0], output_file_path=arguments[1], transformations=arguments[2:])
print(file_handler.data)
file_handler.do_transformations() # 11. dodajemy ta funkcje a nastepnie przechodzimy do file_handler.py do punktu 12.
# 7. dopisujemy na koniec

file_handler.save_data()

# I juz mamy odczytywanie i zapisywanie plikow
# Teraz musimy zrobic te nasze operacje
# W tej chwili mamy dwie funkcje do odczytu i do zapisu. i teraz operacje ktore mamy w naszych argumentach
# (na gorze 3 i 4 linijka) przekazac do file_handler.py - jak to zrobic?? - musimy to miec w klasie FileHandler przekazac jako kolejny parametr
# Przechodzimy do pliku file_handler_py do punktu 8. i dodajemy <transformations>
#   def __int__(self, input_file_path, output_file_path, transformations):
#       self.taransformations = transformations

# 9. dopisujemy parametr <transformations=arguments[2:]> do file handlera - linijka ma wygladac tak
# <file_handler = FileHandler(input_file_path=arguments[0], output_file_path=arguments[1], transformations=arguments[2:])>
# przechodzimy do file_hendler.py do punktu 10 i piszemy 3 funkcje