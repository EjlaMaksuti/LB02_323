from flask import Flask, jsonify

app = Flask(__name__)

benutzer = [
    {'name': 'Mila', 'alter': 8},
    {'name': 'Kilian', 'alter': 37},
    {'name': 'Barbara', 'alter': 23},
    {'name': 'Tina', 'alter': 20}
]


@app.route('/sortiere_benutzer_nach_alter')
def sortiere_benutzer_nach_alter():
    sortierte_benutzer = sorted(benutzer, key=lambda x: x['alter'])

    return jsonify(sortierte_benutzer)


if __name__ == '__main__':
    app.run(debug=True)
