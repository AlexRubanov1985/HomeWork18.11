from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jjjjjjjjj'


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        number1_str = request.form.get('number1')
        number2_str = request.form.get('number2')
        operation = request.form.get('operation')

        try:
            number1 = float(number1_str)
            number2 = float(number2_str)

            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            else:
                flash("Недействительная операция!", "error")
                return redirect(url_for('form'))

            print(f"Рассчитанный результат: {result}")
            return redirect(url_for('result', result=result))

        except ValueError:
            flash("Пожалуйста, введите корректные числа!", "error")
            return redirect(url_for('form'))

    return render_template('form.html')


@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)