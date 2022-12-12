from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 117000333, number2 = 229000333)

@app.route('/mult')
def number():
    var1, var2 = 15210, 38960
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1+var2)


if __name__ == '__main__':
    app.run(debug=True)