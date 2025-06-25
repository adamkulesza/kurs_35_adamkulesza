"""
Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:

    Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. W przypadku
nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
    Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
    Istnieją trzy możliwe informacje dla opadów deszczu:
        Będzie padać (dla wyniku większego niż 0.0)
        Nie będzie padać (dla wyniku równego 0.0)
        Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
    Będzie padać
    Nie będzie padać
    Nie wiem
        Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania
        do API, tylko zwróć wynik z pliku.

URL do API:
https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}

W URL należy uzupełnić parametry: latitude, longitude oraz searched_date
"""

import requests
from file_handler import FileHandler


from geopy.geocoders import Nominatim
lokacja = input("Podaj miejsce dla ktorego chcesz sprawdzic pogode - pisownia angielska: ")
geolocator = Nominatim(user_agent="adamK_app")
location = geolocator.geocode(lokacja)
try:
    latitude = location.latitude
except (ValueError, NameError, AttributeError) as e:
    print("Taka lokacja nie istnieje - blad szerokosci geograficznej")
try:
    longitude = location.longitude
except (ValueError, NameError, AttributeError) as e:
    print("Taka lokacja nie istnieje - blad dlugosci geograficznej")
searched_date = input(f"Podaj date dla ktorej chcesz sprawdzic pogode (YYYY-mm-dd): ")


def get_data_from_pogoda_api(latitude, longitude, searched_date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    response = requests.get(url=url)
    print(url)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        print("Taka lokalizacja nie istnieje")

def modify_data_from_pogoda_api_to_our_dict(response_data):
    if not response_data:
        return {}

    pogoda_info = response_data

    result = {
        "location": lokacja,
        "searched_date": pogoda_info.get("daily", {}).get("time", [])[0],
        "opady_deszczu": pogoda_info.get("daily", {}).get("rain_sum", [])[0],
        "latitude": pogoda_info.get("latitude"),
        "longitude": pogoda_info.get("longitude")
    }
    opady = pogoda_info.get("daily", {}).get("rain_sum", [])[0]
    if opady == 0:
        print(f"Tego dnia bedzie slonecznie. Suma opadow wynosi {opady}mm")
    elif opady <= 0 or opady == []:
        print("Nie wiem jaka bedzie dzisiaj pogoda. Suma opadow jest nie znana.")
    else:
        print(f"Dzisiaj przewidywane opady. Suma opadow wynosi {opady}mm ")

    return result


try:
    file_handler = FileHandler(file_path="data.json")
# user_pogoda = input("Podaj miejsce dla ktorego chcesz sprawdzic pogode: ")

    if city_data := file_handler.look_for_city_in_data(lokacja, searched_date):
        print("Ta lokacja juz istnieje w liscie.")
        print(city_data)
    else:
        pogoda_info_from_api = get_data_from_pogoda_api(longitude, latitude, searched_date)
        modified_data = modify_data_from_pogoda_api_to_our_dict(pogoda_info_from_api)
        file_handler.write_data_to_file(modified_data)

    # pogoda = get_data_from_pogoda_api(latitude, longitude, searched_date)
    # print(modify_data_from_pogoda_api_to_our_dict(pogoda))
    # file_handler.data.append(modify_data_from_pogoda_api_to_our_dict(pogoda))
    # file_handler.write_data_to_file()

except (ValueError, NameError, AttributeError) as e:
    print("Ta lokalizacja nie istnieje - podaj inna nazwe, sprawdz angielska pisownie lub sprawdz poprawnosc daty, ktora podales.")