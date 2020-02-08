from app import create_app,db
from flask_script import Manager, Server
from app.models import User,Pitch,Comment

# app = create_app('development')
app = create_app('test')
manager = Manager(app)
manager.add_command('serve',Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
# def make_shell_context():
#     return dict(app= app, db = db, User = User, Pitch = Pitch, Comment = Comment)


if __name__== '__main__':
    manager.run()

 