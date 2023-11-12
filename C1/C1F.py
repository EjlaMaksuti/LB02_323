from flask import Flask, jsonify

app = Flask(__name__)

# Beispiel-Funktion vor dem Refactoring
def komplexer_code(zahlen):
    ergebnis = 0
    for zahl in zahlen:
        if zahl % 2 == 0:
            ergebnis += zahl ** 2
    return ergebnis

# Refaktorierte Funktion für bessere Lesbarkeit
def klarer_code(zahlen):
    gerade_zahlen = filter_nach_geraden(zahlen)
    quadrierte_zahlen = quadriere(gerade_zahlen)
    ergebnis = summiere(quadrierte_zahlen)
    return ergebnis

def filter_nach_geraden(zahlen):
    return filter(lambda x: x % 2 == 0, zahlen)

def quadriere(zahlen):
    return map(lambda x: x ** 2, zahlen)

def summiere(zahlen):
    return sum(zahlen)

@app.route('/c1f')
def route_beispiel():
    # Verwendung der refaktorierten Funktion
    zahlen = [1, 2, 3, 4, 5]
    ergebnis = klarer_code(zahlen)
    return jsonify({'result': ergebnis})


if __name__ == '__main__':
    app.run(debug=True)
