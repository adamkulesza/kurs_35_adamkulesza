"""Treść zadania

Napisz program śledzący czas ćwiczeń na siłowni.

Działanie programu:

    Program pyta o planowany czas treningu (w minutach).

    Następnie w pętli pobiera kolejne czasy poszczególnych ćwiczeń (w minutach).

    Każde ćwiczenie musi mieć czas od 5 do 45 minut.

    Jeśli podany czas jest spoza zakresu, program kończy wprowadzanie.

    Suma czasów ćwiczeń nie może przekroczyć 150% planowanego czasu treningu - jeśli dodanie kolejnego ćwiczenia przekracza ten limit, program kończy wprowadzanie.

    Na koniec program wyświetla:

        Łączny czas ćwiczeń,

        Procent wykorzystania planu,

        Liczbę ćwiczeń trwających dłużej niż 15 minut,

        Najdłuższe pojedyncze ćwiczenie.

Przykłady

Przykład 1:

text
Plan: 60 minut
Czasy: 30, 35, 25 (przekroczenie limitu)

Podsumowanie:
Łączny czas ćwiczeń: 90 minut
Procent wykorzystania planu: 150.00%
Ćwiczenia >15 min: 3
Najdłuższe ćwiczenie: 35 minut

Przykład 2:

text
Plan: 45 minut
Czasy: 10, 15, 20

Podsumowanie:
Łączny czas ćwiczeń: 45 minut
Procent wykorzystania planu: 100.00%
Ćwiczenia >15 min: 1
Najdłuższe ćwiczenie: 20 minut

Przykład 3:

text
Plan: 30 minut
Czasy: 25, 50 (błąd)

Podsumowanie:
Łączny czas ćwiczeń: 25 minut
Procent wykorzystania planu: 83.33%
Ćwiczenia >15 min: 1
Najdłuższe ćwiczenie: 25 minut

+++++++++++++++++++++++++++++++++++++++++++++++
input: #001 czas treningu
        #002 czas poszczegolnego cwiczenia
        #003 Laczny czas cwiczenia ( prawdziwy_czas_treningu )
        #004 Procent wykorzystania planu
        #005 Cwiczenia powyzej 15 minut
        #006 Najdluzsze cwiczenie
        #007 Restrykcja - Kazde cwiczenie musi miec czas od 5 do 45 minut - jesli czas jest z poza zakresu to program konczy wprowadzanie
        #008  Suma czasów ćwiczeń nie może przekroczyć 150% planowanego czasu treningu - jeśli dodanie kolejnego ćwiczenia przekracza ten limit, program kończy wprowadzanie.
"""

czas_treningu = int(input("Podaj planowany czas treningu (w minutach): ")) #001

prawdziwy_czas_treningu = 0 #003_001 - na poczatku kiedy zaczynamy cwiczyc to prawdziwy czas treningu zawsze jest zero
cwiczenia_powyzej_15_min = 0 #005
najdluzsze_cwiczenie = 0 #006
while True: #002 Czas cwiczenia - nie wiem ile razy bedziemy pytali i nie wiem ile czasu bedzie wpisywane
    czas_cwiczenia = input("podaj czas cwiczenia w minutach: ") #002
    if czas_cwiczenia:  #003_002 wyjscie z nieskonconej petli - ten zapis to jest to samo co ten zapis -  if czas_cwiczenia != "": (if czas_cwiczenia jest rozny od False wowczas przechodzimy do tej instrukcji czyli nasza instrukcja zatrzyma sie kiedy nacisniemy ENTER wowczas pojdzie do else: break- a Famse) dzieki temu po nacisniecu ENTER konczymy wpisywanie czasu cwiczen
        czas_cwiczenia = int(czas_cwiczenia) #003_002 wyjscie z nieskonconej petli
        if czas_cwiczenia > 45 or czas_cwiczenia < 5: #007
            break #007
        if prawdziwy_czas_treningu + czas_cwiczenia > 1.5 * czas_treningu: #008
            break #008
        if czas_cwiczenia > 15: #005
            cwiczenia_powyzej_15_min += 1 #005
        if czas_cwiczenia > najdluzsze_cwiczenie: #006
            najdluzsze_cwiczenie = czas_cwiczenia #006
    else: #003_002 wyjscie z nieskonconej petli
        break #003_002 wyjscie z nieskonconej petli
    prawdziwy_czas_treningu += czas_cwiczenia # 003_001 dodajemy do siebie kazde cwiczenie aby poznac - trafilismy na infinit loop i musimy zrobic wyjscie z tej  nieskonczonej petli
print(f"Czas trwania treningu: {prawdziwy_czas_treningu} minut") #003_003 - printujemy prawdziwy czas treningu
print(f"Wykorzystalismy {(prawdziwy_czas_treningu/czas_treningu) * 100} % planu") #004 Procent wykorzystania planu
print(f"Liczba cwiczen powyzej 15 minut wynosi: {cwiczenia_powyzej_15_min}") #005
print(f"Najdluzsze cwiczenie: {najdluzsze_cwiczenie} minut") #006