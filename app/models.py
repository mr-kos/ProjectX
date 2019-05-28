from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = False)
    surname = db.Column(db.String(64), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(128), unique = False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id) # python 2
        except NameError:
            return str(self.id) # python 3

    def __repr__(self):
        return 'User ' + self.email

@login.user_loader
def load_user(id):
    return User.query.get(int(id))