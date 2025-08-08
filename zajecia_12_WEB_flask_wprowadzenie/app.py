# from flask import Flask,
# # zaimportowalismy sobie obiekt falsak z biblioteki Flask
#
# app = Flask(__name__) #tu zadeklarowalisy sobie ta nasza aplikacje - stworzylismy obiekt naszej aplikacji
#
# # to jest pierwszy - glowny endpoint, ktory bedzie sie nam wykonywal na tej naszej glownej sciezce - "/" oznacza glowna
# # sciezke - ze to jest nasz glowny endpoint
# # <@app.route> jest to dekorator dzieki, ktoremubedziemy mowili, ze ta funkcja bedzie wykonywana, w momencie kiedy ktos
# # wejdzie na nasz glowny endpoint na tym sleshu "/"
#
# # @app.route("/")
# # def hello():
# #     return "Hello, World!"
#
# ########## WAZNE #########
# # uruchamiamy ta aplikacje webowa przez wpisanie w terminalu <flask run>
# # w terminalu pojawil sie adres url na ktory musimy wejsc http://127.0.0.1:5000
#
#
# # # dodajemy teraz kolejny endpoint - po ukosniku ktory oznacza nasz glowny enpoint piszeny <"/hello">
# # # aby ten endpiont zadzialal trzeba zatrzymac dzialanie aplikacji naciskajac Ctrl+C a nastepnie ponownie uruchomic
# # # wpisujac <flask run>
# # # Po nacisnieciu http://127.0.0.1:5000 dopisujemy do adresu url </hello>
# # @app.route("/hello")
# # def hello_user():
# #     return "Hello, User"
# #
# #
# #
# # ###################### Tworzenie dynamicznych endpoinow ######################
# #
# # # aby wykonac dynamiczny endpoint piszemy dekorator naszego endpointu w nastepujacy sposob
# # @app.route("/hello/<name>")
# # def hello_name(name):
# #     return f"Hello, {name}!"
# #
# # # taki sposob zapisu ze zmienna <name> powoduje ze mamy dynamiczny endpiont - wpisujac teraz adres url
# # # http://127.0.0.1:5000/hello/Adam otwiera nam sie strona ktora wita nas <Hello, Adam!>
# # # http://127.0.0.1:5000/hello/Cos_tam_innego otwiera sie nam strona ktora wita nas <Hello, Cos_tam_innego!>
#
#
# #####################
# # Jak polaczyc oba endpointy /hello i /hello/<name>???
# # robimy to w nastepujacy sposob
#
# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_user(name=None):
#     if name:
#         return f"Hello, {name}!"
#     else:
#         return "Hello, User"
# # dzieki temu mamy polaczone endpointy i nie mamy nadmiernego pisania
#
#
# ######################
# # Polaczmy ten nasz kod flaskowy z kodem HTML
# ############# BARDZO WAZNE jest to, ze tworac aplikacje Flask - aplikacja Flask ma swoje jakies ustawienia domyslne, ktore gdzies
# # tam dzialaja.
# # Wiec jezeli my nie bedziemy chcieli nadpisywac tych ustawien domyslnych aplikacji Flask, to bedziemy musieli korzystac
# # z jej schematu. jezeli chcemy korzystac z jej schematu i nie chcemy nadpisywac tych ustawien, to bardzo wazne jest to,
# # ze pliki HTML, ktore bedziemy tworzyli (templatki) beda musialy sie znajdowac w katalogu templates na tym poziomie na
# # ktorym jest ta aplikacja
# # W pliku <zajecia_12_WEB_flask_wprowadzenie> tworzymy katalogo <templates> a w nim plik HTML <hello_world>
# # przejdz do tego pliku <hello_world.html>


# 2.
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return render_template("hello_world.html")
# dzieki temu mamy podpiete do pierwszego endpointa  nasz plik <hello_world.html>

# Po co nam python, ktorego uczylismy sie przez wiele tygodni?
# Sprobujmy go teraz podpiac.
# A teraz jak polaczyc to co mamy w tym naszym pythonie - to co tam sobie obliczaismy z ta nasza warstwa wizualna??
# tworzymy w folderze <templates> plik hello_uesr.html i zmieniamy ponizszy endpoint tak aby odczytywal plik
# hello_user.html

# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_user(name=None):
#     return render_template("hello_user.html")

# Po uruchomieniu tego pliku <flask run> i po przejsciu na strone
# http://127.0.0.1:5000/hello - ortrzymujemy nastepujacy widok strony

# Hello, !
# Welcome to our website.

# po przecinku jest jakas spacja) nie tego sie spodziewalismy - ale wlasnie to jest to miejsce gdzie bedziemy mogli wstrzykiwac nasze dane z pythona - jak tp rpbimy??
# funkcja render_template przyjmuje conajmniej jedna wartosc. wiec w <return> w nawiasie mozemy dopisac <return render_template("hello_user.html", user_name=name)

# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_user(name="Andrzej"):
#     return render_template("hello_user.html", user_name=name) #user_name to jest dokladnie ten sam parametr ktorey mamy
# # w nawiasie w pliku hello_user.html - dzieki temu na naszej stronie wyswietla sie

# Hello, Andrzej!
# Welcome to our website.


# Czasami nie chcemy miec "Andrzeja tylko chcemy miec "None"
# Dzieki temu, ze te nasze templatki to nie jest czysty html, tylko jest to html, ktory wspiera takie cos jak jinja
# templates, to mozemy tam popisac troszeczke logiki - przejdz do pliku hello_user.html

# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_user(name=None):
#     return render_template("hello_user.html", user_name=name)

# mozemy takze w nawiasie dodac np user_age=20

# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_user(name=None):
#     return render_template("hello_user.html", user_name=name, user_age=3)
# wowczas w pliku hello_user.html dodajemy linijki logiki zwiazane z user_age


############## Jak wlaczyc zeby nie trzeba byla wylaczac i wlaczac aplikacje za kazdym razem kiedy cos zmieniamy???

# Domyslnie po uruchomnieniu aplikacji za pomoca komendy flask_run jestesmy w trybie "Debug mode: off"- czyli nie
# jestesmy w trybie debugowania naszej aplikacji
# Aby to zmienic to musimy po wylaczeniu aplikacji (Ctrl +C) wpisac w terminalu <flask run --debug>
# dzieki temu za kazdym razem kiedy zapiszemy plik app.py (ctr+S) automatycznie wszystko zostanie przeladowane w
# terminalu i nasza strone bedziemy mogli odswiezyc bez ponownego restartowania flaska


######### co zrobic zeby uruchamiac nasza aplikacje za pomoca komendy <python app.py>
# piszemy:

# if __name__ == "__main__":
#     app.run(debug=True)
# to tez pozwoli nam na uzycie debugera ale tylko w wersji PRO
# python ma swojego debugera - standardowy winstalowany w pythona nazywa sie "pdb" a niestandardowy, ktory trzeba
# zainstalowac to "ipdb" - wpisujemy linijke <import ipdb; ipdb.set_trace()> od tego momentu gdzie chcemy zaczynac sprawdzanie
# Skroty klawiaturowe do ipdb
# n (next): Wykonuje następny wiersz kodu. Jeśli kolejna linia to wywołanie funkcji, wchodzi do tej funkcji.
# s (step): Wchodzi do wywołania funkcji, zatrzymując się na pierwszej linii wywoływanej funkcji.
# c (continue): Wznawia wykonywanie do następnego punktu przerwania lub końca programu.
# l (list): Wyświetla kod źródłowy wokół bieżącej linii. Można określić zakres, np. l 10, 20, aby zobaczyć linie od 10 do 20.
# p (print): Wyświetla wartość zmiennej lub wyrażenia. Na przykład, p my_variable pokaże wartość my_variable
# q (quit): Wyjście z debuggera i zakończenie programu.
# b (breakpoint): Ustawia punkt przerwania. Można ustawić na konkretnej linii lub funkcji używając b nr_linii lub b nazwa_funkcji.
# tbreak: Ustawia tymczasowy punkt przerwania, który zostaje usunięty po jednym trafieniu.
# where (lub w): Wyświetla bieżący stos wywołań.
# args (lub a): Wyświetla argumenty bieżącej funkcji.
# pp (pretty print): Ładnie drukuje wartość zmiennej lub wyrażenia dla łatwiejszego odczytu.
# up (lub u): Przesuwa się poziom wyżej na stosie wywołań (przydatne przy debugowaniu funkcji zagnieżdżonych).
# down (lub d)*: Przesuwa się poziom niżej na stosie wywołań


########### Zrobmy sobie cos ciekawszego
# dodajmy <users>

from flask import Flask, render_template, request

users = [
    {
        "name": "Alice",
        "age": 30,
        "email": "alice_example.com",
        "city": "New York"
    },
    {
        "name": "Bob",
        "age": 25,
        "email": "bob_example.com",
        "city": "Los Angeles"
    },
    {
        "name": "Charlie",
        "age": 35,
        "email": "charlie_example.com",
        "city": "Chicago"
    }
]

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello_world.html")

@app.route("/hello")
@app.route("/hello/<name>")
def hello_user(name=None):
    return render_template("hello_user.html", user_name=name, user_age=3)

# stworzmy kolejny endpoint

@app.route("/users", methods=["GET", "POST"])
def show_users():
    saldo = 10
    if request.method == "POST":
        form_type = request.form.get("form_type")
        match form_type:
            case "change_price": # formularz zmiana salda
                print("Changing price")
                saldo = request.form.get("new_saldo")
            case "add_user": # formularz dodawanie uzytkownika
                print(form_type)
                new_user = {
                    "name": request.form.get("name"), # to co jest w nawiasie jest to klucz, ktory podalismy w formularzu w pliku users.html name="name"
                    "age": request.form.get("age"), # to co jest w nawiasie jest to klucz, ktory podalismy w formularzu w pliku users.html name="age"
                    "email": request.form.get("email"), # to co jest w nawiasie jest to klucz, ktory podalismy w formularzu w pliku users.html name="email"
                    "city": request.form.get("city_name") # to co jest w nawiasie jest to klucz, ktory podalismy w formularzu w pliku users.html name="city_name"
                }
                users.append(new_user)
            case "delete_user": # formularz usuwanie uzytkownika
                print(form_type)
                user_name = request.form.get("delete_name")
                for user in users:
                    if user["name"] == user_name:
                        users.remove(user)
                        break
    return render_template("users.html", users=users, saldo=saldo) # i tworzymy plik <users.html> w folderze templates

if __name__ == "__main__":
     app.run(debug=True)




# Tworzenie naglowkow w innym pliku dla wszystkich plikow HTML

# tworzymy plik base.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#
# <nav>
#   <h1>aaaa</h1>
#   <h1>aaaa</h1>
#   <h1>aaaa</h1>
#   <h1>aaaa</h1>
#   <h1>aaaa</h1>
# </nav>
#   <h2> to bedzie nasz kontent</h2>
#   {% block content %}
#     {% endblock %}
# </body>
# </html>
#
# W users.html  usuwany wszystko powyzej <body> i ponizej <body> i dodajemy na gorze:
#
# {% extends "base.html" %}
# {% block content %}
#
# a na dole:
#
# {% endblock %}
# nastepnie przeladowujemy strone Ctrl+C i uruchamiamy ponownie - flask run
# Dzieki takim zmianom automatycznie pojawia nam sie nagloweg pobrany z pliku base.html
#
# Podobnie robimy z plikiem hello_world.html tak aby po wpisaniu adresu <http://127.0.0.1:5000> na starcie pojawil sie
# ten sam naglowek co po wpisaniu http://127.0.0.1:5000/users
#
# dzieki temu mamy jeden ten sam naglowek na kilku stronach

#### Tworzymy pierwszy formularz w pliku users.html, w ktory bedziemy mogli dodawac tego uzytkownika po wejsciu na
# strone http://127.0.0.1:5000/users bedziemy mieli na dole formularz

#   <form>
#     <label for="name">Name:</label>
#     <input type="text" id="name" name="name" required>
#     <label for="age">Age:</label>
#     <input type="number" id="age" name="age">
#     <label for="email">Email:</label>
#     <input type="email" id="email" name="email" required>
#     <label for="city">City:</label>
#     <input type="text" id="city" name="city_name" required>
#     <button type="submit">Add User</button>
#   </form>

# i tak oto mamy pierwszy formulaz z przyciskiem <Add User>
# gdy chcemy dodac usera to dostajemy taka informacje. z zapytaniem GET
# 127.0.0.1 - - [28/Jul/2025 12:14:30] "GET /users?name=Adam+Kulesza&age=21&email=bernardkulesza@gmail.com&city_name=Stuttgart HTTP/1.1" 200 -
# Jednakze my potrzebujemy zapytania POST aby dodawac cos do naszego formularza
# co musimy zatem zrobic??
# W naszym formularzu, ktory zrobilismy w pliku <users.html> musimy zrobic dwie rzeczy:
# najpierw dodajemy do <form method="post">
# a nastepnie do endpointu dopisujemy jakiego typu dany endpoint wspiera żądania - jezeli nie mamy tego okreslonego to
# domyslnie stosuje metode GET - wiec dopisujemy:
# @app.route("/users", methods=["GET", "POST"])
# oraz musimy rozroznic co bedziemy robic w zaleznosci od tego jakie pytanie bedziemy mieli czy GET czy POST
# wiec z flaska importujemy <request> (dopisujemy to na gorze pliku przy imporcie z flaska)
# po imporcie dopisujemy do endpointa:
#     if request.method == "POST":
#         new_user = {
#             "name": request.form.get("name"),
#             "age": request.form.get("age"),
#             "email": request.form.get("email"),
#             "city": request.form.get("city")
#         }
#         users.append(new_user)
# Po dopisaniu tego wszystkiego do enpointa nasz formularz dziala i dodaje uzytkownikow
#
#
# Jak dodac przycisk  zeby przemieszczac sie pomiedzy plikami html
# Do <body> w kazdym pliku dopisujemy cos takiego - kolejne przyciski przekierowujace do kolejnych plikow html
#
#     <button>
#         <a href="/">Home</a>
#     </button>
#     <button>
#         <a href="/users">Users</a>
#     </button>
#
# Abu zrobic to bardziek kompatybilne z pythonem to poszemy tak:
#
#     <button>
#         <a href="{{url_for('hello')}}">Home</a> # gdzie nazwa 'hello' wystepuje w definicji - def hello()
#     </button>
#     <button>
#         <a href={{url_for('show_users')}}>Users</a> # gdzie nazwa 'hello' wystepuje w definicji - def show_users()
#     </button>
# dzialanie bedzie takie same jak wczesniejszych przyciskow ale bazujemy juz na strukturze pythonowej