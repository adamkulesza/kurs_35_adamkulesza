"""
Quiz wiedzy o podstawach pythona

Wczytaj odpowiedzi uzytkownika na 10 pytan
1. Typ liczby 5?
2. Typ wartosci 'Hello'
3. Czy zmienne maja okreslony typ przy deklaracji? (tak/nie)
4. Typ wyniku 5/2?
5 Typ wyniku 2+3?
6. Jak zapisac tekst z apostrofem ("I'm")? ('...' lub "...")
7. ktore wyrazenie daje True? (5>2)
8. Co oznacza operator %? (reszta/dzielenie/mnozenie)
9. Czy mozna zmienic typ zmiennej? (tak/nie)
10. Wynik True and False to True to True (tak/nie)

Policz punkty za poprawnosc odpowiedzi
Jesli >= 7 punktow - "Quiz zaliczony", w przeciwnym razie "Quiz niezaliczony"

bez uzycia ifow
"""

punktacja_uzytkownika = 0

#pytanie 1
odpowiedz = input("1. Typ liczby 5? (int/float): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "int")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#Pytanie 2
odpowiedz = input("2. Jaki to jest typ wastosci 'Hello'?: ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "string")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#Pytanie 3
odpowiedz = input("3. Czy zmienne maja okreslony typ przy deklaracji? (tak/nie): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "nie")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#Pytanie 4
odpowiedz = input("4. Jaki bedzie typ 5/2? (float/int): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "float")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#pytanie 5
odpowiedz = input("5. Typ wyniku 2+3? (float/int): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "int")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#pytanie 6
odpowiedz = input("6. Jak zapisac text z apostrofem ('I'am')? cudzyslow czy apostrof: " )
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "cudzyslow")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#pytanie 7
odpowiedz = input("7. Czy to wyrazenie daje True? (5>2)? (True/Folse): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "true")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#pytanie 8
odpowiedz = input("8. Co oznacza operator %? (reszta/dzielenie/mnozenie): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "reszta")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

#pytamie 9
odpowiedz = input("9. Czy mozna zmienic typ zmiennej? (tak/nie): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "tak")
print(f"Twoja punktacja to {punktacja_uzytkownika}/10")

# pytanie 10
odpowiedz = input("10. Wynik True and False to True (tak/nie): ")
punktacja_uzytkownika += 1 * (odpowiedz.lower() == "nie")

print(f"Twoja punktacja to {punktacja_uzytkownika}/10")
print("Quiz zaliczony!" * (punktacja_uzytkownika >= 7) + "Quiz niezaliczony" * (punktacja_uzytkownika < 7))