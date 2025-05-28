#tworzymy dwie funkcje
#dodawanie
"""Funkcja dodaje dwie liczby"""
def dodawanie(liczba_1, liczba_2):
    return liczba_1 + liczba_2

#odejmowanie
"""Funkcja odejmuje dwie liczby"""
def odejmowanie(liczba_1, liczba_2):
    return liczba_1-liczba_2

# print(dodawanie(1, 5))
# print(odejmowanie(7, 3))

#Co zrobic aby moza bylo te dwie funkcje uzywac w pliku <main>?
"""Zebysmy mogli w pelni korzystac i rozdzielac sobie ten kod pythonowy na poszczegolne moduly (pliki .py), na poszczegolne pakiety, co zaraz zrobimy,
i robic to jakos sensownie, musimy skorzystac z czegos takiego jak importy - musimy to zaimportowac, dodac do tego pliku, tak zeby ten plik wiedzial,
ze z tego i z tego pliku uzywamy takich i takich funkcji, takich klas, moze takich zmiennych
Jak takie importy sie dodaje????

Importow mozemy miec kilka rodzai - na ten moment bedziemy stosowali importy globalne - to znaczy ze beda sie one znajdowaly zawsze na poczatku naszego pliku i
one beda zaimportowane do calego pliku a nie tylko do wycinku kodu.

->>>>> przejdz do pliku <main>"""