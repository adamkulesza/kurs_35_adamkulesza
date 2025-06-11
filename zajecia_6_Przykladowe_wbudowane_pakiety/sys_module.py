#          MODUL SYSTEMOWY
# sluzy nam do operacji wejsc oraz wyjsc i do pobierania jakichs danych czy to z terminala czy to moze z jakichs plikow
# korzystajac z tych wewnetrznych modulow, tych bibliotek ktore sa juz dostepne na poziomie pythona - co bedziemy musieli
# robic zeby je wykorzystywac?? Bedziemy musieli je importowac tak samo jak musielismy importowac te nasze moduly te
# nasze pakiety i tutaj bedziemy musieli te nasze moduly czy tez biblioteki sobie importowac.

import sys

# print(sys.version) # mowi nam o wersji pythona
# print(sys.executable) # mowi nam o virtualnym srodowisku i interpreterze z ktorego korzystamy
# print(sys.path) # mowi gdzie sie znajdujemy


# argumenty - cos co wykorzystujemy
# argumenty ktore mozemy podawac w momencie kiedy bedziemy bedziemy wykonywali nasz kod pythonowy czy to z terminala,
# czy to z jakiegos innego, tak zebysmy nie musieli przekazywac informacje z inputa.
# Wiec jezeli bysmy chcieli sparametryzowac jakies nasze skrypty pythonowe, ktore mamy, mozemy je sparametryzowac poprzez
# podanie w terminalu argumentow systemowych, czyli wykonujac nasz program podajaz w terminalu
#      python sys_module.py 1,2 michal adam andrzej
# argumenty te <sys_module.py 1,2 michal adam andrzej> beda sie nam pojawialy wewnatrz listy
# powinnismy uzyskac taki rezultat
# ['sys_module.py', '1,2', 'michal', 'adam', 'andrzej']

# te argumenty ktorymi parametryzujemy ten nasz program pythonowy, one sie beda pojawialy od pierwszego argumentu.
# nalezy pamietac ze indeksujemy od indeksu <0> czyli od pierwszego argumentu. w ten sposob mozemy parametryzowac nasz
# kod pythonowy

# WAZNE jest to ze  poszczegolne elementy jezeli bysmy chcieli miec ich kilka to one beda od siebie oddzielane spacja
#        tak jak tu       python sys_module.py 1,2 michal adam andrzej


arguments = sys.argv
print(arguments)



# CIEKAWE - mamy tutaj zamienniki printa i inputa
# do modulu systemowego mamy dwie rzeczy:
# 1.
#   sys.stdin.readline() - ktory bedzie nam odpowiadal za pobieranie danych: czyli na przyklad jest to pobieranie z tego
# naszego terminala

x = sys.stdin.readline()
print(type(x))
print(x)
# Co jest fajnego w tym wszystkim to jest to ze mozemy te dane pobierac w tym module nie tylko ze standardowego naszego
# wejscia ale takze, nie tylko z naszej konsoli ale mozemy tez je pobierac na przyklad z plikow, czyli robic cos
# podobnego co robilismy z naszymi contekst managerami. Taka roznica miedzy tym naszym <input> a <stdin>

# 2.
# One beda pozwalaly nam na zapisywanie do plikow
sys.stdout.write("Hello World!\n")