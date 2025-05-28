lista_lotow = "Lo123, Lo456"

# zeby przekastowac tego stringa do listy to
#                   to usuwa nam spacje w stringu        dzieki temu okreslamy po czym chcemy dzielic (po przecinku)
lista_lotow2 = lista_lotow.replace(" ", "").split(",")
print(lista_lotow2)
