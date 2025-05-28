"""Pakiet .json
pozwala nam na to zebysmy my mogli zapisywac pliki i odczytywac je przeksztalcajac je na slowniki na przyklad."""
"""stworzylismy plik data.json (zerknij do niego)"""
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))


"""aby nadpisac cos jako slownik w <data.json> nalezy"""
with open("data.json", "w") as file:
    data = {
        "name": "John",
        "age": 30,
        "city": "new York"
    }
    file.write(json.dumps(data))

"""Plik .json - jedna struktura danych jednolita np. slownik albo lista slownikow - kilka slownikow po przecinku nie zadziala"""