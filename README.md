# Flask Application

У цій лабораторній роботі я працювала з Python 3.8 + pipenv 

## Інсталяція

Встановлюємо [pyenv](https://github.com/pyenv/pyenv) та скачуємо і налаштовуємо версію Python
```bash
pyenv install 3.8.2
pyenv global 3.8.2
```

Через [pip](https://pip.pypa.io/en/stable/) встановлюємо pipenv.

```bash
pip install pipenv
```

У папці репозиторію робимо нове віртуальне середовище

```bash
python -m pipenv install
```

Створюємо файл .gitignore та додаємо в нього наступне
```bash
Pipfile
Pipfile.lock
```

## Запуск Flask

Для початку, через [pip](https://pip.pypa.io/en/stable/) встановлюємо Flask. 
```bash
pip install flask
```
або
```bash
pip install -r requirements.txt
```
## Код Flask програми
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/v1/hello-world-<number>')
def number_display(number):
    return 'Hello, World - ' + number, 200

if __name__ == '__main__':
    app.run()