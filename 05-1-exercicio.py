from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # 1. Chama o Flask criando instancia
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) 

class Tasks(db.Model): # 2. Definição do modelo (tabela) de tarefas
    id = db.Column(db.Integer, primary_key=True) # ID único autoincrementável
    description = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/') # Define a rota raiz
def index(): # Página inicial: lista todas as tarefas cadastradas.
    tasks = Tasks.query.all()
    
    return render_template('index-especial-3.html', tasks=tasks) # Mapea o HTML
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=1313, debug=True) # Roda aplicação