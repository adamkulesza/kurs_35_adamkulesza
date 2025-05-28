# Unikamy ARGS i KWARKSY - staramy sie robic funkcje

# ARGS
####################
# Specjalne rodzaje argumentow, parametrow, ktore bedziemy mogli przekazywac do naszych funkcji


def przywitaj_sie(imie, nazwisko):
    print(f"Witaj {imie} {nazwisko}!")
    return f"Witaj {imie} {nazwisko}!"  # ten return nie jest przypisany do naszej zmiennej i mimo to niczego nam nie popsuje


przywitaj_sie("Adam", "Kulesza")

# Do tej popry przekazywalismy te parametry tak stricte. Natomiast my mozemy tez, w parametrach naszej funkcji
# oczekiwac, że nie do konca bedziemy wiedzieli co chcemy do niej przekazywac. Chodzi o to ze wewnatrz Pythona mamy taka
# specjalna skladnie za pomoca ktorej nie musimy jawnie przekazywac parametrow, ktore bedziemy dostawali w momecie wywołania.
# Zeby to osiagnac musimy skorzystac z czegos takiego jak <argumenty> naszej funkcji lub <keyworld argumenty>, ktore beda
# rozpakowywane wewnatrz naszej funkcji.
# Jaka taka skladnia wyglada? Skladnia wyglada tak, ze zamiast przekazywac tak jak w linijce pierwsze (imie, nazwisko)
# czyli zmienne do ktorych bedziemy przekazywali te nasze argumenty, bedziemy korzystali z takiego zapisy <*args>.
# To bedzie nam oznaczalo, ze my bedziemy do tej naszej funkcji przekazywali jakies parametry, ale nie do koncza wiemy jakie.


def przywitaj_sie_z_args(*args):
    argumenty = args
    print(args)


przywitaj_sie_z_args(1, 2, 3, "Michal", "Zietkowski")


# Pozwoli to nam na wywolanie tej naszej funkcji z wieloma parametrami, Ta liczba parametrow moze byc nieskonczenie duza
# mozemy tam wpisywac cokolwieg (w tym nawiasie)
# Uruchamiajac ta funkcje ona nadal bedzie mi dzialala
# Te argumenty, ktore my tu bedziemy przekazywali w parametrach one znajdowac sie beda w takiej specjalnej zmiennej,
# zmiennej <*args> - ta zmienna mozna nazwac dowolnie ale wazne zeby posiadala gwiazdke na poczatku - bo to jest
# rozpakowywanie struktury plaskiej czyli krotki/tuple oraz listy ( czyli kazdy z tych parametrow ma swoj indeks) i aby
# uzyskac ktorys parametr trzeba wywolac go z indeksem


def przywitaj_sie_z_args(*args):
    argumenty = args
    pierwszy_argument = args[0]
    print(pierwszy_argument)
    print(args)


przywitaj_sie_z_args(1, 2, 3, "Michal", "Zietkowski")

# Jaki jest tu problem - podalismy parametry ale nie podalismy stricte czym te parametry sa
# nie podalismy ze
# przywitaj_sie_z_args (1, 2, 3, imie= "Michal", nazwisko= "Zietkowski")
# bo jezeli bysmy chcieli definiowac te parametry wlasnie w taki sposob to wyskoczy nam blad. Takie dzialanie nie bedzie poprawne
# korzystajac z <*args> mozemy przekazywac wartosci tylko i wylacznie bez zadnych nazw


# KWARGSY
#####################
# zeby przekazywac wartosci z nazwami musimy skorzystac z drugiej naszej funkcji <**kwargs>
# ta struktura z dwiem gwiazdkami bedzie nasza struktura slownikowa


def przywitaj_sie_z_kwargs(**moje_kwargsy):
    print(moje_kwargsy)


przywitaj_sie_z_kwargs(imie="Adam", nazwisko="Kulesza", wiek=30, miasto="Szczecin")


# ARGS + KWARGS
# zeby przekazywac argumenty jak i keyword argumenty musimy podac jedno jak i drugie
#!!!!!!!!!!!!! BARDZO WAZNA JEST KOLEJNOSC!!!!!!!!!!!!!!!!


def przywitaj_sie_z_args_kwargs(imie, nazwisko, *args, **moje_kwargs):
    print(imie)
    print(nazwisko)
    print(args)
    print(moje_kwargs)


# zeby wywolywac tak ta funkcje to musimy to robic w ten sposob

przywitaj_sie_z_args_kwargs(
    "Jan",
    "Kowalski",
    1,
    2,
    3,
    4,
    imie="Adam",
    nazwisko="Kulesza",
    wiek=43,
    miasto="Szczecin",
)
