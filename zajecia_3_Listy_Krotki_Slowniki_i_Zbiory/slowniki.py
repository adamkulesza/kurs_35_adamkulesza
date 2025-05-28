#####Slowniki
## slownik sluzy do okreslania i opisywania jakichs naszych zmiennych, dawania dodatkowych informacji/podpowiedzi czym ta nasza zmienna jest
## slownik jest struktura <klucz oraz wartosc>
## klucze w naszych slownikach musza miec okreslony typ bo musza byc unikalne

uzytkownik = {
    # "klucz": "wartosc",
    "imie": "Michal",
    "nazwisko": "zietkowski",
    "wiek": 20,
    "czy_uczen": True,
}

## klucze w naszych slownikach musza miec okreslony typ bo musza byc UNIKALNE
# i na przyklad po dodaniu kolejnego klucza "imie": "Adam", wczesniejszy klucz o nazwie "imie": "Michal", zostanie zastapiony przez klucz "imie": "Adam",
# jak zachowac ta unikalnosc?? - te struktury ktore moga byc kluczami moga byc tylko NIEMUTOWALNE i haszowalna.

uzytkownik_1 = {
    # "klucz": "wartosc",
    "imie": "Michal",
    "nazwisko": "Zietkowski",
    "wiek": 20,
    "czy_uczen": True,
    "imie": "Adam",
}
print(uzytkownik_1)


##### jak pobierac wartosci ze slownika??? - wpisujac odpowiedni klucz - jezeli wpiszemy nieistniejacy klucz to wyskoczy nam KeyError
uzytkownik_1["nazwisko"]
print(uzytkownik_1["nazwisko"])

## sposob zeby poznac liste kluczy - REKOMENDOWANY - po wpisaniu nieistniejacego klucza dostajemy informacje <None>
print(uzytkownik_1.get("plec"))

## sposob zeby poznac lise kluczy - mozna iterowac
for element in uzytkownik_1:
    print(element)

## operacja dodawania <kluczy> i <wartosci kluczy> - nowy klucz jest dodawany na koncu slownika
# klucz      wartosc klucza
uzytkownik_1["plec"] = "mezczyzna"
print(uzytkownik_1)

## updatowanie - zmiana wartosci danego klucza
uzytkownik_1["plec"] = "kobieta"
print(uzytkownik_1)

## usuwanie pary klucz-wartosc z naszego slownika
del uzytkownik_1["plec"]
print(uzytkownik_1)

uzytkownik_1.pop("imie")
print(uzytkownik_1)


##################iteracje w slownikach
for item in uzytkownik_1:  # poznajemy nazwy kluczy
    print(item)

for key in uzytkownik_1.keys():  # poznajemy nazwy kluczy
    print(key)

for value in uzytkownik_1.values():  # poznajemy wartosc kluczy
    print(value)

for key, value in uzytkownik_1.items():  # poznajemy zarowno klucz jak i wartosc
    print(f"{key}: {value}")


# ##### sprawdzanie czy jest taki klucz za pomoca <if>
#
# if "mieszkanie" in uzytkownik_1:
#     print("Taki klucz istnieje")
# else:
#     print("Nie ma takiego klucza")

# # lub mozemy sprawdzajac takie klucze usuwac tez je jezeli istnieja
# if "wiek" in uzytkownik_1:
#     del uzytkownik_1["wiek"]
#     print("Klucz 'wiek' zostal usuniety")
# else:
#     print("Nie ma takiego klucza")
# print(uzytkownik_1)
