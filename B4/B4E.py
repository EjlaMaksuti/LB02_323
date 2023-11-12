from flask import Flask, jsonify
from functools import reduce

app = Flask(__name__)

wörter = ["Wie", "gehts", "dir", "denn", "so", "heute?"]

wörter_in_grossbuchstaben = list(map(lambda x: x.upper(), wörter))
kurze_wörter = list(filter(lambda x: len(x) <= 3, wörter))
kombinierter_text = reduce(lambda x, y: x + " " + y, wörter)


@app.route('/textverarbeitung')
def textverarbeitung_beispiel():
    return jsonify(
        woerter_in_grossbuchstaben=wörter_in_grossbuchstaben,
        kurze_woerter=kurze_wörter,
        kombinierter_text=kombinierter_text
    )


if __name__ == '__main__':
    app.run(debug=True)
