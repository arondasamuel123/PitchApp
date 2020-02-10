# import unittest
# from app.models import Pitch,User
# class PitchModelTest(unittest.TestCase):
    
#     def setUp(self):
#         self.user_new = User(username='jane123', email='jane@gmail.com', password='abcdef', profile_image='/photos/profile.png')
#         self.new_pitch = Pitch(category='promotion',mintute_pitch='This is the best pitch', user=self.user_new)
        
        
#     def tearDown(self):
#         Pitch.query.delete()
#         User.query.delete()
        
    
#     def test_instance_pitch(self):
#         self.assertTrue(isinstance(self.new_pitch, Pitch))
    
#     def test_save_pitch(self):
#         self.new_pitch.save_pitch()
#         self.assertTrue(len(Pitch.query.all())>0)
        
#     def test_get_pitch_by_category(self):
#         self.new_pitch.save_pitch()
#         got_pits = Pitch.get_pitches('promotion')
#         self.assertEqual(len(got_pits)==  1)
        
   