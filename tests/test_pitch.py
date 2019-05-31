import unittest
from app.models import Pitch,User
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_Lelabo = User(username = 'Lelabo',password = '123Pass', email = 'mail@lelabo.com')
        self.new_pitch = Pitch(pitch_id=12345,pitch_title='Pitch Title'user = self.user_Lelabo )


    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch)
        self.assertEquals(self.new_pitch.pitch_title,'Pitch Title')
        self.assertEquals(self.new_pitch.user,self.user_Lelabo)


    def test_save_pitch(self):
        self.new_review.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)


    def test_get_pitch_by_id(self):

        self.new_review.save_pitch()
        got_reviews = Pitch.get_pitch(12345)
        self.assertTrue(len(got_pitch) == 1)