from flask import Blueprint

my_blueprint = Blueprint("my_blueprint", __name__) # definiujemy sobie obiekt typu blueprint


@my_blueprint.route("/")
def root_rout():
    return "Hello from the root route!"
# na co te blueprinty beda nam w tym flasku pozwalaly
# w momecnie, w ktorym my bedziemy definiowali sobie funkcje <root_rout> "Hello from the root route!"
# z deklaracja @my_blueprint.route bedziemy mogli w pliku <routes.py> bedziemy mogli zdefiniowac sobie ten nasz globalny
# endpiot.
# Nie tak jak w poprzednich zajeciach mielismy w app.py cala logike i wszystkie endpointy, ktore tworzylismy. Tak teraz
# oddzielilismy sobie logike aplikacji tworzenia i konfiguracji, od deklaracji tych naszych endpointow.

# uruchommy nasza aplikacje
# o dziwo nie mamy jeszcze tego naszego endpointa, bo zapomnielismy o czyms waznym, o czyms co teoretycznie powinnismy
# pamietac z pythona - musimy zaimportowac w pliku app.py plik routes.py
# przejdz do pliku app.py i na gorze pliku zaimportuj plik, # 2.
# oraz w naszej aplikacji zarejestrowac ten blueprint (app.register_blueprint(my_blueprint) - dopisz to w app.py