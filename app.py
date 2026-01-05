from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# python -m pip install flask SQLAlchemy

# Criando uma conexão com um banco
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site2.db'
db = SQLAlchemy(app)

# Criando uma tabela
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)

# Lendo do banco
@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template('index2.html', tasks=tasks)
    
# Executando App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)