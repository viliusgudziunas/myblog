from datetime import datetime
from app import db

class Post(db.Model):
    """Model for blog posts"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(400))
    author = db.Column(db.String(36))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Post {}>".format(self.body)
