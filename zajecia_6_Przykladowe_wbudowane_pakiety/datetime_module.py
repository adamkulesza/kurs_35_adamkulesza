# 1. Pierwszy sposob

# import datetime
#
# print(datetime.date.today())
# print(datetime.datetime.today())


# 2.
# Mozna tez zrobic to w taki sposob

from datetime import datetime, timedelta
print(datetime.today())                             # data dzisiejsza
tomorrow = datetime.today() + timedelta(days=1)     # data jutrzejsza
print(tomorrow)


# Jezeli chcieli bysmy pobrac date od uzytkownika to piszemy

twoja_data_urodzin = input("Podaj date twoich urodzin (YYYY-MM-DD): ")
print(twoja_data_urodzin)
print(type(twoja_data_urodzin))

#       Dosyc czesto uzytkownicy w momencie kiedy beda nam podawali jakies wartosci, albo te wartosci beda przychodzily do nas
# z jakich zewnetrznych aplikacji, one beda w formacie string, np.
# Bedziemy sobie rozmawiali sobie o protokole HTTP i o tych formatach .json no to tam dostajac jakies zewnetrzne timestumpy
# (czyli odciski czasu w ktorym cos zostalo wykonane) nie bedziemy dostawac tych odciskow w obiektach daytimowych tylko juz
# bedziemy je dostawali za pomoca stringow. Wiec co bedziemy musieli zrobic nmy jako programisci backendowi?? Bedziemy
# musieli przeksztalcic te nasze stringi na nasze obiekty.
# Zeby to zrobic bedziemy musieli skorzystac z czegos takiego jak <strptime>

data_urodzin_obiekt = datetime.strptime(twoja_data_urodzin, "%Y-%m-%d") # przeksztalcenie stringa na obiekt datetime -dzieki temu mamy ta date juz w typie datetime
print(type(data_urodzin_obiekt))

"""
%d - dzien (01-31)
%m - miesiac (01-12)
%Y - rok (pelny, np 2023)
%y - rok (dwoletni, np. 23)
%H - godzina (00-23)
%M - minuty (00-59)
%S - sekundy (00-59
"""

format_amerykanski = "%m/%d/%Y %H:%M:%S"

obiekt_w_formacie_amerykanskim = datetime.strptime("12/22/2022 12:01:02", format_amerykanski) # przeksztalcenie stringa na obiekt datetime -dzieki temu mamy ta date juz w typie datetime
print(obiekt_w_formacie_amerykanskim)

# iso_format = datetime.fromisoformat(twoja_data_urodzin) # iso_format jest formatem daty uzywanym w Europie YYYY-MM-DD
#                                                         # w Stanach jest uzywany MM-DD-YYYY

#       Mozemy tez robic to w druga strone - za amerykanskiego na europejski
twoja_data_urodzin_po_amerykansku = datetime.strftime(data_urodzin_obiekt, format_amerykanski)
print(twoja_data_urodzin_po_amerykansku)