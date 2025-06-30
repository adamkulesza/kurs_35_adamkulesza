import csv
import json
import pickle
from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, input_file_path, output_file_path, zmiany=None):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.data = None
        self.zmiany = zmiany

    @abstractmethod
    def load_data(self):
        """Load data from the input file."""
        pass

    @abstractmethod
    def save_data(self):
        """Save data to the output file."""
        pass


    def do_zmiany(self):
        for zmiana in self.zmiany:
            zmiana_list = zmiana.split(",")
            row = int(zmiana_list[0])
            column = int(zmiana_list[1])
            value = zmiana_list[2]
            self.data[row][column] = value

class CsvFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            temp_matrix = []
            for row in reader:
                temp_row = []
                for number in row:
                    temp_row.append(number)
                temp_matrix.append(temp_row)
        return temp_matrix

    def save_data(self):
        with open (self.output_file, 'w+') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

class JsonFileHandler(FileHandler):
    def load_data(self):
        """Load data from a JASON file."""
        with open(self.input_file) as file:
            return json.load(file)

    def save_data(self):
        with open(self.output_file, "w+") as file:
            file.write(json.dumps(self.data, indent=4))

class TxtFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            temp_matrix = []
            for line in file:
                line = line.strip(', ')
                if line:
                    temp_matrix.append(line.split())  # Domyślnie dzieli po spacjach
        return temp_matrix

    def save_data(self):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            for row in self.data:
                file.write(', '.join(str(item) for item in row) + '\n')


class PickleFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'rb') as file:
            return pickle.load(file)

    def save_data(self):
        with open(self.output_file, 'wb') as file:
            file.write(pickle.dumps(self.data))