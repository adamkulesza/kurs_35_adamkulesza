import csv


class FileHandler:
    def __init__(self, input_file_path, output_file_path, zmiany=None):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.data = self.load_data()
        self.zmiany = zmiany


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

    def do_zmiany(self):
        for zmiana in self.zmiany:
            zmiana_list = zmiana.split(",")
            row = int(zmiana_list[0])
            column = int(zmiana_list[1])
            value = zmiana_list[2]
            self.data[row][column] = value


