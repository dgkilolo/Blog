from app import create_app
from flask_script import Manager,Server
# from app.models import User, Pitch, Comment
# from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')

manager = Manager(app)
# migrate = Migrate(app,db)

manager.add_command('server',Server)
# manager.add_command('db', MigrateCommand)


@manager.command
def test():
  """Run the Unit Test"""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch=Pitch, Comment=Comment )


if __name__ == '__main__':
    manager.run()