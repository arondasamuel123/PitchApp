# import unittest
# from app.models import Comment,User,Pitch

# class CommentModalTest(unittest.TestCase):
#     def setUp(self):
        
#         self.user_sydo = User(username= 'mark2', email='mark2@gmail.com',password='xyz', profile_image='/photos/mark.png')
#         self.pitch_type = Pitch(category='interview', mintute_pitch=' Pitch Nine', user=self.user_sydo)
#         self.new_comment = Comment(comment= "comment six", pitch =self.pitch_type, user=self.user_sydo)
        
        
#     # def tearDown(self):
        
#     #     User.query.delete()
#     #     Pitch.query.delete()
#     #     Comment.query.delete()
    
    
#     def test_save_comment(self):
#         # import pdb; pdb.set_trace()
#         self.new_comment.save_comment()
#         self.assertTrue(len(Comment.query.all()) > 0)
        
#     def test_isinstance_comment(self):
#         self.assertTrue(isinstance(self.new_comment, Comment))
        
#     def test_get_comment_by_pitch_id(self):
#         self.new_comment.save_comment()
#         get_comms = Comment.get_comments(self.new_comment.pitch_id)
        
#         self.assertEqual(len(get_comms)== 1)
    
    
        