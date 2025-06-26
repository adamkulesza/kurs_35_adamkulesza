import json

class FileHandler:
    def __init__ (self, file_path):
        self.file = file_path
        self.data = self.read_data_from_file()
        self.iterator = iter(self.data.items()) # dopisujemy to kiedy tworzymy iterator

    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)


# metoda __getitem__
    def __getitem__(self, item):
        city,date = item
        print(city)
        print(date)
        return self.data.get(city, {}).get(date, "Data not found")


# metoda __setitem__
    def __setitem__(self, key, value):
        city, date = key
        # sprawdzamy w pierwszej kolejnosci czy nasze miasto "Poznan" istnieje w naszej liscie
        if city in self.data.keys():
            self.data[city][date] = value
        else:
        # a nastepnie dodajemy brakujacy poznac do slownika
            self.data[city] = {}
            self.data[city][date] = value
        # zapisujemy plik
    def write_to_file(self):
        with open(self.file, 'w') as file:
            file.write(json.dumps(self.data, indent=4))


# generator item
    def items(self):
        for city, date in self.data.items(): #iterujemy sobie po naszym glownym slowniku - po calosci
            for date_value, weather_info in date.items():
                yield city, date_value, weather_info

# iterator
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)