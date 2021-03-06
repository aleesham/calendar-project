from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        ## Eventually write a password hashing function

    def __repr__(self):
        return '<User {0}>'.format(self.username)