import os

print(os.getcwd()) # funkcja ktora pokaze w jakim aktualnie katalogu sie znajduje (get current working directory)
print(os.listdir()) # funkcja za pomoca ktorej wyswietlimy sobie co znajduje sie w katalogu w ktorym obecnie jestesmy
os.chdir('..') # funkcja za pomoca ktorej przechodzimy do folderu wyzej
print(os.getcwd())
print(os.listdir())
os.chdir('zajecia_6_Przykladowe_wbudowane_pakiety')
print(os.getcwd())
print(os.listdir())



# Gdzie stosujemy ten modul <os>???
# Stosujemy go:
# 1.
nazwa_pliku =input("Podaj nazwe pliku: ")
if os.path.exists(nazwa_pliku):
    print("Plik istnieje")

# 2.
print(os.path.join(os.getcwd(), nazwa_pliku)) # mozemy polaczyc <cwd> Current Working Directory z nazwe pliku z
                                            # wczesniejszego przykladu