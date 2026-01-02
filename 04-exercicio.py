# Iniciando com SQLite criando Instância e tabela

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    tasks = ['Tarefa 1', 'Tarefa 2', 'Tarefa 3']
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=1313, debug=True)