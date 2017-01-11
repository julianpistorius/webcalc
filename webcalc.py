from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    return str(int(number1) + int(number2))


@app.route('/div/<number1>/<number2>')
def div(number1, number2):
    return str(int(number1) / int(number2))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
