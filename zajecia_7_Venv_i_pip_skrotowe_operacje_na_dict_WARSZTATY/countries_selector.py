"""
** Zadzanie: Napisz program< ktory dostarczy nam informacji o wybranym kraju. Uzyj do tego ponizszego API Rest Countries.
Aplikacja ma dzialac nastepujaco:**
- Program pyta urzytkownika o nazwe kraju, dla ktorego nalezy sprawdzic informacje. Nazwa kraju musi byc podana w jezyku
angielskim i pozwala na pelne lub czesciowe dopasowanie.
- Aplikacja wykona zapytaie do API w celu pozyskania danych o kraju.
- Program powinien wyswietlic nastepujace informacje o kraju (jezeli sa dostepne):
    - Pelna nazwa kraju
    - Stolica
    - Region
    - Podregion
    - Jezyk urzedowy
    - Waluta
    - Flaga (poprzez URL do obrazka)
- Wyniki zapytan powinny byc zapisane do pliku. Jezeli szukany kraj znajduje sie juz w pliku, nie wykonuj zapytania do API,
tylko zwroc wynik z pliku.
URL do API:
https://restcountries.com/v3.1/name/{country_name}?fullText=true
W URL nalezy uzupelnic parametr: country_name
przykladowy funkcjonalny rezultat dla zapytania "Poland":
Pelna nazwa: Republic of Poland
Stolica: warsaw
Re3gion: Europe
Podregion: Eastern Europe
Population: 37970000
Jezyki urzedowe: Polish
Waluta: Polish zloty (PLN)
Flaga: https://flagcdn.com/pl.svg
**Wskazowka:** Mozesz wymagac od uzytkownika podania pelnej nazwy kraju (ustawiajac parametr fullText na true w URL) lub
pozwolic na wyszukanie zarowno pelnych, jak i czesciowych nazw kraju (bez parametru fullText)
"""
# 1.
# robimy srodowisko wirtualne w folderze <zajecia_7_Venv_i_pip_skrotowe_operacje_na_dict_WARSZTATY>
# korzystajac z terminala przechodzimy do folderu <zajecia_7_Venv_i_pip_skrotowe_operacje_na_dict_WARSZTATY>
# w terminalu wpisujemy
#                           <python -m venv countries_selector_venv>
# i wirtualne srodowisko mamy
# nastepnie aby aktywowac wirtualne srodowisko w terminalu wpisujemy
#                           <countries_selector_venv/Scripts/activate>
# teraz musimy sie dowiedziec co chcemy importowac
# znajdujemy w internecie jak zainstalowac w python biblioteke requests - https://pypi.org/project/requests/
# kopjujemy i wklejamy w terminalu komende
#                                   <pip install requests>
# po zainstalowaniu w naszym wirtualnym srodowisku biblioteki requests wpisujemy w terminalu <pip freeze > requirements.txt>
# dzieki temu requesty zaktywowaly sie w srodowisku wirtualnym (powstal tam plik <requirements.txt>)
# nastepnie wpisujemy w terminalu
#                                   <pip install -r requirements.txt> # aktywowanie pliku requirements.txt w srodowisku wirtualnym
# nastepnie sprawdzamy czy ta biblioteka dziala - na stronie tej biblioteki mamy

#import requests
#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
#print(r.status_code)
#print(r.json())

# Po uruchomieniu tego kodu mamy jakas odpowiedz z tego naszego endpointa i wiemy ze biblioteka requests dziala poprawnie
# wobec tego teraz musimy to napisac po naszemu.

import requests
# 3.
from file_handler import FileHandler

#file_handler = FileHandler(file_path="data.json")
# w folderze <zajecia_7_Venv_i_pip_skrotowe_operacje_na_dict_WARSZTATY> tworzymy plik <data.json> i narazie on bedzie
# pusta lista (wpisujemy tam tylko [] ) po stworzeniu tego pliku wpisujemy w parametrach na gorze
#               FileHandler(file_path="data.json")
# Przejdz teraz do punktu 4. na dol pliku countries_selector.py


# 1. kontynlacja
# Skorzystamy z funkcji - piszemy funkcje ( jako parametr podajemy juz <country_name>
# adres URL bedzie zapisany w f stringu - po co my to tak robimy? Zeby juz ten string dostal country name ktory podajemy w funkcji)
# (w dokumentacji nasze strony sprawdzamy jaka metoda tyczy sie zapytania o <Name>) - po sprawdzeniu wiemy ze to metoda get
# nastepnie piszemy
#                   <response = requests.get(url=url)>
# Zanim przekazemi i zwrocimy sobie te nasze dane z tego naszego API to co bedziemy musieli zrobic? Bedziemy musieli
# sprawdzic czy my mamy dobre pytanie?
# wiemy ze to nasze API jzezeli cos jest poprawne to zwtaca tylko kod 200 - wiec mozemy napisac
#                  <if response.status_code == 200:
#                       print(response.json())
#                       return response.json()
#                   else:
#                       print("Niestety taki kraj nie istnieje.")>


# def get_data_from_countries_api(country_name):
#     url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
#     response = requests.get(url=url)
#     if response.status_code == 200:
#         print(response.json())
#         return response.json()
#     else:
#         print("Niestety taki kraj nie istnieje.")

# Nastepnie wywolujemy ta metode dla testowania

# get_data_from_countries_api("Poland")
# get_data_from_countries_api("Republika Bananowa")


# Dygresja - po co nam te <.json> - pamietasz mielismy .json ktore imitowaly nam slowniki. Aktualnie protokol HTTP wspiera
# trzy rodzje wysylki danych ( pedy body) pomiedzy soba i takim glownym rodzajem tego jak cialo (body) bedzie skonstrulowane,
# tym naszym glownym, ktory aktualnie jest naszym trendem jest komunikacja typu REST.
# komunikacja typu REST pozwala nam na wysylke ciala i komunikacji ciala wlasnie za pomoca typu .json
# wiec te pliki .json zawsze beda nam dostepne w komunikacji RESTowej i bedziemy juz mogli automatycznie przeksztalcic sobie
# do jakiejs struktury
# wobec czego piszemy


# def get_data_from_countries_api(country_name):
#     url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
#     response = requests.get(url=url)
#     if response.status_code == 200:
#         data = response.json
#         print(type(data)) # po wyprintowaniu data wiemy ze plik .json jest struktura typu 'list' z ktorej mozemy pobrac sobie rzeczy
#         print(type(response.text)) # po wyprintowaniu wiemy ze response.txt jest struktura typu 'str' wiec bedziemy musieli go ewentualnie przeksztalcac
#         return response.json()
#     else:
#         print("Niestety taki kraj nie istnieje.")
#
# get_data_from_countries_api("Poland")
# get_data_from_countries_api("Republika Bananowa")

# Usuwamy sobie te trzy linijki (byly one tylko do pokazania jaki typ informacji dostaniemy)
#                               data = response.json
#                               print(type(data))
#                               print(type(response.txt))


def get_data_from_countries_api(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Niestety taki kraj nie istnieje.")


# wiec mamy pobieranie danych z tego API
# Kolejna rzecz ktora musimy zrobic (bo juz pobralismy sobue dane - mamy te dane w jakims formacie) jest napisanie
# kolejnej funkcji tak aby pobierac juz tylko okreslone informacje

# Po napisaniu pierwszej funkcji wyciagnelismy nasza liste ktora wyglada tak
# [{'name': {'common': 'Poland', 'official': 'Republic of Poland', 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}, 'tld': ['.pl'], 'cca2': 'PL', 'ccn3': '616', 'cioc': 'POL', 'independent': True, 'status': 'officially-assigned', 'unMember': True, 'currencies': {'PLN': {'symbol': 'zł', 'name': 'Polish złoty'}}, 'idd': {'root': '+4', 'suffixes': ['8']}, 'capital': ['Warsaw'], 'altSpellings': ['PL', 'Republic of Poland', 'Rzeczpospolita Polska'], 'region': 'Europe', 'subregion': 'Central Europe', 'languages': {'pol': 'Polish'}, 'latlng': [52.0, 20.0], 'landlocked': False, 'borders': ['BLR', 'CZE', 'DEU', 'LTU', 'RUS', 'SVK', 'UKR'], 'area': 312679.0, 'demonyms': {'eng': {'f': 'Polish', 'm': 'Polish'}, 'fra': {'f': 'Polonaise', 'm': 'Polonais'}}, 'cca3': 'POL', 'translations': {'ara': {'official': 'الجمهورية البولندية', 'common': 'بولندا'}, 'bre': {'official': 'Republik Polonia', 'common': 'Polonia'}, 'ces': {'official': 'Polská republika', 'common': 'Polsko'}, 'cym': {'official': 'Republic of Poland', 'common': 'Poland'}, 'deu': {'official': 'Republik Polen', 'common': 'Polen'}, 'est': {'official': 'Poola Vabariik', 'common': 'Poola'}, 'fin': {'official': 'Puolan tasavalta', 'common': 'Puola'}, 'fra': {'official': 'République de Pologne', 'common': 'Pologne'}, 'hrv': {'official': 'Republika Poljska', 'common': 'Poljska'}, 'hun': {'official': 'Lengyel Köztársaság', 'common': 'Lengyelország'}, 'ind': {'official': 'Republik Polandia', 'common': 'Polandia'}, 'ita': {'official': 'Repubblica di Polonia', 'common': 'Polonia'}, 'jpn': {'official': 'ポーランド共和国', 'common': 'ポーランド'}, 'kor': {'official': '폴란드 공화국', 'common': '폴란드'}, 'nld': {'official': 'Republiek Polen', 'common': 'Polen'}, 'per': {'official': 'جمهوری لهستان', 'common': 'لهستان'}, 'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}, 'por': {'official': 'República da Polónia', 'common': 'Polónia'}, 'rus': {'official': 'Республика Польша', 'common': 'Польша'}, 'slk': {'official': 'Poľská republika', 'common': 'Poľsko'}, 'spa': {'official': 'República de Polonia', 'common': 'Polonia'}, 'srp': {'official': 'Република Пољска', 'common': 'Пољска'}, 'swe': {'official': 'Republiken Polen', 'common': 'Polen'}, 'tur': {'official': 'Polonya Cumhuriyeti', 'common': 'Polonya'}, 'urd': {'official': 'جمہوریہ پولینڈ', 'common': 'پولینڈ'}, 'zho': {'official': '波兰共和国', 'common': '波兰'}}, 'flag': '🇵🇱', 'maps': {'googleMaps': 'https://goo.gl/maps/gY9Xw4Sf4415P4949', 'openStreetMaps': 'https://www.openstreetmap.org/relation/49715'}, 'population': 37950802, 'gini': {'2018': 30.2}, 'fifa': 'POL', 'car': {'signs': ['PL'], 'side': 'right'}, 'timezones': ['UTC+01:00'], 'continents': ['Europe'], 'flags': {'png': 'https://flagcdn.com/w320/pl.png', 'svg': 'https://flagcdn.com/pl.svg', 'alt': 'The flag of Poland is composed of two equal horizontal bands of white and red.'}, 'coatOfArms': {'png': 'https://mainfacts.com/media/images/coats_of_arms/pl.png', 'svg': 'https://mainfacts.com/media/images/coats_of_arms/pl.svg'}, 'startOfWeek': 'monday', 'capitalInfo': {'latlng': [52.25, 21.0]}, 'postalCode': {'format': '##-###', 'regex': '^(\\d{5})$'}}]
# musimy z tej list wyciagnac pierwsza wartosc - to robimy piszac
#
#               <country_info = respons_data[0] # dzieki temu pobieramy nasza wartosc
# nastepnie pobieramy aby pobrac oczekiwane wartosci piszemy
#
#     result = {
#         "full_name": country_info.get("name", {}).get("common", "N/A"),
#         "capital": country_info.get("capital", ["N/A"])[0],
#         "region": country_info.get("region", "N/A"),
#         "subregion": country_info.get("subregion", "N/A"),
#         "population": country_info.get("population", "N/A"),
#         "languages": ", ".join(country_info.get("languages", {}).values()),
#         "currency": ", ".join([f"{v['name']} ({k})" for k, v in country_info.get("currencies", {}).items()]),
#         "flag": country_info.get("flags", {}).get("svg", "N/A")
#     }


def modify_data_from_api_to_our_dict(response_data):
    if not response_data:
        return {}
    country_info = response_data[0]
    result = {
        "full_name": country_info.get("name", {}).get("common", "N/A"),
        "capital": country_info.get("capital", ["N/A"])[0],
        "region": country_info.get("region", "N/A"),
        "subregion": country_info.get("subregion", "N/A"),
        "population": country_info.get("population", "N/A"),
        "languages": ", ".join(country_info.get("languages", {}).values()),
        "currency": ", ".join([f"{v['name']} ({k})" for k, v in country_info.get("currencies", {}).items()]),
        "flag": country_info.get("flags", {}).get("svg", "N/A")
    }

    return result

# wiec na probe zrobmy sobie

#           poland = get_data_from_countries_api("Poland")
#           get_data_from_countries_api("Republika Bananowa")
#           print(modify_data_from_api_to_our_dict(poland))
# 4. Po punkcie 3. dopisujemy w tym miejscu
#           file_handler.data.append(modify_data_from_api_to_our_dict(poland)) # dodajemy ten nasz slownik do tej naszej listy
#           file_handler.write_data_to_file() # bedziemy to wszystko zapisywali w pliku data.json ktory byl pusta lista
# ostania rzecz - Wyniki zapytan powinny byc zapisane do pliku. Jezeli szukany kraj znajduje sie juz w pliku, nie wykonuj
# zapytania do API, tylko zwroc wynik z pliku. - O co tu chodzi
# Chodzi tutaj o to ze w naszych aplikacjach, ktore mu piszemy, komunikacja z jakim kolwiek zewnetrznym serwisem, czy to
# baza danych, czy to jakis plik, czy to jest komunikacja przez protokul HTTP z jakims zewnetrznym API jest komunikacja
# droga pod wzgledem czasu, czyli odpowiedz naszego serwera bedzie zajmowala o wiele wiecej czasu. No i tez nie zawsze
# chcemy zeby te zapytania caly czas chodzily. Tutaj przychodzi nam z pomoca takie cos jak "keszowanie danych" - czyli
# trzymanie jakichs wartosci w wewnetrznej pamieci naszej aplikacji, zebysmy my mogli z tej pamieci skorzystac. Nie zawsze
# musi byc to pamiec zewnetrzna, natomiast zazwyczaj chcielibysmy zeby to byla pamiec szybka. Jezeli nie bedzie to pamiec
# wewnetrzna tak jak w tym przypadku, to bardzo czesto my jako programisci bedziemy korzystali z takiej bazy danych typpu
# "readies" - readies to jest baza danych (klucz oraz wartosc) ktora jest szybka - ona dziala na pamieci RAM.
# Natomiast Keszowanie mozna robic rowniez w ten sposob ktory my tu zrobimy. Ten sposob nazywa sie
#
#                               MEMOIZACJA
# Memoizacja jest to trzymanie stanu naszej aplikacji w pamieci aplikacji a nie w jakiejs zewnetrznej bazie
# Co tobimy to Komentujemy/Usuwamy ostatnie 5 linijek naszego kodu i piszemy


# 6. Przerzucamy tutaj
file_handler = FileHandler(file_path="data.json")
user_country = input("Enter country name: ")
# 6. i dopisujemy
if country_data := file_handler.lookup_for_country_in_data(user_country): # := oznacza ze sprawdzam czy jest tu (file_handler.lookup_for_country_in_data(user_country)) jakas wartosc i jezeli jest to przypisuje ja do zmiennej <country_data>
    print("Country data already exist in file.")
    print(country_data)
else:
    country_info_from_api = get_data_from_countries_api(user_country)
    modified_data = modify_data_from_api_to_our_dict(country_info_from_api)
    file_handler.write_data_to_file(modified_data)
# Przechodzimy do file_handlera i modyfikujemy ostatnia funkcje - przejsd do punkty 5. w file_kandler


# 1. kontynlacja
# Czego jeszcze brakuje - to zapisywania naszych danych do pliku - wiec tworzymy plik <file_handler>
# przejdz do punktu 2 w pliku <file_handler>