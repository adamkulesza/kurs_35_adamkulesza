user_list = [
    {
        "name": "Jan Kowalski",
        "age": 30,
        "email": "jan.kowalski@gmail.com",
        "address": "Warszawa, Polska",
        "zip_code": "00-001",
        "city": "Warszawa",
        "country": "Polska"
    },
    {
        "name": "Anna Nowak",
        "age": 25,
        "email": "anna.nowak@gmail.com",
        "address": "Krakow, Polska",
        "zip_code": "31-001",
        "city": "Krakow",
        "country": "Polska"
    },
    {
        "name": "Piotr Wisniewski",
        "age": 40,
        "email": "piotr.wisniewski@gmail.com",
        "address": "Wroclaw, Polska",
        "zip_code": "50-001",
        "city": "Wroclaw",
        "country": "Polska"
    }
]

# Znajdujemy Jana Kowalskiego i zmieniamy zip_code metodą __setitem__
for user in user_list:
    if user["name"] == input("Podaj imie jakie chcesz wyszukac w liscie: "):
        user.__setitem__("zip_code", input("Podaj zip_code, ktory chcesz zmienic dla podanej osoby (00-123): "))
        break  # opcjonalne, jeśli wiadomo że jest tylko jeden taki użytkownik

# Sprawdzenie efektu
print(user_list)  # lub print(user_list) dla całej listy