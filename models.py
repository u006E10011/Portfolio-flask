from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import re

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256))
    
    # Profile info
    avatar = db.Column(db.String(256), default='default_avatar.png')
    bio = db.Column(db.Text)
    skills = db.Column(db.JSON, default=list)  # Store as list of strings
    contacts = db.Column(db.JSON, default=dict) # Store as {platform: url}
    
    # Auth & Verification
    is_verified = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(5))
    code_expires_at = db.Column(db.DateTime)
    
    # Security (Lockout)
    failed_attempts = db.Column(db.Integer, default=0)
    lockout_until = db.Column(db.DateTime)
    
    # Relationships
    projects = db.relationship('Project', backref='author', lazy='dynamic', cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def validate_username(username):
        # Only English letters, numbers and underscores
        return re.match(r'^[a-zA-Z0-9_]+$', username) is not None

    def is_locked(self):
        if self.lockout_until and self.lockout_until > datetime.utcnow():
            return True
        return False

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    stack = db.Column(db.JSON, default=list) # List of technologies
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    images = db.relationship('ProjectImage', backref='project', lazy='dynamic', cascade="all, delete-orphan")

class ProjectImage(db.Model):
    __tablename__ = 'project_images'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    image_path = db.Column(db.String(256), nullable=False)
    is_main = db.Column(db.Boolean, default=False) # For Unity Asset Store style gallery
