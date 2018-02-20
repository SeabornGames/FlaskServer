import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from seaborn_file.file import clear_path, file_list
from example_flask_app.settings.global_import import setup_flask

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
EXPECT_DIR = os.path.join(BASE_DIR, 'example_bindings')
RESULT_DIR = os.path.join(BASE_DIR, 'example_flask_app', 'bindings')


class TestBindings(unittest.TestCase):
    def compare_files(self, file):
        with open(file, 'r') as fp:
            expected = fp.read()
        with open(file.replace(EXPECT_DIR, RESULT_DIR), 'r') as fp:
            result = fp.read()
        self.assertEqual(expected, result, file.replace(EXPECT_DIR, ''))


    def test_python_bindings(self):
        clear_path(os.path.join(RESULT_DIR, 'python_bindings'))
        setup_flask.create_python_bindings()
        path = os.path.join(EXPECT_DIR, 'python_bindings')
        for file in file_list('*.*', path):
            if sys.version_info[0] == 2:
                self.compare_files(file)
            else:
                with self.subTest(file.replace(EXPECT_DIR, '')):
                    self.compare_files(file)

    def test_unity_bindings(self):
        clear_path(os.path.join(RESULT_DIR, 'unity_bindings'))
        setup_flask.create_python_bindings()
        path = os.path.join(EXPECT_DIR, 'unity_bindings')
        for file in file_list('*.*', path):
            if sys.version_info[0] == 2:
                self.compare_files(file)
            else:
                with self.subTest(file.replace(EXPECT_DIR, '')):
                    self.compare_files(file)


if __name__ == '__main__':
    unittest.main()
