from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app import login_manager
from app import database

db = database.db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @login_manager.user_loader
    def load_user(self, user_id):
        return self.id