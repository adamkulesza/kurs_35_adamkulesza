from flask import Flask
# 2.
from routes import my_blueprint
# 3.
from views import users_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint) # 2.
app.register_blueprint(users_blueprint) # 3.
if __name__ == "__name__":
    app.run(debug=True)

# mamy taka nasza podstawowa aplikacje.
# Na niej nic nie ma
# I zeby pisac i tworzyc enpoint to powinnismy pisac dalej ale nie po to uczylismy sie calego tego pythona, nie o to
# korzystalismy z tego calego dziedziczenia itd żebysmy teraz wrocili do podstaw i zebysmy wszystko walili w app.py do
# jednego pliku. No bo tych linijek kodu mamy bardzo bardzo duzo. wiec jezeli mamy bardzo duzo linijek kodu, to bardzo
# ciezko byloby to miec w jednym pliku i sie nie pogubic. Wiec co my w takich aplikacjach robimy?? bardzo czesto
# rozdielamy logike biznesowa od konfiguracyjnej od deklaracji tych poszczegolnych endpointow.
# Jak oddzielic sobie deklaracje endpoinow, ktore tutaj mamy w tej naszej aplikacji od tej tak naprawde konfiguracji,
# ktora tu mamy. Czyli stworzylismy sobie tego naszego flaska. Narazie wylacznie to ale zaraz bedziemy dodawali kolejne
# rzeczy i tez w ciagu tego tygodnia kilka konfiguracji nam przyjdzie w momencie kiedy bedziemy mowili sobie o bazach
# danych i o migracjach, natomiast tutaj narazie mamy app.py
# wiec zebysmy nie musieli deklarowac tych naszych endpointow w pliku app.py, to dobra praktyka programistyczna w naszych
# aplikacjach webowych jest stworzenie na ten moment pliku <routes.py>, ktory bedzie importowal z flaska cos takiego
# jak <Blueprint> - tworzymy ten plik - przejdz do tego pliku


# 2. Dopiero teraz rejestrujac sobie ten nasz blueprint uruchamiajac nasza aplikacje, wchodzac na ten nasz endpoint
# dopiero teraz mamy polaczenie meidzy tymi naszymi endpointami, czyli miedzy tym naszym plikiem routes.py i app.py

# I finalnie tak to powinno wygladac - abysmy jak najmniej logiki biznesowej trzymali w pliku app.py
# pliki w ktorych uruchamiamy te nasze serwery one powinny byc jak naj krotsze. Tu nie powinno byc zadnej logiki, tutaj
# powinna byc tylko i wylacznie konfiguracja ktora mamy, czasami jzeli ta konfiguracja jest spora i czesto ta
# konfiguracja spora jest, to mamy pliki config.py, w ktorych trzymamy te konfiguracje tych naszych webserwerow, tak
# tutaj jest tylko i wylacznie deklaracja tej aplikacji, dodanie jej jakiejs nazwy, rejestracja roznych rzeczy i tutaj
# nie powinno sie nic wiecej znajdowac.
# cała logika, ktora bedziemy pisali  w tej naszej ksiegarni ona sie bedzie znajdowala poza tym plikiem app.py

# Przejdzmy sobie teraz do naszych widokow klasowych - stworz plik views.py i przejdz do niego

# 3. po uruchomieniu app.py i po przejsciu do http://127.0.0.1:5000/users - strona wyswietla nam "List of users"