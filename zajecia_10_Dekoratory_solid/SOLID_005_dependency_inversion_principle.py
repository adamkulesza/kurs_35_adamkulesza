# D - dependency inversion principle

# mamy wlacznik
# mamy Lampe ledowa

# class Ledlamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("lED lamp is turned on")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("LED lamp is turned off.")
#
#
#
# # ten nasz wlacznik bedzie mial w metodzie inicjalizujacej <lamp> i ta lampa bedzie nasza <Ledlamp>
# class LightSwitch:
#     def __init__(self, ):
#         self.lamp = Ledlamp()
#
#     def switch_light(self):
#         if not self.lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
# # dodajemy
#
# switch = LightSwitch()
#
# switch.switch_light() #Turn on the LED lamp
# switch.switch_light() #Turn off the LED lamp



# Jaki problem mamy tutaj w tym naszym rozwiazaniu??
# W mieszkaniach czy tam domach nie mamy tylko i wylacznie zarowek ledowych, mamy rozne - jazeniowe, neony, xeony itp.
# W tym momencie w tej impementacji, ktora my teraz zrobilismy, ten <switch_light> zalezy tylko i wylaczne od tej lampy
# ledowej. Wiec zebysmy zrobili sobie polaczenie znowu wlacznik - swiatlo no to musimy nie dosc ze zaimplementowac
# <KsenonLamp> patrz punkt 1. to rowniez musieli bysmy sobie zrobic <KsenonLightSwitch> - patrz punkt 2.
# Przez to ze mamy to tak rozwiazane to ilosc naszego kodu wzrasta. Poniewaz te nasze klasy <LightSwitch> i
# <KsenonLightSwitch> w zaleznosciach ktore tu wrzucilismy w tych dependencjach one zaleza od konkretnej implementacji.
# Zaleza od implementacji <LedLamp> lub <KsenonLamp>. To sa faktyczne implementacje jakichs naszych klas.



# class Ledlamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("lED lamp is turned on")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("LED lamp is turned off.")
#
#
# # 1.
# class Ksenonlamp:
#     def __init__(self):
#         self.turned_on = False
#
#     def turn_on(self):
#         self.turned_on = True
#         print("Ksenon lamp is turned on.")
#
#     def turn_off(self):
#         self.turned_on = False
#         print("Ksenon lamp is turned off")
#
#
# class LightSwitch:
#     def __init__(self, ):
#         self.lamp = Ledlamp()
#
#     def switch_light(self):
#         if not self.lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
# # 2.
# class KsemonLightSwitch:
#     def __init__(self):
#         self.lamp = Ksenonlamp()
#
#     def switch_light(self):
#         if not self. lamp.turned_on:
#             return self.lamp.turn_on()
#         else:
#             return self.lamp.turn_off()
#
#
# switch = LightSwitch()
#
# switch.switch_light()  # Turn on the LED lamp
# switch.switch_light()  # Turn off the LED lamp



#   A co my chcemy zrobic - my chcieli bysmy zgodnie z zasada dependency inversion, zeby te nasze klasy ktore definiujemy
# nie zalezaly strikte od jakichs naszych implementacji, tylko zeby zalezaly od abstrakcji. Po to, zebysmy potem
# korzystajac z polimorfizmu mogli sobie dobudowywac to nie wplywajac juz na ten stan. Bo korzystajac z polimorfizmu, z
# liskov substytution mozemy dodawac sobie kolejne nasze zrodla swiatla.
# Jak to zrobimy??

#importujemy metody abstrakcyjne
from abc import ABC, abstractmethod

# robimy klase abstrakcyjna <LightSource>, ktora bedzie miala turn_off i turn_on
class LightSource:
    def __init__(self):
        self.turned_on = False

    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# robimy sobie znowu klase <Switch>, ktora bedzie przyjmowala tego <light_source>, ktora nie bedzie klasa
# abstrakcyjna tylko bedzie wykonywalo metode
class Switch:

    def __init__(self, light_source: LightSource):
        self.light_source = light_source

    def switch_light(self):
        if not self.light_source.turned_on:
            return self.light_source.turn_on()
        else:
            return self.light_source.turn_off()

# Roznica jest taka miedzy poprzednim rozwiazanie <LightSwitch> a tym <Switch ze teraz mozemy:

class KsenonLamp(LightSource):
    def turn_on(self):
        self.turned_on = True
        print("Ksenon lamp is turned on")

    def turn_off(self):
        self.turned_on = False
        print("Ksenon lamp is turned off.")

class LedLamp(LightSource):
    def turn_on(self):
        self.turned_on = True
        print("Led lamp is turned on")

    def turn_off(self):
        self.turned_on = False
        print("Led lamp is turned off.")

class HalogenLamp(LightSource):
    def turn_on(self):
        self.turned_on = True
        print("Halogen lamp is turned on")

    def turn_off(self):
        self.turned_on = False
        print("Halogen lamp is turned off.")

# Dodajac sobie nasze rzeczy i dzieki temu, ze nasza zaleznosc nie polega na konkternej implementacji, tylko polega na
# abstrakcji to mozemy sobie zrobic:

switch1 = Switch(LedLamp())
switch2 = Switch(HalogenLamp())
switch3 = Switch(KsenonLamp())

switch1.switch_light() # Turns on the LED lamp
switch1.switch_light() # Turns off the LED lamp
switch2.switch_light() # Turns on the Halogen lamp
switch2.switch_light() # Turns off the Halogen lamp
switch3.switch_light() # Turns on the Ksenon lamp
switch3.switch_light() # Turns off the Ksenon lamp

# dzieki temu zmniejszylismy bardzo ilosc kodu
# dzieki temu ze zalezymy od abstrakcji a nie zalezymy od konkretnej implementacji, to tylko i wylacznie bedziemy
# dodawali kolejne dzieci, kolejne konkretne implementacje tej klasy abstrakcyjnej, zamiast tworzyc kolejne schematy
# polaczen.