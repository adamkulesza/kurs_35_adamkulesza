class Pies:
    def __init__(self, imie):
       self.imie = imie

    def szczekaj(self):
        print(f"{self.imie} sczeka: Hau hau!")

    def __repr__(self):
        return f"Pies {self.imie}"