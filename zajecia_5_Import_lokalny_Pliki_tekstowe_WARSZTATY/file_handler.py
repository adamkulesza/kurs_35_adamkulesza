import json

class FileHandler:
    def __init__(self, ksiegozbior_file, saldo_file, historia_file):
        self.ksiegozbior_file = ksiegozbior_file
        self.saldo_file = saldo_file
        self.historia_file = historia_file
        self.ksiegozbior = self.load_ksiegozbior_file()
        self.historia = self.load_history_file()
        self.saldo = self.load_saldo_file()
# """ w tym momencie zaznaczylismy na jakich plikach bedziemy dzialac - ale my ich jeszcze nie wczytalismy
# Wiec w tym momencie musimy je wczytac
# Wiec piszemy metode do otwierania tych naszych plikow - 3 METODY - dla kazdego pliku osobno"""
# """W metodzie zawsze musimy zrobic:
#     otworzyc
#     przetworzyc - abu zaimportowac modul .json trzeba zaimportowac modul json ktory ulatwi nam przetwarzanie plikow typu .json
#     zwrocic zawartosc pliku
# """

# 1 METODA
# to ponizej to jest otwieranie
    def load_ksiegozbior_file(self):
# to ponizej to jest przetwarzanie
        with open(self.ksiegozbior_file) as file:
            ksiegozbior = json.load(file)
# to ponizej to jest zwracanie zawartosci - aby zwrocic  zawartosc pliku musimy w naszej inicjalizacji dopisac
# self.ksiegozbior = self.load_ksiegozbior_file() a ponizej dopisac:
            return ksiegozbior

# 2 METODA
    def load_history_file(self):
        with open(self.historia_file) as file:
            historia = json.load(file)
            return historia

# 3 METODA
    def load_saldo_file(self):
        with open(self.saldo_file) as file:
            saldo = file.read().strip()
            return float(saldo)

# Zainicjowalismy te pliki i mamy te stan tych trzech plikow wewnatrz pliku file_handler.py
# Nastepnie importujemy obietk (plik) file_handler.py na sam poczatek pliku ksiegozbior.py piszemy
# from file_handler import file_handler

# a nastepnie pozaminiac w pliku ksiegozbior.py zawartosc:
# lista_ksiazek = file_handler.ksiegozbior
# saldo = file_handler.saldo
# historia = file_handler.historia

# nastepnie musimy wszystko zabezpieczyc - musimy pozapisywac sobie zmiany ktore zrobilismy
# mozemy zrobic to dwojako
# 1 rzecz, ktora musimy zrobic to zaimplementowac 3 metody kolejne wewnatrz tego naszego file handlera - zapisanie danych

    def save_ksiegozbior_file(self):
        with open(self.ksiegozbior_file, "w") as file:
            file.write(json.dumps(self.ksiegozbior, indent=4))

    def save_historia_file(self):
        with open(self.historia_file, "w") as file:
            file.write(json.dumps(self.historia, indent=4))

    def save_saldo_file(self):
        with open(self.saldo_file, "w") as file:
            file.write(str(self.saldo))

# 2 rzecz - Nastepnie aby zapisac ten nasz stan w momencie zamkniecia programu ksiegozbior.py musimy wykonac defakto 6 rzeczy
# - musimy byc pewni ze trzy wartosci w pliku file_handlet.ksiegozbior, file_handler.saldo i file_handler.historia sa takie same jak w pliku ksiegozbior.py
# wobec tego n akoncu pliku ksiegozbior.py piszemy
#       file_handler.ksiegozbior = lista_ksiazek
#       file_handler.saldo = saldo
#       file_handler.historia = historia
# (piszemy to w tym momencie bo wszystko zostanie zapisane kiedy caly program sie zamknie)

# Nastepnie definiujemy te nasz 3 metody dodajac
#       file_handler.save_ksiegozbior_file()
#       file_handler.save_saldo_file()
#       file_handler.save_historia_file()

file_handler = FileHandler("ksiegozbior.json", "saldo.txt", "historia.json")


# 2 punkt inaczej aby zrobic zzapisywanie na przyklad po kazdej operacji to zrobimy sobie funkcje w pliku file_handler.py

def save_temporary_data(file_handler, lista_ksiazek, saldo, historia):
    file_handler.ksiegozbior = lista_ksiazek
    file_handler.saldo = saldo
    file_handler.historia = historia
    file_handler.save_ksiegozbior_file()
    file_handler.save_saldo_file()
    file_handler.save_historia_file()

# w pliku ksiegozbior.py na gurze do importowanego pliku dopisujemy save_temporary_data - powinno to wygladac tak
#           from file_handler import file_handler, save_temporary_data

# nastepnie kiedy bedziemy cos dodawali do historii(historia.append) wpisujemy
#           save_temporary_data(file_handler, lista_ksiazek, saldo, historia)