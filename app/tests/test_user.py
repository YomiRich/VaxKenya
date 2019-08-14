import unittest
from app.models import User

class UserTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(password = '1234')
    
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def tes_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('1234'))            
