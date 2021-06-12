from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Facilities(db.Model):
    __tablename__ = 'facilities'
    f_id = db.Column(db.Integer, primary_key=True)
    osm_id = db.Column(db.String())
    geolocation = db.Column(db.String())
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.u_id'), nullable=False)
    owner = db.relationship('Facilities', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<Playlistname %r>' % self.name



class Users(db.Model):
    __tablename__ = 'users'
    #Table attributes
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return '<Titlename %r>' % self.name
