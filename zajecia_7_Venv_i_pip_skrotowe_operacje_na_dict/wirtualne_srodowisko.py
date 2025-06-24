#       Kazdy z nas pracujac sobie nad tymi naszymi programami mial juz stycznosc z tym naszym <pip>. Za pomoca niego
# instalowalismy sobie <raff>, <mypy>, instalowalismy sobie <pytest>. Kazdy z nas ma swoj osobisty komputer, i kazdy z
# nas prawdopodobnie moze miec inna wersje python. Jezyk python ewoluuje non stop. Bardzo czesto jest tak, ze dana jakas
# rzecz, ktora dzialac moze w wersji python 3.12.3 moze nie dzialac na python 3.13. Wobec tego programistom jest ciezko
# pracowac z kims nad jednym projektem, poniewaz kazdy moze miec inna wersje pythona i nie zawsze powiedziane jest, ze
# jezeli jeden programista odpali program na swojej wersji pythona to on bedzie taki sam z wersja ktora wy macie. Co jest
# jeszcze gorsze dla nas - aplikacje komercyjne ktore programisci utrzymuja one bardzo czesto skladaja sie z wiecej niz
# jednego projektu i mozemy natrafic na taka sytuacje ze w jednym projekcie mamy wersje 3.12 w innym 3.06 a w jeszcze
# innym wersje 2.0 pythona. Wszystko nam sie rozjezdza. I oprucz tego pythona rozjezdzac sie nam beda paczki ktore
# zewnetrznie instalujemy.
#       Wiec co musieli bysmy robic za kazdym razem jako programisci pythona? Musielibysmy pracujac sobie nad jednym
# projektem instalowac nowy jezyk, nowa wersje jezyka po czym przeinstalowywac na inna. Byloby to uciazliwe ze wzgledu
# na spowolnienie w pracy przez kolejne instalowanie i reinstalacje.
#       Programisci pythona wpadli na ciekawy koncept, ze nie musimy miec na naszych komputerach globalnych wersji pythona
# (czyli jednej wersji ktora wszyscy maja) i ja przeinstalowywac, tylko mozemy miec takie cos jak:
#
#                                               WIRTUALNE SRODOWISKA
#
#       Jak mamy nasz komputer to mozemy sobie zrobic takie mniejsze wersje symulujace nasze srodowisko programistyczne
# w ktorych bedziemy mieli inne wersje pythona. Wirtualne srodowiska miedzy ktorymi bedziemy sie mogli tylko i wylacznie
# przelaczac i bedziemy mieli automatycznie inna wersje pythona. Nie bedziemy sie musieli martwic o instalacje lub
# przeinstalowywanie jezyka python.
#       Wersje pythona to nie jest jedyny powod dla ktorego my te srodowiska tworzymy. Pracujac nad roznymi programami
# musimy miec zainstalowane bardzo duzo bibliotek zewnetrznych i wielokrotnie jest tez tak ze wersje tych bibliotek
# zewnetrznych niejednokrotnie nie zgadzaja sie nam na tych naszych srodowiskach. dla tego tez tworzymy te nasze
# wirtualne/abstrakcyjne srodowiska w ktorych te nasze aplikacje na naszych komputerach beda odpalane.
#       Jak takie WIRTUALNE SRODOWISKA mozemy sobie tworzyc???
#
#       Wpisujac sobie w terminalu <python> pokaze nam sie informacja ktora wersje mamy zainstalowana.
# Nastepnie wpisujac <exit> wychodzimy z okna komend. Wiemy juz jaka mamy wersje pythona
# Mozemy sobie takie WIRTUALNE SRODOWISKO STWORZYC - robimy to w nastepujacy sposob. Tworzymy wirtualne srodowisko tam
# gdzie aktualnie sie znajdujemy czyli w katalogu kurs_35_piosenka

#       Piszemy w terminalu:
#                               <python -m venv kurs35_intro_venv>
# OBJASNIENIE
#       venv -virtual environment - virtualne srodowisko
#       kurs35_intro_venv - nazwa jak bedzie nazywac sie wirtualne srodowisko stworzone przez nas
#
# w folderze kurs_35_piosenka stworzyl nam sie folder kurs35_intro_venv.
#       Wiec teraz nie wystarczy mi to ze to wirtualne srodowisko bede u siebie posiadali. Jeszcze je trzeba zaktywowac,
# zeby ono bylo uruchomione u mnie w terminalu mojej konsoli. Zeby to uruchomic tzreba wpisac w terminalu
#
# versja linux i mac
#                       <source kurs35_intro_venv/bin/activate>
#
# versia windows - podajemy tylko sciezke do pliku activate
#                       <kurs35_intro_venv/Scripts/activate>
#
# Zeby na poziomie tego termilana wyjsc z WIRTUALNEGO SRODOWISKA wpisujemy
#
#                                   <deactivate>
#
#       Jedna z cech po co my to robimy jest to zebsmy mogli miec rozne wersje pyhona - zebysmy mogli sie szybko przelaczac
# miedzy wersjami z roznymi bibliotekami.
#       Jak instalowac te biblioteki wewnatrz WIRTUALNEGO SRODOWISKA za pomoca pip??? Gdzie te paczki znalezc i jak ich szukac???
#
#       Czym sa zewnetrzne paczki?
#       Wraz z instalacja pythona dostajemy ta nasza standardowa biblioteke, w ktorej sa te nasze poszczegolne standardowe
# biblioteki typu <datetime>, <regex>, <os>, <sys>, ktorych nie musimy dodatkowo instalowac - to sa wbudowane biblioteki,
# z ktorych mozemy automatycznie korzystac. czasami chcielibysmy wykorzystac cos lepszego niz standardowe biblioteki. Dzieki
# temu ze python jest jezykiem open source'owym to rozni programisci potworzyli lepsze wersje, lub biblioteki ktorych nie
# ma standardowej wersji pythona. Dzieki temu mozemy doinstalowywac sobie, dzieki spolecznosci pythonowej jakies zewnetrzne
# biblioteki/paczki, ktorych potem mozemy uzywac.
#       Te zewnetrzne paczki moga byc hostowane w dwojaki sposob. Pierwszy to firmy tworza i maja wlasne paczki na swoj
# wlasny uzytek i nie rozpowszechniaja ich na zewnatrz - mozna je poznac pracujac w srodowisku danej firmy. Drugi sposob
# to taki, ze poznajemy je przez strone:
#
#                                       pypi.org
#
# Jest to strona na ktorej te nasze biblioteki/paczki sie znajduja i dzieki ktorej mozemy za pomoca <pip> te paczki
# instalowac np..
#               Musimy byc w naszym WIRTUALNYM SRODOWISKU
#               Wpisujemy w Google "python requests library" - jeden z linkow powinien byc do pypi.org
#               W lewym gornym rogu pod nazwa biblioteki mamy ramke "pip install requests"
#               Kopjujemy sobie to co jest w tej ramce i wklejamy do terminala i naciskamy enter.
#               Nasza biblioteka source zainstalowala sie do naszego srodowiska wirtualnego
#       W Googloo mozemy napisac "Special libraries for exel in python" i wyskoczy nam kilka roznych stron nie tylko pypi.org
#
#                                           WAZNE!!!!!!!!!!!!
#
#       Kazda biblioteka ma swoja licencje - na uzytek prywatny mozna wykozystac wszystkie - jednak na uzytek komercyjny
# juz nie wszystkie np.
#
# Licencja MIT - ma to do siebie ze jezeli bedziecie chcieli korzystac produkcyjnie to musicie sie zglosic do autorow,
# zeby poprosic ich o uzycie tej biblioteki.
# Licencja Apache Software Licence - jest licencja z ktorej mozemy zawsze korzystac
#
# skoro mamy zainstalowany <request w tym naszym wirtualnym srodowisku to sprobujmy go uruchomic
# tworzymy w folderze <zajecia_7...> plik <requests_test_py>
# Co mozemy zrobic to zaimportowac bezposrednio ta biblioteke piszac w tym pliku
#
# import requests
#
# a nastepnie wywolajmy ta biblioteke piszac to co oni na stronie zasugerowali
#
# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r.status_code)
# print(r.text)
#
# nastepnie przechodzimy do folderu <zajecia_7_Venv_i_pip_skrotowe_operacje_na_dict> dzie nasz ten plik sie znajduje i
# z poziomu terminala uruchamiamy go w nastepujacy sposob:
# python requests_test.py
# Po odczekaniu chwili widzimy ze program zadzialal
#
#               WAZNE!!!!!!!!!!!!!!!
#       Jezeli cos jest zainstalowane w Wirtualnym srodowisku to nie jest zainstalowane w repozytorium globalnie ani w
# innym innym srodowisku wirtualnym, czyli po napisaniu <deactivate> biblioteka/paczka nie bedzie widoczna/dostepna.
#       I teraz pojawia sie pytanie jak sprawdzic, ktore biblioteki w jakim wirtualnym srodowisku sa poinstalowane?
# Aby to sprawdzic musimy byc przelaczeni do tego wirtualnego srodowiska.
# na potrzeby pracy z pip mozemy zrobic taka operacje - przerzucenia tych wszystkich zainstalowanych bibliotek w wirtualnym
# srodowisku do pliku textowego, ktory moze byc widoczny dla kazdego innego programisty. Zeby wszyscy mieli swiadomosc
# jakie poszczegolne biblioteki sa wymagane, zeby ten program z tego wirtualnego srodowiska nam dzialal. Zeby wszyscy
# uzytkownicy mieli takie same wersje tych samych bibliotek.
#
#           W terminalu wpisujemy "pip freeze > requirements.txt"
#
# ten plik zapisze sie w glownej sciezce <kurs_35_piosenka>
#
# wychodziny z wirtualnego srodowiska uzywajac <deactivate> a nastepnie chcemy zainstalowac wszystkie te packi
# jednoczesnie - jak to zrobic?
# przechodzimy do Wirtualnego Srodowiska w ktorym chcemy miec to wszystko zainstalowane lub globalnie i wpisujemy w terminalu
#
#           <pip install -r requirements.txt>
#
# i teraz jak mamy poinstalowane takie same paczki to nasze programy powinny dzialc
#
#
#
#       Mozemy ustawic pyCharm tak zeby odpalal sie automatycznie w wirtualnym srodowisku. Jak to zrobic
# W prawym dolnym rogu mamy Python 3,13 - klikamy lewym przyciskiem myszy - pojawia sie okienko Python Interpreter - klikamy
# Add New Interpreter - Add local Interpreter..
# Pojawi sie okienko "Add Python Interpreter" i w tym okienku mozemy wybrac dwie opcje:
#
# 1. W przypadku gdy juz stworzyliscie sobie wirtualne srodowisko zaznaczamy "Select existing" i znajdujemy sciezke do
# istniejacego juz Wirtualnego srodowiska w ktorym ma sie odpalac automatycznie python
#
# kurs_35_intro_venv - bin - python3,13
#
# dzieki temu w terminalu dodajac nowa zakladke Local (na gorze terminala obok nazwy - add ne tab) automatycznie ta
# zakladka odpali sie w naszym wirtualnym srodowisku
#
#
#
#
#
#                   WAZNE!!!!!!!!!
# do automatycznego przeskaiwania miedzy wersjami pythona - zebysmy nie musieli przeskakiwac i instalowac roznych wersji
# globalnie sluzy nam <pyenv> do versjonowania - na Github jest instrukcja instalacji tego
#
# Po zainstalowaniu - W terminalu wpisujemy
#                           pyenv instal 3.06
# 3.06 - oznacza wersje pythona ktora chcemy zainstalowac ta wersja nie jest instalowana globalnie - jest ona isnatlwana
# na pyenv srodowiskach wirtualnych
# globalnie bedzie tylko wersja 3.13.2
#
# wpisujemy w terminalu
#                           <pyenv virtualenv 3.06 test_3.06>
# automatycznie tworzy wirtualne srodowisko bez tworzenia folderu wirtualnego srodowiska w naszym repozytorium
# Naztepnie wpisujemy w terminalu
#                           <pyenv activate test_3.06>
#          w ten sposob pzreskoczylismy do naszego wirtualnego srodowiska z wersia pythona 3.06
