from functools import reduce

from flask import Flask, jsonify

app = Flask(__name__)


def urspruenglicher_code(zahlen):
    result = 1
    for zahl in zahlen:
        result *= zahl
    return result


def refaktorierter_code(zahlen):
    return 1 if not zahlen else reduce(lambda x, y: x * y, zahlen)


@app.route('/c1e')
def refactoring_anwenden():
    zahlen = [2, 3, 4, 5]

    # Originaler Code
    ergebnis_urspruenglich = urspruenglicher_code(zahlen)

    # Refaktorierter Code
    ergebnis_refaktoriert = refaktorierter_code(zahlen)

    # Überprüfung der Auswirkungen
    assert ergebnis_urspruenglich == ergebnis_refaktoriert, "Refactoring hat unerwünschte Nebeneffekte!"

    # Rückgabe der Ergebnisse als JSON mit jsonify
    return jsonify(
        ergebnis_urspruenglich=ergebnis_urspruenglich,
        ergebnis_refaktoriert=ergebnis_refaktoriert
    )


if __name__ == '__main__':
    app.run(debug=True)
