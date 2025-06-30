# 2.
#       Mamy file_handler - i bedziemy musieli miec dwa pliki - <plik_wejscia> i <plik_wyjscia>. Nie zawsze plike wejsciowy
# bedzie tozsamy z plikiem wyjsciowym. Nie zawsze bedziemy chcieli do tego samego pliku zapisywac.
#       Musimy wobec tego napisac metode inicjalizujaca i przekazac dwie zmienne <input_file_path> i <output_file_path>
# To beda te wartosci ktore bedziemy otrzymywac w tym naszym transformie z tej bnaszej listy
#                   ['in.csv', 'out.csv', 'add,row,0,10', 'mult,col,1,3']
#                           czyli wartosci in.csv i out.csv
# importujemy modul csv

import csv


class FileHandler:
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.data = self.load_data()
        self.transformations = transformations  # 8. przechodzimy z matrix_transform.py i dodajemy na gorze kolejny
                                                # parametr <transformations> a tutaj dopisujemy ta linijke - nastepnie
                                                # przechodzimy do matrix_transform.py do punktu 9.

# nastepnie piszemy funkcje zby wgrac plik CSV

    def load_data(self):
        """Load data from a CSV file."""
        with open(self.input_file) as file:
            reader = csv.reader(file)


# tworzymy plik .csv
#       My bedziemy sobie dzialali na podstawie pliku .csv, wewnatrz pythona na macierzy - zeby stworzyc sobie macierz
# dwokierunkowa (mamy osie x i y - rzedy oraz kolumny)
# 1,2,3
# 4,5,6
# 7,8,9
# musimy zrobic sobie taka specyficzna strukture - listy w liscie - w pliku matrix_transform.py - przejdz do pliku
#                                   matrix_transform.py



# 4.
#       przechodziny z matrix_transform.py
#       Musimy w filehandlerze zapisac wartosci z pliki in.csv do tej naszej struktury - (lista w liscie za pomoca petli for)
# zeby to zrobic musimy zrobic sobie petle for

            temp_matrix = []
            for row in reader:
                temp_row = []
                for number in row:
                    temp_row.append(int(number))
                temp_matrix.append(temp_row)
        return temp_matrix

# Prechodzimy do matrix_transform.py zeby uruchomic

# 6. piszemy kolejna funkcje
    def save_data(self):
        with open (self.output_file, 'w+') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

# przechodziny do pliku matrix_transform.py do punktu 7.

# 10. Piszemy kolejna funkcje dla transformations - transformacji bedzie nieskonczenie wiele wiec aby odczytac je
# wszystkie po kolei powinnismy uzyc petli for


    def do_transformations(self):
        for transformation in self.transformations:
# przechodzimy do matrix_transform.py do punktu 11. i dodajemy prawie na koniec funkcje
#               <file_handler.do_transformations()>

# 12 kontynlujemy nasza funkcje - przy kazdej iteracji bedziemy otrzymywali string 'add,row,0,20' z tego stringa musimy
# wyciagnac kolejne kluczowe wartosci, ktore oddzielone sa przecinkiem i przypisac do zmiennych - zebysmy mogli to tak
# zrobic musimy najpierw przeksztalcic naszego stringa do tymczasowej struktury, potem z tej tymczasowej struktury
# przypisac te wartosci do zmiennych - najlepsza tymczasowa struktura bedzie lista - wiec zamieniamy string na liste

            transformation_list = transformation.split(",")
            operation = transformation_list[0]                  # nasze dodawanie
            axis = transformation_list[1]                       # podajemy os
            index = int(transformation_list[2])
            value = int(transformation_list[3])
# w zaleznosci od tego co my bedziemy chcieli zrobic np. <if operation == "add"> to bedziemy wykonywac inne metody
            if operation == "add":              # dodawanie
                if axis == "row":
                    self.add_row(index, value)
                elif axis == "col":
                    self.add_col(index, value)
            if operation == "mult":             # multiplikacja
                if axis == "row":
                    self.mult_row(index, value)
                elif axis == "col":
                    self.mult_col(index,value)
# teraz te metody bedziemy musieli napisac
    # dodawanie rzed
    def add_row(self, index, value):
        for position, item in enumerate(self.data[index]):
            self.data[index][position] += value

    # dodawanie columna
    def add_col(self, index, value):
        for row in self.data:
            row[index] += value

#nastepnie dopisujemy na gorze multiplikacje
    def mult_row(self, index, value):
        for position, item in enumerate(self.data[index]):
            self.data[index][position] *= value

    def mult_col(self, index, value):
        for row in self.data:
            row[index] *= value

# i teraz po uruchomieniu w pliku out.csv dostalismy zmienione wartosci