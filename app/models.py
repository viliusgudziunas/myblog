from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class User(UserMixin, db.Model):
    """ Model for users"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        """Password setter"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Password checker"""
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    """Loads a user given the ID"""
    return User.query.get(int(id))

class Post(db.Model):
    """Model for blog posts"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(400))
    author = db.Column(db.String(36))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Post {}>".format(self.body)
