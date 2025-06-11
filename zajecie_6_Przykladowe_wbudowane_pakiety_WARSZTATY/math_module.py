# 1. wersja pliku math_module.py

# def add_numbers(number1, number2):
#     return number1 + number2

# 2. wersja pliku math_module.py do testu gdzie swiadomie chcemy zeby wykryl blad i mimo to nam zaliczyl

def add_numbers(number1, number2):
     return int(number1) + int(number2)


#       Do naszych testow mozemy dodac jeszcze takie cos

def format_user_profile(user):
    """
    Zwraca sformatowany profil uzytkownika na podstawie slownika z danymi.
    """
    full_name = f"{user["first_name"]} {user["last_name"]}"
    age = user.get("age", "unknown")
    email = user.get("email", "no email provided")
    is_admin = "Yes" if user.get("is_admin", False) else "No"

    return {
        "full_name": full_name,
        "age": age,
        "email": email,
        "admin": is_admin
    }