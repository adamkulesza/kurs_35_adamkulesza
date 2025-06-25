# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Jest problem z metodami Magicznymi!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Metody magiczne to sa tylko i wylacznie metody ktore sa juz dostepne domyslnie w podstawowej implementacji Pythona i
# maja swoje specyficzne nazwy - nazywnictwo jest z gory sprecyzowane do danej metody magicznej.

user_list = [{
        "name": "Jan Kowalski",
        "age": 30,
        "email": "jan.kowalski@gmail.com",
        "address": "Warszawa, Polska",
        "zip_code": "00-001",
        "city": "Warszawa",
        "country": "Polska",
        "oceny": {
            "math": 5,
            "english": 4,
            "historia": 3
        }
    },
    {
        "name": "Anna Nowak",
        "age": 25,
        "email": "anna.nowak@gmail.com",
        "address": "Krakow, Polska",
        "zip_code": "31-001",
        "city": "Krakow",
        "country": "Polska",
        "oceny": {
            "math": 5,
            "english": 4,
            "historia": 3
        }
    },
    {
        "name": "Piotr Wisniewski",
        "age": 40,
        "email": "piotr.wisniewski@gmail.com",
        "address": "Wroclaw, Polska",
        "zip_code": "50-001",
        "city": "Wroclaw",
        "country": "Polska",
        "oceny": {
            "math": 5,
            "english": 4,
            "historia": 3
        }
}]



# #                      Metoda __str__
# # pozwala na wykastowanie uzytkownikow na typ stringowy
#
# class Users:
#     def __init__(self, users):
#         self.uzytkownik = users
#
#     def __str__(self):
#         return f"Users({self.uzytkownik})"
#
# user_print = Users(user_list)
# print(str(user_print))





# #                           Metoda __int__
# # metoda ktora podaje nam liczbe uzytkownikow
#
# class Users:
#     def __init__(self, users):
#         self.uzytkownik = users
#
#     def __int__(self):
#         return len(self.uzytkownik)
# user_print = Users(user_list)
# print(int(user_print))





# # #                           Metoda __getitem__
# # # wyszukiwanie po <name>
#
# class Users:
#     def __init__(self, users):
#         self.uzytkownik = users
#
#     def __getitem__(self, name):
#         for user in self.uzytkownik:
#             if user["name"] == name:
#                 return user
#         raise KeyError(f"Uzytkownik ktory nazywa sie {name} nie znaleziony w liscie.")
#
# # Tworzenie instancji
# user_print = Users(user_list)
#
# # Pobieranie Jana Kowalskiego
# osoba = user_print[input("Podaj imie i nazwisko osoby, ktora chcesz sprawdzic, czy znajduje sie na liscie: ")]
# print(osoba)




# #                           Metoda __getitem__
# # Wyszukiwanie po indeksach
# #
# # Jesli chcesz by twoja klasa zachowywala sie jak lista (czyli pozwalala na <user[0}, user[1], itd) mozesz zrobic to w
# # taki sposob:
#
# class Users:
#     def __init__(self, users):
#         self.uzytkownik = users
#
#     def __getitem__(self, index):
#         return self.uzytkownik[index]
#
# # Tworzenie instancji
# user_print = Users(user_list)
#
# # ale wtedy musimy znac index "Jana Kowalskiego
# numer_index = input("Podaj indeks, ktory posiada dana osoba w liscie (0, 1, 2, 3...]: ")
# numer_int = int(numer_index)
# print(user_print[numer_int])



#                           Metoda __setitem__
#
# Znajdujemy Jana kowalskiego i zmieniamy zip_code metoda __setitem__

for user in user_list:
    if user["name"] == input("Podaj imie jakie chcesz wyszukac w liscie: "):
        user.__setitem__("zip_code", input("Podaj zip_code, ktory chcesz zmienic dla podanej osoby (00-123): "))
        break  # opcjonalne, jeśli wiadomo że jest tylko jeden taki użytkownik

# Sprawdzenie efektu
print(user_list)  # lub print(user_list) dla całej listy