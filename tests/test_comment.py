import unittest
from app.models import Comment,User,Pitch

class CommentModalTest(unittest.TestCase):
    def setUp(self):
        
        self.user_sydo = User(username= 'sydo123', email='sydo@gmail.com',password='420', profile_image='/photos/sydo.png')
        self.pitch_type = Pitch(category='promotion', pitch='Promotion Pitch', user=self.user_sydo)
        self.new_comment = Comment(comment= "comment of a pitch",pitch=pitch_type, user=self.user_sydo)
        
        
    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()
    
    
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertEqual(len(Comment.query.all()) > 0)
        
    def test_isinstance_comment(self):
        self.assertTrue(isinstance(self.new_comment, Comment))
        
    def test_get_comment_by_pitch_id(self):
        self.new_comment.save_comment()
        get_comments = Comment.get_comments(1)
        
        self.assertEqual(len(get_comments)== 1)
    
    def test_instance_variables(self):
        self.assertEqual(self.new_comment.comment, "comment of promotion pitch")
        self.assertEqual(self.new_comment.user, self.user_sydo )
        self.assertEqual(self.new_comment.pitch, self.pitch_type)
        
        