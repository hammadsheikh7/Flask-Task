from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def square_number():
    result = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = number ** 2
        except ValueError:
            result = "Invalid input. Please provide a valid number."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
