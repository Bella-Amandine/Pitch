import unittest
from ..models import Pitch
from .. import db

class PitchTest(unittest.TestCase):
    '''
    A class to test CRUD operation on Pitch Model
    '''

    def SetUp(self):
        self.new_pitch = Pitch(project_name = "Hello World", pitch_description = "blablablabla blaalbal")

    def create_pitch_test(self):
        db.session.add(self.new_pitch)
        db.session.commit()
        saved_pitch = Pitch.query.filter_by(project_name = "Hello World").first()
        self.assertEqual("Hello World", saved_pitch.project_name)

        