#Krotki sa po to zeby ograniczyc mozliwosc jakiejs modyfikacji dla uzytkownika

####podstawowa struktura krotki
##pierwszy sposob robienia tuple/krotki
imiona = ("Jan", "Anna", "Tomasz", "Przemek", "Piotr", "Ewa")
print(type(imiona)) #aby poznac typ danej wartosci uzywamy funkcji <type>
print(id(imiona))
##### tuple sa tez indeksowalne
print(imiona[0]) #chcemy poznac wartosc indeksu [0] - wartosc indeksu [0] naszego tupla to "jan"

##drugi sposob robienie krotek
plcie = "mezczyzna", "kobieta"
print(plcie)

##trzeci sposob
another_tuple = tuple(("Michal", "Grzegorz"))
print(another_tuple)


#####CZYM SIE ROZNIA TUPLE/KROTKI OD LIST???????????????
## tuple sa NIEMUTOWALNE - co za tym idzie eliminuje to nam mozliwosc wykonywania jakichkolwiek operacji .appendowania, .insertowani, usuwania, czy tez modyfikacji
## mozna wpisac rozne typy wartosci
## mozemy je odczytac
print(imiona)

## mozemy iterowac po nich
for imie in imiona:
    imie += " Cebula "
    print(imie)

for index, imie in enumerate(imiona):
    print(f"Element {index} to {imie}")