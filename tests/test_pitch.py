import unittest
from app.models import Pitch,User

class PitchModelTest(unittest.TestCase):
    
    def setUp(self):
        self.user_new(username='jane123', email='jane@gmail.com', password='abcdef', profile_image='/photos/profile.png')
        self.new_pitch = Pitch('promotion','This is the best pitch', user=self.user_new)
        
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        
    
    def test_instance_pitch(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))
    
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertEqual(len(Pitch.query.all())>0)
        
    def test_get_pitch_by category(self):
        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches('promotion')
        self.assertEqual(len(got_pitches)==  1)
        
    def test_instances_variables(self):
        self.assertEqual(self.new_pitch.category, 'promotion')
        self.assertEqual(self.new_pitch.minute_pitch, 'This is the best pitch')
        self.assertEqual(self.new_pitch.user, self.user_new)
        
  
        