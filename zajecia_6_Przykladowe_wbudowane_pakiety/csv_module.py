import csv
import os
#przetwarzanie plikow excelowych
# uzywamy modulu os zeby przeniesc sie w miejsce gdzie plik csv istnieje

os.chdir('D:/szkolenia_wlasne/python/python_future_collars/013_Przykladowe_wbudowane_pakiety')

with open("lista_uczniow.csv") as file:
    reader = csv.reader(file, delimiter=',') # delimiter oznacza czym w pliku csv oddzielane sa komorki od siebie
    for row in  reader:
        print(row)


# stworzenie pliku z nowa lista
with open("lista_uczniow_002.csv", mode="a+") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Jan", "kowalski", "6A"])