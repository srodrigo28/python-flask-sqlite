# primeiros passos com flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundo!'

if __name__ == '__main__':
    app.run(debug=True, port=1313)