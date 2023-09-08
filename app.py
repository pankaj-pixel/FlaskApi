from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"

@app.route('/data')
def emp_data():
    return "HERE IS THE DATA OF EMPLOYEE "

@app.route('/<name>')
def printname():
    return 'hi ,{}'.format(name)


if __name__ == '__main__':
    app.run(debug=True)