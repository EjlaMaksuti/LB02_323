from flask import Flask, jsonify
from functools import reduce

app = Flask(__name__)

zahlen = [1, 2, 3, 4, 5]

quadrierte_zahlen = list(map(lambda x: x**2, zahlen))
gerade_zahlen = list(filter(lambda x: x % 2 == 0, quadrierte_zahlen))
summe_aller_zahlen = reduce(lambda x, y: x + y, gerade_zahlen)


@app.route('/b4f')
def kombinierte_funktionen_anwenden():
    return jsonify(
        quadrierte_zahlen=quadrierte_zahlen,
        gerade_zahlen=gerade_zahlen,
        summe_aller_zahlen=summe_aller_zahlen
    )


if __name__ == '__main__':
    app.run(debug=True)
