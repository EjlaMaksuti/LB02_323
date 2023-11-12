from flask import Flask, jsonify

app = Flask(__name__)


def quadrat(x):
    return x ** 2


def wende_auf_funktion_an(funktion, zahl):
    ergebnis = funktion(zahl)
    return ergebnis


@app.route('/b2f')
def route_beispiel():
    zahl = 5
    quadrat_ergebnis = wende_auf_funktion_an(quadrat, zahl)

    return jsonify({'quadrat_ergebnis': quadrat_ergebnis})


if __name__ == '__main__':
    app.run(debug=True)
