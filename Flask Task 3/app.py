from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_table():
    table_data = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table_data = [(i, i * number) for i in range(1, 11)]
        except ValueError:
            table_data = "Invalid input. Please provide a valid number."

    return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)


