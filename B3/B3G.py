from flask import Flask, jsonify

app = Flask(__name__)

quadriere = lambda x: x ** 2
konvertiere_grossbuchstaben = lambda s: s.upper()


@app.route('/b3g')
def lambda_ausdruecke():
    zahl = 5
    text = "hallo"

    ergebnis_quadrieren = quadriere(zahl)
    ergebnis_grossbuchstaben = konvertiere_grossbuchstaben(text)

    return jsonify(
        ergebnis_quadrieren=ergebnis_quadrieren,
        ergebnis_grossbuchstaben=ergebnis_grossbuchstaben
    )


if __name__ == '__main__':
    app.run(debug=True)
