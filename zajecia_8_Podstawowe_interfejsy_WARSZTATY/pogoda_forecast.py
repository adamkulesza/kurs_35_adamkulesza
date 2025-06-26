from pogoda_forecast_file_handler import FileHandler

file_handler = FileHandler("data.json")

# print(file_handler.data)




# Metoda __getitem__
szczecin_info = file_handler["Szczecin", "2025-06-25"]
print(szczecin_info)




# Metoda __setitem__ - ta metoda dopisuje brakujace czesci slownika i nadpisuje jus istniejace czesci slownika
file_handler["Praga", "2025-06-27"] = "Bedzie padac"
# aby zapisac plik dopisujemy:
file_handler.write_to_file()




# generator items
my_generator = file_handler.items() # <items> taka jest nazwa tej funkcji w <pogoda_forecast_file_handler>

# po napisaniu tego - wyprintuje nam wszystko
for weather in my_generator:
    print(weather)

# a po napisaniu tego mozemy printowac poszczegolne linijki jedna po jednej - manualnie
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))




# iterator
for city, weather_info in file_handler:
    print(f"{city} - {weather_info}")