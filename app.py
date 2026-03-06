import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных
# Если запущено в Docker, берем DATABASE_URL из окружения, иначе используем локальный SQLite для тестов
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Пример модели данных
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Создаем таблицы при запуске (в реальных проектах лучше использовать миграции)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)