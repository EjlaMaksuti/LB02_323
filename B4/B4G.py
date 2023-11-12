from flask import Flask, jsonify
from functools import reduce

app = Flask(__name__)

zahlen = [2, 4, 6, 8, 10]

quadrierte_zahlen = list(map(lambda x: x**2, zahlen))

gerade_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))

summe_aller_zahlen = reduce(lambda x, y: x + y, zahlen)


@app.route('/b4g')
def funktionen_anwenden():
    return jsonify(
        quadrierte_zahlen=quadrierte_zahlen,
        gerade_zahlen=gerade_zahlen,
        summe_aller_zahlen=summe_aller_zahlen
    )


if __name__ == '__main__':
    app.run(debug=True)
