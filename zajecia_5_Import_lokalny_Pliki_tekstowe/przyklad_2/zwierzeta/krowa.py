class Krowa:
    def __init__ (self, imie):
        self.imie = imie
        self.glos = "Muuu"
        self.wiek = 8
        self.waga = 250

    def __repr__(self):
        return f"Krowa {self.imie} ma {self.wiek} lat i wazy {self.waga} kg"
