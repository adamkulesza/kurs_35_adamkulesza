# S - single responsibility - pojedyncza odpowiedzialnosc
# Mowi nam o tym, ze klasa lub funkcja powinna miec tylko i wylacznie jeden powod do zmiany, czyli powinna brac
# odpowiedzialnosc tylko za jedna rzecz

# Nawiazujac do naszej firmy - mamy raport z calego dnia


# class Report:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# # mamy generowanie takiego raportu
#
#     def generate(self):
#         print("Generating report...")
#         print("Retriving data from users...")
#         print("Rormatting report content...")
#         return f"Report {self.title}\nContent: {self.content}"
#
# # zapisujemy do pliku
#
#     def save_to_file(self, filename):
#         with open(filename, "w") as file:
#             file.write(self.generator())


# Co sie dzieje w tej naszej klasie?
#   W tej naszej klasie mamy powiazane w tym raporcie dwie odpowiedzianosci. Mianowicie mamy powiazona dzialalnosc
# <generate> generowania raportow i mamy powiazana odpowiedzialnosc zapisywania jakichs danych do pliku. Dwie
# odpowiedzialnosci danej klasy.
#   Zamiast tego, zgodnie z zasada Single Responsibility, powinnismy rozbic sobie ten nasz kod na to zeby mial
# poszczegolne odpowiedzialnosci. Po co to robimy?
# Mamy klase <Report>, ktort cos generuje i cos zapisuje - jezeli bysmy mieli setki takich klas to zmiana formatu zapisu
# pliku wydluzyla by nam kod. A tak jezeli rozbijemy na klase <Report> i na klase <FileSaver> to zaoszczedzimy czas.

# Powinno to wygladac tak

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        print("Generating report...")
        print("Retriving data from users...")
        print("Rormatting report content...")
        return f"Report {self.title}\nContent: {self.content}"

class FileSaver:
    @staticmethod
    def save(filename, content):
        with open(filename, "w") as file:
            file.write(content)
        print(f"content save to {filename}")

# Starajmy sie to rozdzielac zeby laczyc to z mniejszych klockow.