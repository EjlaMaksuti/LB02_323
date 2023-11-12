from flask import Flask, jsonify

app = Flask(__name__)


def urspruenglicher_algorithmus(zahlen):
    ergebnis = 0
    for zahl in zahlen:
        ergebnis += zahl
    return ergebnis


def summiere_zahlen(zahlen):
    return sum(zahlen)


def multipliziere_zahlen(zahlen):
    ergebnis = 1
    for zahl in zahlen:
        ergebnis *= zahl
    return ergebnis


@app.route('/b1f')
def funktionale_teilstuecke_anwenden():
    zahlen = [2, 3, 4, 5]

    summe = summiere_zahlen(zahlen)
    produkt = multipliziere_zahlen(zahlen)

    return jsonify(
        urspruenglicher_algorithmus=urspruenglicher_algorithmus(zahlen),
        summe=summe,
        produkt=produkt
    )


if __name__ == '__main__':
    app.run(debug=True)
