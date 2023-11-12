from flask import Flask, jsonify

app = Flask(__name__)


kombiniere_worte = lambda wort1, wort2: wort1 + wort2
verdopple_buchstabe = lambda buchstabe: buchstabe * 2


@app.route('/stringoperationen/<string:wort1>/<string:wort2>/<string:buchstabe>')
def stringoperationen_route(wort1, wort2, buchstabe):
    ergebnis_kombination = kombiniere_worte(wort1, wort2)
    ergebnis_verdopplung = verdopple_buchstabe(buchstabe)

    return jsonify({'kombination': ergebnis_kombination, 'verdopplung': ergebnis_verdopplung})


if __name__ == '__main__':
    app.run(debug=True)
