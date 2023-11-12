from flask import Flask, jsonify

app = Flask(__name__)


def lineare_suche(liste, element):
    for index, wert in enumerate(liste): #enumerate() gibt index und wert zurück
        if wert == element:
            return index
    return -1


@app.route('/b1g')
def algorithmus_erlaeuterung():
    zahlenliste = [1, 5, 8, 12, 7, 3, 15]

    gesuchte_zahl = 7
    ergebnis_index = lineare_suche(zahlenliste, gesuchte_zahl)

    return jsonify(
        gesuchte_zahl=gesuchte_zahl,
        ergebnis_index=ergebnis_index
    )


if __name__ == '__main__':
    app.run(debug=True)
