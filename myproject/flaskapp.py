from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/hello-world-<number>')
def number_display(number):
    return 'Hello, World - ' + number, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')