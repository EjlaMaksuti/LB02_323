from flask import Flask, jsonify

app = Flask(__name__)


def countdown_generator(startwert):
    def countdown():
        nonlocal startwert
        if startwert > 0:
            aktueller_wert = startwert
            startwert -= 1
            return aktueller_wert
        else:
            return "Countdown abgeschlossen!"

    return countdown


@app.route('/countdown')
def starte_countdown():
    countdown_closure = countdown_generator(5)
    countdown_werte = [countdown_closure() for _ in range(6)]

    return jsonify({'countdown_werte': countdown_werte})


if __name__ == '__main__':
    app.run(debug=True)
