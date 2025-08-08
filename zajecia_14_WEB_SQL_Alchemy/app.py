from flask import Flask
from flask_sqlalchemy import SQLAlchemy #4 importujemy
from flask_migrate import Migrate #14

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zajecia_14_baza.db' #4 konfiguracja bazy danych
db = SQLAlchemy(app) #4 synchronizacja naszej aplikacji z SQLAlchemy
migrate =  Migrate(app, db) #14 - w nawiasie (stam aplikacji (app) i stan bazy danych (db)) - podajemy to po to, zeby
                            # caly mechanizm migracji, ktory kryje sie pod ta nasza zewnetrzna biblioteka widzial jaka
                            # jest roznica miedzy satnem faktycznym rzeczywistym bazy, a stanem faktycznym, ktory mamy
                            # wewnatrz tego pythonowego kodu.
#5
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, server_default='dummy.email@gmail.com') #13 Dodajemy

    #10
    def __str__(self):
        return f"User(id={self.id}, username={self.username}, first_name={self.first_name}, last_name={self.last_name}"

#6
with app.app_context(): # otwieramy kontekst naszej aplikacji
    db.create_all() # Tworzymy tabele w bazie danych

    # #7 ### OPERACJA TWORZENIA NOWEGO REKORDU W BAZIE DANYCH ###
    # user = User(
    #     username='admin3',
    #     password='admin123',
    #     first_name='Admin',
    #     last_name='User'
    # )
    # #7 teraz na sesji naszej bazy danych musimy dodac naszego uzytkownika
    # db.session.add(user) #Dodanie uzytkownika do bazy danych
    # # i teraz aby te dane trafily do tabelki w bazie danych musimy zakomitowac ta nasza sesje
    # db.session.commit()

    #13
    # admin_3 = User(
    #     username="admin_3",
    #     password="admin123",
    #     first_name="Admin",
    #     last_name="User",
    #     email="admin_3@gmail.com",
    # )
    # db.session.add(admin_3) # Dodajemy uzytkownika do bazy danych
    # db.session.commit() # Zapisanie zmian w bazie danych


    # #8 ### ODCZYTYWANIE NASZYCH REKORDOW ###
    # users = User.query.all()#8 - odczytanie wszystkich rekordow - po uruchomieniu programu w terminalu pojawia sie
    # # informacja [<User 1>, <User 2>], ze istnieja w naszej bazie danych dwaj uzytkownicy. I za kazdym razem bedzie ta
    # # informacja zwracane w postaci listyobiektow
    # print(users)
    # first_user = User.query.first() # wyciagamy pierwszego uzytkownika. Dostajemy informacje <User 1> za kazdym razem
    # # bedzie ta informacja zwracane w postaci tego specyficznego obiektu
    # print(first_user)



    # #9 ###FILTROWANIE DANYCH###
    # admin_2 = User.query.filter_by(username='admin', last_name='User'). first()
    # print(admin_2) # w tym momencie dostajemy informacje w postaci obiektu <User 2>, jezeli chcemy filtrowac po wiecej
    # # niz jednym polu to wystarczy w nawiasie podac po przecinku kolejne pole do filtrowania



    # #11 ###UPDATE REKORDU###
    # admin_2_to_change = User.query.filter_by(username='admin2').first() # filtrujemy sobie po <username>
    # admin_2_to_change.last_name = "ela"
    # db.session.add(admin_2_to_change) # teraz dodajemy uzytkownika do sesji
    # db.session.commit() # i dodajemy commit



    # #12 ###OPERACJA USUWANIA###
    # # db.session.delete(admin_2_to_change) # usuwanie uzytkownika z bazy danych
    # # db.session.commit() # Comitujemy - Zapisujemy zmiany w bazie danych
    #
    # # operacje usuniecia mozemy robic tez w inny sposob - to jest lepszy sposob bo usuwamy po konkretnym parametrze a
    # # nie po sesji jak powyzej
    # data_to_remove = User.query.filter_by(username="admin").delete()
    # db.session.commit() # Robimy commit zapisujac zmiane w bazie danych



if __name__ == "__main__":
    app.run(debug=True) # Uruchamianie aplikacji Flask w trybie debugowania


# 1 Instalujemy w SQLAlchemy wpisujac w terminalu <pip install Flask-SQLAlchemy>
# 2 Nastepnie w folderze gdzie znajduje sie nasz plik app.py tworzymy subfolder o specyficznej nazwie <instance>, bo tam
# bedzie sie miescila nasza baza.
# 3 tworzymy baze danych przez stworzenie pliku w folderze <instance>, pliku o nazwie <zajecia_14_baza.db>
# 4 nastepnie wpisujemy powyzej w punkcie #4 - po napisaniu tych 3 linijek mamy nasza aplikacje polaczona z nasza baza
# danych

# 5 Zaczniemy sobie od stworzenia sobie naszej pierwszej tabeli w naszej bazie danych - przejdz do #5 i stworz klase
# 6 Musimy terzaz powiedziec naszemu skryptowi pythonowemu naszemu flaskowi zeby stworzyl ta tabele - przejdz do #6
# I teraz jak uruchomimy program DBeaver to w tym programie widzimy nasza tabele.
# wg dobrych zasad zapytania SQLowe bedziemy robic w endpointach w pliku <routes.py>, ale na potrzeby tego cwiczenia
# teraz bedziemy te zapytania umieszczac w pliku <app.py>
# 7 tworzymy obiekt naszej tabeli - przejdz do #7
# Po zakomitowaniu naszej sesji bazy danych automatycznie nasz uzytkownik trafia do naszej tabelki w bazie danych
#!!!!!!!!!!!!!!! Po dodaniu uzytkownika do bazy danych i ponownym uruchomieniu programu wyskakuje nam blad ze nie moze
# dodac ponownie uzytkownika. dzieje sie to dla tego, ze mamy zapisane ze username ma byc unikalne

#                     username = db.Column(db.String(80), unique=True, nullable=False)

# wyskakuje blad bo username nie jest unikatowy - wiec zakomentujemy teraz punkt #7 - jest to pierwsza z operacji
# OPERACJA TWORZENIA REKORDU W BAZIE DANYCH



### ODCZYTYWANIE NASZYCH REKORDOW ###
# Zakladamy ze chcemy trzymac nasze rekordy w jakiejs zmiennej <users> wiec piszemy - przejdz do #8




###FILTROWANIE DANYCH###
# do filtrowania danych piszemy zapytanie, ktore bedzie wygladalo tak - przejdz do #9

# aby poznac co zawiera caly wiersz to musimy napisac funkce __str__ - przejdz do #10



###UPDATE REKORDU###
# Kiedy robimy update to nanosimy poprawki w jednym recordzie pod tym samym ID.
# Mozemy zrobic to w nastepujacy sposob - przejdz do #11



###OPERACJA USUWANIA###
# przejdz do #12



###Tworzenie migracji bazodanowych####
###Dodawanie kolumny z emailem kiedy tabela juz istnieje###
# 13 - tworzymy w <class> nowa linijke kodu do tworzenia kolumny <email>
# Przejdz do punktu #13 i dodajemy <admin_3>
# po uruchomieniu aplikacji wyskakuje nam blad - mowiacy nam ze nie doda nam czegos do kolumny, ktora nie istnieje

# sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) table user has no column named email
# [SQL: INSERT INTO user (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)]
# [parameters: ('admin_3', 'admin123', 'Admin', 'User', 'admin_3@gmail.com')]

# Jak taki blad jestesmy w stanie sobie rozwiazac nie usuwajac calego stanu naszej tabeli?
# Mozemy skorzystac z operacji tworzenia migracji bazodanowych do naczych aplikacji - zebysmy my mogli ten nasz stan
# ktory bedziemy mieli wewnatrz naszych kodow, wewnatrz tych naszych tabel zmieniac.
# Jak robic takie migracje??
# Flask nie jest frameworkiem lecz jest biblioteka. Wiec skoro nie mielismy wewnatrz tego rozszerzenia do jakichkolwiek
# narzedzi zwiazanych z operacjami na bazach danych, tak tez nie mamy wewnetrznych operacji wewnatrz tego naszego Flaska
# do migracji.
# Python jest jezykiem opensoursowym wiec posiada zewnetrzna biblioteke <Flask-Migrate>
# Aby ja zainstalowac wpisujemy w terminalu <pip install Flask-Migrate>. Instalujemy to na glownej sciezce w
# repozytorium - pamietamy ze caly czas jestesmy w wirtualnym srodowisku <(ksiegarnia_venv)>
# Przechodzimy do folderu <zajecia_14_WEB_SQL_Alchemy> gdzie mamy swoja baze danych
# Teraz musimy stworzyc obiekt migracji wewnatrz konfiguracji Flaska - dopisujemy na gorze #14
#               from flask_migrate import Migrate
# oraz pod synchronizacja piszemy
#               migrate =  Migrate(app, db)
# nastepnie bedac w folderze gdzie mamy nasza aplikacje <zajecia_14_WEB_SQL_Alchemy> piszemy w terminalu
#               flask db init
# to spowoduje ze powstana katalogi alembikowe, ktore beda odpowiedzialne za tworzenie i egzekucje migracji
# w tym momencie mamy polaczenie naszej aplikacji flaskowej z migracjami.
# Czym takie migracje faktycznie sa??
# Takie migracje sa plikami pythonowymi, ktore poprzez wykonanie odpowiedniej komendy beda one updatowaly/aktualizowaly
# faktyczny realny stan w bazie danych.
# W tym momencie tylko i wylacznie polaczylismy sobie mechanizm tworzenia migracji z nasza aplikacja - nie mamy w tym
# momencie jeszcze zadnej migracji stworzonej.
# wiec stworzmy sobie nasza pierwsza migracje
# Zebysmy mogli stworzyc migracje i zeby nam mechanizm migracji sprawdzil nam ten stan, ktory mamy zastany aktualnie z
# tym, ktory mielismy wczesniej to musimy dodac taka "flage" (jak w commit) piszemy w terminalu
# !!!!!!!!!WAZNE aby migracja zadzialala to nie moze byc zadnych aktywnych operacji na rekordach - wszystkie operacje
# !!!!!!!!!typu odczytywanie, dodawanie, usuwaie, updatowanie, filtrowanie itd. wszystkie musza byc zacomentowane
# !!!!!!!!!czyli niekaktywne
#               flask db migrate -m 'Nasza pierwsza migracja'
# w tym momencie w folderze <migrations> w folderze <versions> powstal plik z rozszerzeniem .py ktory ma kilka ciekawych
# opcji:
# 1. revision = '685f0d97f0f9' - ktory mowi nam o takim hash'u tej naszej migracji, tak samo jak mamy te hashe commitow
# jak sobie z gita wyciahniemy, tak samo wewnatrz tego mechanizmu naszej migracji tez te nasze hashe bedziemy mieli
# 2. def upgrade() - funkcja ktora bedzie nam dziala sie kiedy bedziemy chcieli zmienic stan rzeczywisty naszej bazy
# danych do tego stanu, ktory jest po tej migracji
# 3. def downgrade() - cofanie zmian i upgradow do zapisu z przed commita

# nasza tabela w bazie danych sie jeszcze niczym nie rozni
# poniewaz <unique constarin> powodowal nam problem wiec zmieniamy linijke:
# email = db.Column(db.String(80), unique=True, nullable=False)
# na
# email = db.Column(db.String(80), nullable=False, server_default='dummy.email@gmail.com')
# i teraz romimy downgrade
#               flask db downgrade
# Usuwamy z folderu <version> migracje
# i zrobmy sobie kolejna migracje piszac
#              flask db migrate -m 'trzecia migracja'
# powstal plik ce80f8f17a75_trzecia_migracja.py
# i teraz piszemy w terminalu
#               flask db upgrade
# odswiezamy tabelke z bazy danych i sie okazuje ze kolumna z emailem zostala dodana
# i od teraz modyfikacje naszych danych bedzie mozna przeprowadzac tylko i wylacznie za pomoca mechanizmu migracji


