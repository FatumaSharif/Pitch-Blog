import unittest
from app.models import Pitch, User
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

  def setUp(self):
    self.user_lelabo = User(username='Lelabo')
