import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(username='jack123', email='jack@gmail.com', password='123467',profile_image'/photos/jack.png')
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)
        
    def test_isinstance_user(self):
        self.assertTrue(isinstance(self.new_user,User)
                               
    def test_no_access_pass(self):
        with self.assertRaises(AttributeError)
            self.new_user.password
            
    def test_verification_pass(self):
        self.assertTrue(self.new_user.verify_password('1234567'))
        
    def test_instance_variables(self):
        self.assertEqual(self.new_user.username, "jack123")
        self.assertEqual(self.new_user.email,'jack@email.com')
        self.assertEqual(self.new_user.password, '1234567')
        self.assertEqual(self.new_user.profile_image, '/photos/jack.png')
        
        
        