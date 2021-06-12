from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

class Facility(db.Model):
    __tablename__ = 'facility'
    f_id = db.Column(db.Integer, primary_key=True)
    osm_id = db.Column(db.String(100))
    osm_admin_lvl5 = db.Column(db.String(1000))
    osm_admin_lvl6 = db.Column(db.String(1000))
    osm_admin_lvl9 = db.Column(db.String(1000))
    osm_admin_lvl10 = db.Column(db.String(1000))
    geolocation = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    #owner_id = db.Column(db.Integer, db.ForeignKey('users.u_id'), nullable=False)
    #owner = db.relationship('Facilities', backref=db.backref('users', lazy=True))

    def __init__(self, osm_id, lvl5, lvl6, lvl9, lvl10, **kwargs):
        super().__init__(**kwargs)
        self.osm_id = osm_id
        self.osm_admin_lvl5 = lvl5
        self.osm_admin_lvl6 = lvl6
        self.osm_admin_lvl9 = lvl9
        self.osm_admin_lvl10 = lvl10


    def __repr__(self):
        return '<Facility %r>' % self.osm_id



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    #Table attributes
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __init__(self, username, password, is_admin, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.name

@login.user_loader
def load_user(id):
    return User.query.get(int(id))