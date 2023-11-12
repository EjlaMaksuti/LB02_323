from flask import Flask, jsonify

app = Flask(__name__)


def filtere_positive_zahlen(zahlen):
    result = []
    for zahl in zahlen:
        if zahl > 0:
            result.append(zahl)
    return result

# Verbesserte Funktion mit verbesserten Namen und Kommentaren
def filtere_positive_zahlen_refaktorisiert(zahlen):
    """
    Filtert positive Zahlen aus einer Liste von Zahlen.
    :param zahlen: Liste von Zahlen
    :return: Liste von positiven Zahlen
    """
    positive_zahlen = [zahl for zahl in zahlen if zahl > 0]
    return positive_zahlen


@app.route('/c1g')
def route_beispiel():
    # Verwendung der refaktorierten Funktion
    zahlen = [1, -2, 3, -4, 5]
    ergebnis_json = jsonify({'positive_zahlen': filtere_positive_zahlen_refaktorisiert(zahlen)})
    return ergebnis_json


if __name__ == '__main__':
    app.run(debug=True)
