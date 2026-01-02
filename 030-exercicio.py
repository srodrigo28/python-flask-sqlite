from flask import Flask, render_template
from livereload import Server  # Nova importação

app = Flask(__name__)

@app.route('/')
def index():
    tasks = ['Tarefa 1', 'Tarefa 2', 'Tarefa 3', 'Tarefa 4', 'Tarefa 5', 'Tarefa 6', 'Tarefa 7']
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    
    # Observa mudanças nos arquivos
    server.watch('templates/**/*.html')  # templates HTML
    server.watch('static/**/*')          # CSS, JS, imagens etc.
    server.watch('*.py')                 # arquivos Python (reinicia o servidor)
    
    # Roda o servidor USANDO o livereload (não use app.run aqui!)
    server.serve(port=1313, host='127.0.0.1', debug=True)