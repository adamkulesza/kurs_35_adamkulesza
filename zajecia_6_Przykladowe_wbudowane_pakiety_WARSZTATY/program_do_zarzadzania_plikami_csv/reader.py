"""
        Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i wyświetli w terminalu jego
zawartość, a na końcu zapisze w wybranej lokalizacji.

        Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

    <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
    <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
    <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0, natomiast
    "wartosc" zmianą która ma trafić na podane miejsce.

        Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.csv".

        Przykład działania:
python reader.py in.csv out.csv 0,0,gitara 1,3,kubek 2,1,17 3,3,0
Z pliku in.csv:
drzwi,3,7,0
kanapka,12,5,1
pedzel,22,34,5
plakat,czerwony,8,kij
Ma wyjść plik out.csv:
gitara,3,7,0
kanapka,12,5,kubek
pedzel,17,34,5
plakat,czerwony,8,0
"""

""""
[
    drzwi, 2, 7, 0
    kanapka, 12, 5, 1
    pedzel, 22,34, 5
    plakat, czerwony, 9, kij
]
"""

import sys
from file_handler import FileHandler

arguments = sys.argv[1:]
print(arguments)

# temp_matrix = [["drzwi", 2, 7, 0],
#                ["kanapka", 12, 5, 1],
#                ["pedzel", 22, 34, 5],
#                ["plakat", "czerwony", 9, "kij"]]
#
# value_1 = temp_matrix[0]

file_handler = FileHandler(input_file_path=arguments[0], output_file_path=arguments[1], zmiany=arguments[2:])
print(file_handler.data)
file_handler.do_zmiany()
file_handler.save_data()