from zajecie_6_Przykladowe_wbudowane_pakiety_WARSZTATY.math_module import add_numbers, format_user_profile


import pytest

@pytest.fixture
def sample_user():
    return {
        "first_name": "Matt",
        "last_name": "Collins",
        "age": 15,
        "email": "matt@gmail.com",
        "is_admin": True
    }

@pytest.fixture
def expected_user_profile():
    return {
        "full_name": "Matt Collins",
        "age": 15,
        "email": "matt@gmail.com",
        "admin": "Yes"
    }

#       nasze testy powinny sie zaczynac od slowka kluczowego <test>
#       wewnatrz testow beddziemy musieli sprawdzic tak jak zwykle testy czy na przyklad dodanie 2 i 3 da nam 5
#       sprawdzenie i porownanie czy wynik dzialania tej funkcji (<add_nmbers>) jest rowny jakiejs wartosci (5) robimy
# sobie za pomoca slowka <assert> - w tym momencie napisalismy, bardzo prosty test jednostkowy - bo w tym momencie ten
# test testuje tylko i wylacznie jedna funkcjonalnosc, jedna funkcje, z tego naszego kodu.
# Testy jednostkowe to Unitesty sa najwazniejsza czescia testowania - takie jednostkowe testowanie

#       w pythonie do wytwarzania testow jednostkowych i testow integracyjnych i ogolnie do pisania testow mamy dwa glowne pakiety
# 1. Pakiet Unit test - wbudowany w pythona
# 2. Pakiet Pytest - najczesciej uzywany pakiet - nie jest zainstalowany wiec musimy go zainstalowac - wpisujemy w terminalu
#                                   pip instal pytest

# po zainstalowaniu pytest - wpisujac w terminalu
#                   pytest .
#       test ten sie wykona - przyimek <test> w nazwie test_add_numbers() powoduje ze pytest go wykonuje - gdyby nie bylo
# tego przyimka <test> to pytest nie wykryl by tego jako test.
# Pytest organizuje testy na poziomie funkcji nie na poziomie klas
# unitTest organizuje testy na poziomie klas

def test_add_numbers():
    assert add_numbers(2, 3) == 5

# te testy mozemy oczywiscie rozszerzacz - np mozemy sprawdzic:

    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


#       po zaimportowaniu sobie tutaj <import pytets> mozemy sobie ten nasz kod zparametryzowac - ponizej napiszemy 5 testow
# pliku math_module

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add_numbers_parameterized(num1, num2, expected):
    assert add_numbers(num1, num2) == expected

#       to sa testy jednostkowe ktore nie zaleza od jakiegokolwiek innego modulu w pythonie - one maja za zadanie tylko i
# wylacznie sprawdzic czy ten fragment kodu (pojedyncza funkcja) jest zrobiona poprawnie

#       mozemy tez napisac taka funkcje - mozemy sprawdzic czy na przyklad w momencie wykonania bledu on nam zatwierdzi
# ten test jako pozytywny bo my oczekiwalismy ze wyskoczy blad

def test_add_numbers_throws_exception():
    with pytest.raises(ValueError):
        add_numbers("a", 1) # w pliku math_module dodalismy w return aby te liczby byly intigerem




# testujemy format_user_profile z pliku math_module

# def test_format_user_profile():
#     temp_user = {
#         "first_name": "Matt",
#         "last_name": "Collins",
#         "age": 15,
#         "email": "matt@gmail.com",
#         "is_admin": True
#     }

# mamy ten <expected_format> i musimy zobaczyc czy bedzie to nam dzialalo i dla tego robimy powyzej <temp_user>
# ma przeksztalcac z <temp_user> na <expected_format>

    # expected_format = {
    #     "full_name": "Matt Collins",
    #     "age": 15,
    #     "email": "matt@gmail.com",
    #     "admin": "Yes"
    # }
    # assert format_user_profile(temp_user) == expected_format

# aby sprawdzic w terminalu jak przebiegly wszystkietesty to wpisujemy w terminalu <pytest -vv .>

#       test format_user_profile z pliku math_module zostal pozytywnie wykonany - ale chcieli bysmy zrobic kolejny test z tego
# pliku. Chcieli bysmy np. zeby tylko zwrocil nam "full_name": full_name. Normalnie musielibysmy jeszcze raz napisac
# taki sam test i ponownie napisac temp_user i expected_format. Wiec zeby nie pisac znowu tego samego do nieskonczonej
# ilosci funkcji mozemy skorzystac z czegos takiego jak <fixture> - piszemy to na poczatku pliku.
#       Majac te fixtury mozemy przekazac je do tych testow

def test_format_user_profile(sample_user, expected_user_profile):
    assert format_user_profile(sample_user) == expected_user_profile

#       Teraz po przekazaniu tych fixtur i po uruchomieniu testu, widzimy ze test ten działa. Mamy dokladnie to samo.
# Natomiast dzieki fixturom mamy to na poziomie globalnym (nie mamy tego wewnatrz funkcji w naszym lokalnym scoupie) i
# bedziemy mogli z tego korzystac bez wielokrotnego powielania funkcji. A wiec mozemy na teraz zapytac sie tylko o
# full_name bez pisania ponownego tych samych funkcji. I tak w nieskonczonosc bez powielania funkcji.

def test_format_user_profile_proper_full_name(sample_user, expected_user_profile):
    user_profile = format_user_profile(sample_user)
    assert user_profile["full_name"] == "Matt Collins"

def test_format_user_profile_email(sample_user, expected_user_profile):
    user_profile = format_user_profile(sample_user)
    assert user_profile["email"] == "matt@gmail.com"


#       Testy integracyjne
# Roznica miedzy testami integracyjnymi a testami jednostkowymi jest taka, ze  w testach jednostkowych testujemy jedna
# funkcje, jedno dzialanie. Wszystko do okola sobie obudowujemy, jestesmy w jakims odizolowanym srodowisku, testujemy
# tylko jeden fragment kodu.
#       To testy integracyjne nie maja tej otoczki (srodowiska zamknietego) czyli one rzeczywiscie, o ile program tego
# wymaga, powinny zadzwonic do jakiegos zewnetrznego serwisu, albo wykonac ta inna funkcje i powiny sprawdzic jak to
# nasze polaczenie miedzy tymi naszymi dwiema funkcjami wyglada. Testy integracyjne sa robione w osobnym module
# (w osobnym katalogu)