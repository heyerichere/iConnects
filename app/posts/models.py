from datetime import datetime
from app import db
from app.auth.models import Alum 

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'), nullable=False)

    author = db.relationship('Alum', backref='posts', lazy=True)

    def __repr__(self):
        return f"<Post {self.title}>"