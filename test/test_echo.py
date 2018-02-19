import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from test.test_base import BaseTest


class EchoTest(BaseTest):
    def test_echo(self):
        ret = self.conn.echo.get()
        self.assertEquals("Hello Cruel World!", ret)

    def test_database_write(self):
        ret = self.conn.echo.key.post('test', 'passed')
        self.assertEquals({"echo_key": "test", "echo_value": "passed"}, ret)
        ret = self.conn.echo.key.get('test')
        self.assertEquals({"echo_key": "test", "echo_value": "passed"}, ret)
