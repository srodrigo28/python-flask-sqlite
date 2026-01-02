from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tasks = ['Tarefa 1', 'Tarefa 2', 'Tarefa 3']
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(port=1313, debug=True)