from . import db     

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(255))
    pitch_description = db.Column(db.String(255))

    def __repr__(self):
        return f'Pitch {self.project_name}'