import random

# sluzy na generowania pseldolosowego jakich liczb wartosci
# np mozemy zasymulowac sobie jakis program LOTTO
# pseldo losowosc
for number in range(8):
    print(random.randint(1, 49))

print(random.choices([1, 2, 3, 4, 5, 6, 7, 8,], k=4))


print(random.choices(["Adam", "Andrzej", "Grzegorz", "Michal", "Krzysztof", "Ela", "Zbigniew"], k=4))


names_list = ["Adam", "Andrzej", "Grzegorz", "Michal", "Krzysztof", "Ela", "Zbigniew"]
for x in range(len(names_list)):
    selected_name = random.choices(names_list, k=1)
    print(selected_name[0])
    names_list.remove(selected_name[0])