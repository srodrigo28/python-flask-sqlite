from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.Column(db.String(100), unique=False, nullable=False)

@app.route('/')
def index():
    posts = ['Tarefa 1', 'Tarefa 2', 'Tarefa 3']
    return render_template('index2.html', tasks=posts)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)