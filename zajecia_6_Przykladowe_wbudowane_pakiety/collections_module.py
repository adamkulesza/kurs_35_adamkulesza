# biblioteka collections - ma w sobie kilka dodatkowych struktur danych oprocz tych podstawowych o ktorych mowilismy
# ma DefaultDict

from collections import defaultdict, Counter

# zliczanie ilosci wystepowania liter w tym stringu
very_long_string = "this is a very long string that we will use to demonstrate the DefaultDict function in Python."

counter_dict  ={}

# for letter in very_long_string:
#     if letter in counter_dict.keys():   # sprawdzamy czy taka literka (klucz) w naszym slowniku istnieje - jezeli istnieje
#                                         # to dodamy 1, jezeli nie istnieje to nie dodamy 1
#         counter_dict[letter] += 1
#     else:
#         counter_dict[letter] = 1
#
# print(counter_dict)


#       zeby nie robic tego <if> to mozemy uzyc <defoultdict>

defoult_counter_dict = defaultdict(int) # defoultdict domyslnie dopisuje do tej wartosci 0 (zero)

for letter in very_long_string:
    defoult_counter_dict[letter] += 1

print(defoult_counter_dict)


#       kolejna nasza strukturka do policzenia czegos jest strukturka <Counter>
# zamiast tej petli <for> mozemy zrobic takie cos

counter = Counter(very_long_string)
print(counter)