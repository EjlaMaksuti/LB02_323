from functools import reduce

from flask import Flask, jsonify

app = Flask(__name__)

namen = ["Mano", "Oliver", "Willy", "Kia"]
namen_laenge = list(map(lambda x: len(x), namen))
namen_mit_e = list(filter(lambda x: 'e' in x.lower(), namen))
namen_laenge_summe = reduce(lambda x, y: x + y, namen_laenge)


@app.route('/b4f')
def funktionen_anwenden():
    return jsonify(
        namen_laenge=namen_laenge,
        namen_mit_e=namen_mit_e,
        namen_laenge_summe=namen_laenge_summe
    )


if __name__ == '__main__':
    app.run(debug=True)
