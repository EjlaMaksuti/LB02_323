from flask import Flask, jsonify

app = Flask(__name__)


class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis


def calculate_discount(preis, rabatt):
    return {'endpreis': preis * (1 - rabatt)}


@app.route('/a1e')
def lösen():
    produkt = Produkt(name='Uhr', preis=1000)
    rabatt_satz = 0.1

    preis_oo = produkt.preis * (1 - rabatt_satz)
    preis_prozedural = produkt.preis * (1 - rabatt_satz)
    preis_funktional = calculate_discount(produkt.preis, rabatt_satz)

    return jsonify(
        preis_oo=preis_oo,
        preis_prozedural=preis_prozedural,
        preis_funktional=preis_funktional
    )


if __name__ == '__main__':
    app.run(debug=True)
