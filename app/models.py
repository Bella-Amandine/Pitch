from . import db     

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    pitch_description = db.Column(db.String(255))
    project_image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Pitch {self.project_name}'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    password = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'pitch', lazy = "dynamic")


    def __repr__(self):
        return f'User {self.email}'