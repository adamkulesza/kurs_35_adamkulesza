from file_handler import FileHandler

file_handler = FileHandler("data.json")

olecko_info = file_handler["Olecko", "2025-06_25"]

print(olecko_info)