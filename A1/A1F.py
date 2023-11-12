from flask import Flask, jsonify

app = Flask(__name__)


def update_salary(employee, new_salary):
    updated_employee = {**employee, 'salary': new_salary}
    return updated_employee


@app.route('/a1f')
def immutable_values():
    employee_data = {'name': 'Lia Marti', 'position': 'Software Engineer', 'salary': 80000}
    new_salary = 90000

    # updaten ohne immutable values
    updated_employee_data = update_salary(employee_data, new_salary)

    return jsonify(
        original_employee=employee_data,
        new_salary=new_salary,
        updated_employee=updated_employee_data
    )


if __name__ == '__main__':
    app.run(debug=True)
