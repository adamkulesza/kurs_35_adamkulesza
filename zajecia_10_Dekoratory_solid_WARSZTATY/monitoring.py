# 1.
# Tutaj napiszemy swoj wlasny dekorator.
# Jak wyglada dekorator??
# Dekorator przyjmowal jako argument ta nasza funkcje.
# Przyjmujac ta funkcje jako nasz argument, my wewnatrz niego musielismy pisac cos takiego jak nasz wrapper (to nasze
# opakowanie, ktore mielismy) - w tym wraperze mozemy pisac cokolwiek ale w pewnym momencie bedziemy musieli wykonac ta
# nasza funkcje.
#        func(*args, **kwargs)
#        print("function execution completed.")
# Na samym koncu bedziemy musieli ten nasz wrapper zwrocic. <return wrapper>
# to jest podstawowa struktura czym ten dekorator jest
# Wracamy do pliku lotnisko do punktu #2.

# def monitor(func):
#     """
#     Decorator that monitors the execution time of a function.
#     """
#     def wrapper(*args, **kwargs):
#         print("Starting executing of the function...")
#         result = func(*args, **kwargs)
#         print("function execution completed.")
#         return result
#     return wrapper

# 3. Importujemy sobie
import time
from datetime import datetime
# chcemy zmierzyc czas trwania tej funkcji, chcemy przekazac nazwe tej funkcji, i chcemy przekazac argumentu, ktore
# podalismy, zeby wiedziec co sie w tych logach dzieje
# wiec do dekoratora dopisujemy:
# <start_time = time.time()>
# usuwamy print("Starting executing of the function...") i print("function execution completed.")
# zmieniamy nasz dekorator w nastepujacy sposob
# tworzymy plik monitoring.log


def monitor(func):
    """
    Decorator that monitors the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_datetime = datetime.now()
        try:
            result = func(*args, **kwargs)
            status = "Success"
            return result
        except Exception as e:
            status = f"Error: {e}"
        finally:
            end_time = time.time()
            duration = end_time - start_time
            log_line = (
                f"{start_datetime} - Function '{func.__name__}'"
                f"executed in {duration:.4f} seconds."
                f" Arguments: {args}, {kwargs},"
                f"Status: {status}"
            )
            with open("monitoring.log", "a") as log:
                log.write(log_line + "\n")
    return wrapper

# Majac ta funkcje ktora mamy i majac to dodane do tego lotniska - uruchamiajac teraz to lotnisko