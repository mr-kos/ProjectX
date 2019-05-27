from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = False)
    surname = db.Column(db.String(64), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(32), unique = False)

    def __repr__(self):
        return '<User %r>' % (self.email)