""" This defines a Base Test, which will be sub class by the other tests
"""
import os
import sys
import time
import configparser

from seaborn_file.file import find_file
from seaborn_logger.skip_traceback import skip_path as traceback_skip_path
from seaborn_logger.logger import log
from test_chain import TestChain

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from example_flask_app.settings.config import configuration
from example_bindings.connection import Connection

PROXY_DEBUG_SERVER = 'http://127.0.0.1:4777'
PROXY_AWS_SERVER = 'http://127.0.0.1:4888'
DEBUG_SERVER = 'http://127.0.0.1:4999'
AWS_SERVER = 'http://%s' % configuration.domain
AWS_SERVER_SSL = 'https://%s' % configuration.domain


class BaseTest(TestChain):
    thread = None
    SERVER = globals()[os.environ.get('TEST_SERVER', 'DEBUG_SERVER')]
    TIMEOUT = 10
    START_TIME = time.time()
    config = configparser.ConfigParser()
    configuration = configuration
    anonymous = None

    @classmethod
    def setUpClass(cls):
        traceback_skip_path('/bindings/')
        log.debug('Connecting to Server: %s' % cls.SERVER)
        cls.config.read(find_file('_config.ini'))
        admin_password = cls.config['users']['admin_pwd']
        cls.anonymous = Connection("Anonymous", base_uri=cls.SERVER)
        if cls.SERVER is DEBUG_SERVER or cls.SERVER is PROXY_DEBUG_SERVER:
            cls.start_server()
        cls.conn = Connection('Admin-User', admin_password,
                              'user/login', base_uri=cls.SERVER)

    @classmethod
    def start_server(cls):
        try:
            cls.anonymous.echo.get()
            log.info("Server %s is Already Started" % cls.SERVER)
        except Exception as ex:
            if cls.SERVER != DEBUG_SERVER and cls.SERVER != PROXY_DEBUG_SERVER:
                log.error("Exception server is not started", ex)
                raise
            from example_flask_app.run_flask import run
            if sys.version_info[0] == 3:
                import _thread as thread
            else:
                import thread
            thread.start_new_thread(run, ())

    @classmethod
    def tearDownClass(cls):
        log.info("That's All Folks in %s seconds",
                 round(time.time() - cls.START_TIME, 2))

    def test_login(self, name=None, password=None):
        user = Connection(name or self.config['users']['demo'],
                          password or self.config['users']['demo_pwd'],
                          'user/login', base_uri=self.SERVER,
                          timeout=self.TIMEOUT)
        return user

    def test_user_signup(self, username="Ben", password=None,
                         email=None, delete_if_exists=True):
        password = password or self.config['users']['demo_pwd']

        if delete_if_exists:
            try:
                old = self.conn.user.get(username=username)
                self.conn.user.delete(old['user_id'])
            except Exception:
                pass

        user_conn = Connection(username, password,
                               base_uri=self.SERVER, timeout=self.TIMEOUT)
        ret = user_conn.user.signup.put(username=username,
                                        password=password, email=email)

        user_conn.user_id = ret['user_id']
        user_conn._status = "logged in from signup"
        return user_conn
