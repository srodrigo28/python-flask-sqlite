# 1. Importação das bibliotecas necessárias
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# 2. Configuração da aplicação Flask e do banco de dados
app = Flask(__name__)

# 3. Configura o caminho do banco de dados SQLite (será criado na pasta do projeto)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# 4. Cria a instância do SQLAlchemy vinculada à aplicação Flask
db = SQLAlchemy(app)

class Tasks(db.Model): # 5. Definição do modelo (tabela) de tarefas
    id = db.Column(db.Integer, primary_key=True) # ID único autoincrementável
    description = db.Column(db.String(100), unique=True, nullable=False)

# 6. Rota principal da aplicação
@app.route('/')
def index(): # Página inicial: lista todas as tarefas cadastradas.
    tasks = Tasks.query.all()
    
    # Renderiza o template HTML passando a lista de tarefas
    return render_template('index-especial-3.html', tasks=tasks)

# 7. Inicialização do banco de dados e execução da aplicação
if __name__ == '__main__':
    # Garante que o contexto da aplicação esteja ativo para operações com o banco
    with app.app_context():
        # Cria o arquivo do banco e as tabelas (se ainda não existirem)
        db.create_all()
        # Inicia o servidor de desenvolvimento na porta 1313 com modo debug ativado
    app.run(port=1313, debug=True)