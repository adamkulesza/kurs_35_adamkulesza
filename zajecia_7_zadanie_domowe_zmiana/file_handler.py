import json

class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.read_data_from_file()

    def read_data_from_file(self):
        try:
            with open(self.file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def write_data_to_file(self, new_data):
        city_name = list(new_data.keys())[0]
        date = list(new_data[city_name].keys())[0]
        pogoda = new_data[city_name][date]

        # Upewnij się, że miasto istnieje w danych
        if city_name not in self.data:
            self.data[city_name] = {}

        # Dodaj lub nadpisz prognozę dla daty
        self.data[city_name][date] = pogoda

        # Zapisz do pliku
        with open(self.file, "w") as file:
            json.dump(self.data, file, indent=4)

    def look_for_city_in_data(self, city_name, searched_date):
        city_name = city_name.capitalize()
        city_data = self.data.get(city_name)

        if city_data and searched_date in city_data:
            return {
                "city": city_name,
                "date": searched_date,
                "pogoda": city_data[searched_date]
            }

        return None