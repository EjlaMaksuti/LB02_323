from flask import Flask, jsonify

app = Flask(__name__)


def quadrat(x):
    return x ** 2


def double(x):
    return x * 2


@app.route('/a1g')
def rechne():
    zahl = 4
    quadrat_zahl = quadrat(zahl)
    doubled_zahl = double(zahl)

    return jsonify(
        ergebnis1=quadrat_zahl,
        ergebnis2=doubled_zahl
    )


if __name__ == '__main__':
    app.run(debug=True)
