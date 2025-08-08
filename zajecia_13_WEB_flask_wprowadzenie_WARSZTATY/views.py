##### Widoki klasowe
# To jest cos co sie tworzy zamiennie z tymi widokami funkcyjnymi. Dlaczego???
# dla tego ze lwia czesc tej naszej ligiki bedzie oderwana od rzeczywistosci i od deklaracji tych routes'ow i tego
# wszystkiego. Wiec nie ma az tak duzego sensu zeby dawac sobie dodatkowy narzut w tworzeniu tych naszych widokow
# klasowych. natomiast cos takiego tez istnieje. Wazne zeby wiedziec ze te dwa sposoby sa wykorzystywane do tworzenia
# widokow.
# Mamy routes.py gdzie mamy te nasze endpointy
# ale tez mozemy uzyc pliku views.py, w ktorym bedziemy mieli te widoki
# piszemy
from flask import Blueprint
from flask.views import MethodView

users_blueprint = Blueprint("users", __name__) # blueprint na naszych uzytkownikow

# stworzmy sobie UsersView, ktory bedzie nasza klasa i co bardzo wazne w tym naszym flasku bedzie on dziedziczyl po
# czyms takim jak MethodView - MethodView jest to kalasa, ktora przychodzi nam z flaska, wmomencie kiedy go instalujemy
# <from flask.views import MethodView> tu bedzie ta metoda
class UsersView(MethodView):
    def get(self):
        return "List of users"

    def post(self):
        return "Add a new user"


# mamy metode <get> i metode <post>
# mozemy teraz zrobic sobie takie cos, ze

users_view = UsersView.as_view("users")
users_blueprint.add_url_rule('/users', view_func=users_view, methods=['GET', 'POST'])

# teraz przechodzimy do pliku app.py do # 3.