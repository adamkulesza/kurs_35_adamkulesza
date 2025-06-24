# import datetime
#
#
# lokacja = input("Podaj miejsce dla ktorego chcesz sprawdzic pogode: ")
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="adamK_app")
# location = geolocator.geocode(lokacja)
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)
#
# data_pogody = input(f"Podaj date dla ktorej chcesz sprawdzic pogode (YYYY-mm-dd): ")
#
# jutro = (datetime.datetime.now() + datetime.timedelta(days=1))
# data_pogody_jutro = jutro.date().isoformat()
# print(data_pogody_jutro)

data = [
    {
        "searched_date": ["2025-06-23"],
        "opady_deszczu OLECKO": [0.0],
        "latitude": 22.5,
        "longitude": 54.0
    },
    {
        "searched_date": ["2025-06-23"],
        "opady_deszczu WARSZAWA": [0.0],
        "latitude": 21.125,
        "longitude": 52.25
    }
]

# Wartości do sprawdzenia
target_date = "2025-06-23"
target_lat = 22.5
target_lon = 54.0

# Sprawdzenie, czy istnieje taki wpis
exists = any(
    target_date in entry.get("searched_date", []) and
    entry.get("latitude") == target_lat and
    entry.get("longitude") == target_lon
    for entry in data
)

print("Wpis już istnieje:", exists)