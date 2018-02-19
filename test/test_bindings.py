import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from seaborn_file.file import clear_path
from example_flask_app.settings.global_import import setup_flask

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
EXPECT_DIR = os.path.join(BASE_DIR, 'example_bindings')
RESULT_DIR = os.path.join(BASE_DIR, 'example_flask_app',
                          'bindings', 'python_bindings')


class test_bindings(unittest.TestCase):
    def startTestRun(self):
        clear_path(RESULT_DIR)
        setup_flask.create_python_bindings()

    def compare_files(self, filename):
        with open(os.path.join(EXPECT_DIR, filename), 'r') as fp:
            expected = fp.read()
        with open(os.path.join(RESULT_DIR, filename), 'r') as fp:
            result = fp.read()
        self.assertEqual(expected, result)

    def test_connection(self):
        self.compare_files('connection.py')

    def test_account(self):
        self.compare_files('account.py')

    def test_account_access(self):
        self.compare_files('account_access.py')

    def test_account_transfer(self):
        self.compare_files('account_transfer.py')

    def test_echo(self):
        self.compare_files('echo.py')

    def test_user(self):
        self.compare_files('user.py')

    def test_init(self):
        self.compare_files('__init__.py')


if __name__ == '__main__':
    unittest.main()
