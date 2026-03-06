import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from models import db, User, Project, ProjectImage

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')
app.config['SQLALCHEMY_DATABASE_HOST'] = os.environ.get('DB_HOST', 'db')
app.config['SQLALCHEMY_DATABASE_PORT'] = os.environ.get('DB_PORT', '5432')
app.config['SQLALCHEMY_DATABASE_USER'] = os.environ.get('DB_USER', 'postgres')
app.config['SQLALCHEMY_DATABASE_PASSWORD'] = os.environ.get('DB_PASSWORD', 'postgres')
app.config['SQLALCHEMY_DATABASE_NAME'] = os.environ.get('DB_NAME', 'portfolio_db')

# Construct Database URL
db_url = f"postgresql://{app.config['SQLALCHEMY_DATABASE_USER']}:{app.config['SQLALCHEMY_DATABASE_PASSWORD']}@{app.config['SQLALCHEMY_DATABASE_HOST']}:{app.config['SQLALCHEMY_DATABASE_PORT']}/{app.config['SQLALCHEMY_DATABASE_NAME']}"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', db_url)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Mail Configuration (Yandex)
app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

# Initialize Extensions
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Basic Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return "Login Page (Coming Soon)"

@app.route('/register')
def register():
    return "Register Page (Coming Soon)"

@app.route('/@<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return f"Profile of {user.username}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
