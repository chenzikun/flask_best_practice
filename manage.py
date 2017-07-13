__author__ = "chenzikunczk@gmail.com"
__version__ = "1.0.0"

import os
from app import create_app
from flask_script import Manager



environment = os.getenv("FLASK_CONFIG") or "default"
app = create_app(environment)

manager = Manager(app)


@manager.command
def test():
    """RUN the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
