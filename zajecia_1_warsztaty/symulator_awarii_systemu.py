"""
Symulator awarii systemu

Wczytaj od uzytkownika
- czy serwer odpowiada (tak/nie)
- czy baza danych działa (tak/nie)
- czy aplikacja webowa jest dostepna (tak/nie)

Awaria:
- Krytyczna: serwer nie dziala i baza nie dziala
- czesciowa: serwer lub baza lub aplikacja nie dziala

Wyswietl:
- "Natychmiastowa interwencja!"
- "Awaria czesciowa - sprawdz system"
- "System dziala poprawnie"
"""

################# moja aplikacja ########################
serwer = input("Czy serwer dziala? (tak/nie): ")
serwer = serwer.lower()
serwer_dziala = serwer == "tak"

baza_danych = input("Czy baza danych działa? (tak/nie): ")
baza_danych = baza_danych.lower()
baza_danych_dziala = baza_danych == "tak"

aplikacja_web = input("Czy aplikacja webowa dziala? (tak/nie): ")
aplikacja_web = aplikacja_web.lower()
aplikacja_web_dziala = aplikacja_web == "tak"

# print("Awaria Krytyczna" * (not serwer_dziala and not baza_danych_dziala) + "Awaria czesciowa" * (not serwer_dziala or not baza_danych_dziala or not aplikacja_web_dziala))

print("Natychmiastowa interwencja - Awaria Krytyczna" * (not serwer_dziala and not baza_danych_dziala)
      or "Awaria czesciowa - sprawdz system" * (not serwer_dziala or not baza_danych_dziala or not aplikacja_web_dziala)
      + "System dziala poprawnie" * (serwer_dziala and baza_danych_dziala and aplikacja_web_dziala))


######### instruktor w cwiczeniu troche pomieszal za bardzo ##########