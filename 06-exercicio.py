from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# --- Configuração do Aplicativo e Banco de Dados ---
app = Flask(__name__)

# Define o caminho do banco de dados SQLite (armazenado localmente como site.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Boa prática para economizar recursos

# Instancia o ORM SQLAlchemy para gerenciar o banco de dados
db = SQLAlchemy(app)

# --- Definição do Modelo de Dados (ORM) ---
class Tasks(db.Model):
    """Modelo que representa a tabela de tarefas no banco de dados."""
    id = db.Column(db.Integer, primary_key=True)
    # description: Campo obrigatório (nullable=False) e sem repetições (unique=True)
    description = db.Column(db.String(100), unique=True, nullable=False)

# --- Rotas do Aplicativo ---
@app.route('/')
def index():
    """Rota principal: Busca todas as tarefas e renderiza o template."""
    # Consulta todos os registros da tabela Tasks
    tasks = Tasks.query.all()
    return render_template('index-especial-3.html', tasks=tasks)

# --- Inicialização do Servidor ---
if __name__ == '__main__':
    # Garante que as tabelas sejam criadas dentro do contexto do Flask antes de rodar
    with app.app_context():
        db.create_all()
    
    # Executa o servidor de desenvolvimento na porta 1313
    app.run(port=1313, debug=True)