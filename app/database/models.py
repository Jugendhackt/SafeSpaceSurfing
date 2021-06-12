from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Facility(db.Model):
    __tablename__ = 'facility'
    f_id = db.Column(db.Integer, primary_key=True)
    osm_id = db.Column(db.String(100))
    geolocation = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    #owner_id = db.Column(db.Integer, db.ForeignKey('users.u_id'), nullable=False)
    #owner = db.relationship('Facilities', backref=db.backref('users', lazy=True))

    def __init__(self, osm_id, **kwargs):
        super().__init__(**kwargs)
        self.osm_id = osm_id


    def __repr__(self):
        return '<Facility %r>' % self.osm_id



class User(db.Model):
    __tablename__ = 'user'
    #Table attributes
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
