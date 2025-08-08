from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dane
lista_ksiazek = [
    {"tytul": "Harry Potter i Kamien Filozoficzny", "autor": "J.K. Rowling", "rok_wydania": 1999,
     "cena": 39.99, "ilosc_na_stanie": 5, "kategoria": "fantazy", "ISBN": "978-3-163148410-0"},
    {"tytul": "Władca Pierścieni: Drużyna Pierścienia", "autor": "J.R.R. Tolkien", "rok_wydania": 1954,
     "cena": 49.99, "ilosc_na_stanie": 3, "kategoria": "fantazy", "ISBN": "978-0-261-10221-7"},
    {"tytul": "Zbrodnia i Kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866,
     "cena": 29.99, "ilosc_na_stanie": 2, "kategoria": "klasyka", "ISBN": "978-3-14-044913-6"},
]
saldo = {'wartosc': 10000}
historia = []

@app.route("/")
def home():
    return render_template("index.html",
                           lista_ksiazek=lista_ksiazek,
                           saldo=saldo['wartosc'],
                           historia=historia)

@app.route("/doladuj", methods=["POST"])
def doladuj():
    kwota = float(request.form["kwota"])
    saldo['wartosc'] += kwota
    historia.append(f"Doładowanie: +{kwota} PLN")
    return redirect(url_for('home'))

@app.route("/wypozycz", methods=["POST"])
def wypozycz():
    isbn = request.form["isbn"]
    for book in lista_ksiazek:
        if book["ISBN"] == isbn and book["ilosc_na_stanie"] > 0:
            book["ilosc_na_stanie"] -= 1
            saldo['wartosc'] += 10
            historia.append(f"Wypożyczenie: {book['tytul']}")
            break
    return redirect(url_for('home'))

@app.route("/zakup", methods=["POST"])
def zakup():
    t = request.form["tytul"]
    a = request.form["autor"]
    c = float(request.form["koszt"])
    i = int(request.form["ilosc"])
    isbn = request.form["isbn"]
    if saldo['wartosc'] >= c * i:
        saldo['wartosc'] -= c * i
        lista_ksiazek.append({
            "tytul": t, "autor": a, "rok_wydania": request.form["rok"],
            "cena": c, "ilosc_na_stanie": i, "kategoria": request.form["kategoria"],
            "ISBN": isbn
        })
        historia.append(f"Zakup: {t}, {i} sztuk")
    else:
        historia.append("Nieudany zakup: saldo niewystarczające")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
