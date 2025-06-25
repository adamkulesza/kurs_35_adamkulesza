import json


class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.read_data_from_file()

    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    def __getitem__(self, item):
        city, date = item
        print(city)
        print(date)
        return self.data.get(city, {}).get(date, "Data not found")



    def write_data_to_file(self, new_data):
        self.data.append(new_data)
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data, indent=4))

    def look_for_city_in_data(self, city_name,  searched_date):
        for city in self.data:
            if city.get("location").lower() == city_name.lower():
                if searched_date in city.get("searched_date"):
                    return city



