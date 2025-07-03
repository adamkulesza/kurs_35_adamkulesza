#                         zasada SOLID

# akronim od poszczegolnych liter tego wyrazu - kazda litera cos oznacza. Zacznijmy od:

# S - single responsibility - pojedyncza odpowiedzialnosc
# Mowi nam o tym, ze klasa lub funkcja powinna miec tylko i wylacznie jeden powod do zmiany, czyli powinna brac
# odpowiedzialnosc tylko za jedna rzecz

# O - open, close principle - Mowi nam ona, ze ten nasz kod powinien byc otwarty na rozszerzanie. Dzieki tej klasie
# abstrakcyjnej <DiscountStartegy> bedziemy mogli powiekszac nasz kod o kolejne dzieci ktore tutaj mamy.
# A zamkniety powinien byc na modyfikacje. Nie powinnismy pisac tego kodu w taki sposob ze zmieniamy jakis wartosci
# nieskonczenie wiele razy, lecz tylko po prostu bedziemy dodawali i rozszerzali to wszystkp.
# Te nasze programy powinny wygladac jak budowle z klockow.

# L - liskov substitution principle - # mowi o czyms bardzo podobnym poniewaz on nam mowi o tym, ze te obiekty klas
# potomnych one powinny byc wymienialne w miejsce klas bazowych bez zmiany poprawnosci dzialania programu. Czyli defakto
# te dzieci moga w 100% symulowac nam rodzicow.

# I - interface segregation principle - Ta zasada jest mocno powiazana z zasada liskov substytution. Poniewaz ona muwi
# tez nam o tym, ze nie powinnismy jako te klasy nadzredne zmuszac tych naszych klas podrzednych do implementowania
# jakichs metod.

# D - dependency inversion principle - zgodnie z zasada dependency inversion, zeby te nasze klasy ktore definiujemy
# nie zalezaly strikte od jakichs naszych implementacji, tylko zeby zalezaly od abstrakcji. Po to, zebysmy potem
# korzystajac z polimorfizmu mogli sobie dobudowywac to nie wplywajac juz na ten stan. Bo korzystajac z polimorfizmu, z
# liskov substytution mozemy dodawac sobie kolejne nasze zrodla swiatla.