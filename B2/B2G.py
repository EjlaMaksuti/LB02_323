from flask import Flask, jsonify

app = Flask(__name__)


def grussfkt(name):
    return f"Hallo, {name}!"


gespeicherte_funktion = grussfkt


@app.route('/b2g')
def route_beispiel():
    benutzername = "Benutzer"
    ergebnis = gespeicherte_funktion(benutzername)

    return jsonify({'gruss': ergebnis})


if __name__ == '__main__':
    app.run(debug=True)
