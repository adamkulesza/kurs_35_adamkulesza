# 2.
# importujemy sobie biblioteke  json
# tworzymy sobie klase w pliku

import json

class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.read_data_from_file()

    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    # def write_data_to_file(self):
    #     with open(self.file, "w") as file:
    #         file.write(json.dumps(self.data, indent=4))


# przechodzimy do pliku <country selector> gdzie zaimportujemy sobie z pliku <file_handler>
# przejsdz na poczatek pliku <country_selector> gdzie znajdziesz punkt # 3.


# 5. w ostatnia funkcje zmieniamy  w nastepujacy sposob
# - dopisujemy parametr "new_data"

    def write_data_to_file(self, new_data):
        self.data.append(new_data)
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data, indent=4))

# Teraz gdy odpalamy plik <countries_selector> to widzimy, ze program powinien nam dzialac ale jeszcze nie dzialamy w
# trybie keszowania. Co musimy zrobic to musimy sprawdzic czy mamy ten kraj juz na naszej liscie - czy ktos sie juz o ten
# kraj pytał. Wobec tego musimy jeszcze tutaj dopisac.

    def lookup_for_country_in_data(self, country_name):
        for country in self.data:
            if country.get("full_name").lower() == country_name.lower():
                return country

# przechodzimy do punktu 6. w pliku <countries_selector>