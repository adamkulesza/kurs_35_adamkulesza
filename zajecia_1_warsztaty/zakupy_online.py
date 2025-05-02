"""
Zakupy online - rabaty
Wczytaj od urzytkownika:
- czy zamowienie przakracza 100zl (tak/nie)
- czy jest klientem VIP (tak/nie)
- czy kulił produkt promocyjny (tak/nie)

Rabat:
- 15% jesli zamowienie > 10 zł lub VIP
- dodatkowo 5% jesli produkt promocyjny.

Wyswietl "twoj rabat wynosi x%" bez ifow.
"""


###################### program instruktora #################

# zamowienie = input("czy zamowienie przekracza 100 zł?: ")
# zamowienie = zamowienie.lower()
#
# vip = input("czy jestes klientem VIP? (tak/nie): ")
# vip = vip.lower()
#
# promocja = input("czy kupiles produkt promocyjny? (tak/nie): ")
# promocja = promocja.lower()
#
# zamowienie_powyzej_100 = zamowienie == "tak"
# klient_vip = vip == "tak"
# produkt_promocyjny = promocja == "tak"
#
# rabat = 0.15 * (zamowienie_powyzej_100 or klient_vip) + 0.05 * produkt_promocyjny
# print(f"Twoj rabat wynosi {rabat * 1:.0%}")


############################# inaczej zrobione zadanie ########
zamowienie = float(input("Podaj cene swojego zamowienia: "))

vip = input("czy jestes klientem VIP? (tak/nie): ")
vip = vip.lower()

promocja = input("czy kupiles produkt promocyjny? (tak/nie): ")
promocja = promocja.lower()

zamowienie_powyzej_100 = zamowienie >= 100
klient_vip = vip == "tak"
produkt_promocyjny = promocja == "tak"

rabat = 0.15 * (zamowienie_powyzej_100 or klient_vip) + 0.05 * produkt_promocyjny
print(f"Twoj zamowienie po rabatowaniu wynosi: {zamowienie * (1 - rabat)}")
