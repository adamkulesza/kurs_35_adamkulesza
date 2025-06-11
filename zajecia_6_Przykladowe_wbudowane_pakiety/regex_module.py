#       regexy beda umozliwialy nam stworzenie paternow, takich przykladow za pomoca ktorych bedziemy mogli porownac czy ten
# nasz napis spelnia nasze zalozenie - np czy adres email jest adresem email
#       w regexach tak samo jak w daytime znaki beda mialy znaczenie, bedziemy mieli D, d, S, s, beda + - itd.
#       Tworzenie regexu wymaga duzej wiedzy wiec najlatwiej o stworzenie regexu poprosic AI
#       regex patterny w pythonie beda wpisywane za pomoca stringa i dodajemy literke <r> przed sringiem (regexem)

#regex dla adresow email
#               regex_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#       ^ znak poczatku tekstu
#       $ znak konca tekstu
#       zeby przetestowac czy nasz regex spelnia nasze zalozenia mozemy skorzystac ze strony:

#                                       www.regex101.com

#       Jak w pythonie mozemy sprawdzic czy to dziala - w pierwszej kolejnosci musimy zaimportowac modul regexowy

import re

# regex_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  -  orginalny regex emaila

regex_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"   #    -  regex bez znaku poczatku <^> i znaku konca <$>
                                                                    #    -  usuwamy te znaki jezeli szukamy danego regexu w wiekszym tekscie
wiersz_o_emailach = """
W cyfrowym swiecie, dzie dane fruwaja,
Maile codziennie skrzynki zalewaja,
Pisze Ada z rana - ada.nowak@poczta.pl,
A potem wiadomosc - od Marka sygnal.

marek123@onet.eu - w tytule "Pilne",
Choc tresc jak zwykle: "spotkajmy sie w Wilnie".
zosia.kwiat@firma.com przysyla fakture,
A admin@bezpiecznie.net - alert o strukturze.

Na koniec robot7@gmail.com pisze: "Hello!",
Choc nikt nie wie, czy to czlowiek, czy AI zgola...
"""
#       majac modul regexowy mozemy sprawdzic czy nasz regex jest validny (czyli czy dany email spelnia warunki i jest emailem

# def is_valid_email(email: str) -> bool:
#     valid_email = re.match(regex_pattern, email)
#     print(valid_email)
#     return valid_email is not None #sprawdzamy czy ten obiekt istnieje - is not None - nie jest niczym

# is_valid_email("<EMAIL>")
# is_valid_email("adfzftswyg@gmailon.com")



# jak znalezc cos w tekscie za pomoca regexu?? szukamy emaili

def is_valid_email(email: str) -> bool:
    valid_email = re.match(regex_pattern, email)
    print(valid_email)
    return valid_email is not None #sprawdzamy czy ten obiekt istnieje - is not None - nie jest niczym

def is_valid_email_in_text(text: str) -> list:
    emails = re.findall(regex_pattern, text)
    print(emails)

validation1 = is_valid_email("<EMAIL>")
print(validation1)
is_valid_email("michal@gmail.com")

emails = is_valid_email_in_text(wiersz_o_emailach)

