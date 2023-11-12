from flask import Flask, jsonify

app = Flask(__name__)


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def perform_operations(x, y):
    sum_result = add_numbers(x, y)
    product_result = multiply_numbers(x, y)
    return sum_result, product_result


@app.route('/calculate/<int:x>/<int:y>')
def calculate(x, y):
    sum_result, product_result = perform_operations(x, y)
    return jsonify({'sum': sum_result, 'product': product_result})


if __name__ == '__main__':
    app.run(debug=True)
