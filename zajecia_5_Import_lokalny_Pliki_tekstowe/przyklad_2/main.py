"""Tworzymy <python pakage> automatycznie tworzy sie tam nam plik <__init__.py>
ten plik robi super rzecz
<__init__> jest to plik inicjujacy nasz pakiet, ktory bedzie sie wykonywal w momencie uruchomienia naszego programu jako pierwszy"""
"""dzieki wpisowi w pliku <__init__.py> mozemu zaimportowac w taki sposob"""

####To sa importy NIERELATYWNE/BEZWZGLEDNE bezposrednio z tego samego katalogu gdzie znajduje sie plik main - z glownego katalogu
# from zwierzeta.pies import Pies
# from zwierzeta.krowa import Krowa
from zajecia_5_Import_lokalny_Pliki_tekstowe.przyklad_1.math_operations import dodawanie

"""IMPORT PO WPISIE W PLIKU <__init__.py"""
from zwierzeta import Krowa, Pies


krowa = Krowa("Marta")
print(krowa)

pies = Pies("Burek")
print(pies)

print(dodawanie(12, 68))
"""importy NIERELATYWNE/BEZWZGLEDNE - czyli takie gdzie podajemy cala sciezke dostepu"""



