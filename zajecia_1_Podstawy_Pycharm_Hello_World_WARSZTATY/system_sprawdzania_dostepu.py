"""System sprawdzania dostępu

Wczytaj od użytkownika:
- wiek (liczba całkowita),
- hasło dostępu (tekst),
- czy jest pracownikiem firmy (tak/nie).

Stwórz zmienne:
- prawidlowy_wiek (wiek >= 18),
- haslo_poprawne (hasło == "admin123"),
- jest_pracownikiem (tak/nie).

Dostęp przyznaj jeśli: (pełnoletni i poprawne hasło) lub (jest pracownikiem).

Wyświetl:
- "Dostęp przyznany" lub "Dostęp zabroniony", bez użycia ifów."""

# wartosc_prawidlowa = True
# wartosc_falszywa = False

######################## pierwsze podejscie do aplikacji
# wiek_dostepu = 18
# haslo = "admin123"
# pracownik_firmy = "tak"
# pracownik_fitmy = pracownik_firmy.lower()
# wiek = input("Podaj wiek: ")
# haslo_dostepu = input("Podaj haslo dostepu: ")
# haslo_dostepu = haslo_dostepu.lower()
# pracownik = input("czy jest pracownikiem firmy (tak/nie): ")
# pracownik = pracownik.lower()
# print(int(wiek) >= wiek_dostepu)
# print(haslo == haslo_dostepu)
# print(pracownik_firmy == pracownik)

######################### drugie podejscie do aplikacji

wiek = int(input("Podaj swoj wiek: "))
prawidlowy_wiek = wiek >= 18

haslo = input("Podaj haslo: ")
haslo = haslo.lower() == "admin123"

pracowkik = input("Czy jestes pracownikiem? (tak/nie): ")
pracownik = pracowkik.lower() == "tak"

print(
    "Dostep przyznany" * (prawidlowy_wiek and haslo or pracownik)
    + "Dostep zabroniony" * (not pracownik)
)
