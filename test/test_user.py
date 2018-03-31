import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from test.test_base import *


class UserTest(BaseTest):
    def test_user_update_email(self, email=None):
        email = email or 'update@%s' % \
                         '.'.join(self.configuration.domain.split('.')[-2:])
        ben = self.test_user_signup()
        user = ben.user.post(email=email)
        self.assertEqual(email, user['email'], 'Failed to set the email')
        user = ben.user.get()
        self.assertEqual(email, user['email'], 'Failed to get the email')
        ben.user.login.email.post(email, ben._password)

    def test_user_update_username(self, username='Ben'):
        ben = self.test_user_signup(username)
        updated_name = '%s_updated' % username
        user = ben.user.post(username=updated_name)
        self.assertEqual(updated_name, user['username'],
                         'Failed to set the username')
        user = ben.user.get()
        self.assertEqual(updated_name, user['username'],
                         'Failed to get the username')
        ben.user.login.post(updated_name, ben._password)
        user = ben.user.post(username=username)

    def test_user_update_password(self, username='Ali'):
        updated_password = '%s_updated' % self.config['users']['user_pwd']
        conn = self.test_user_signup(username, self.config['users']['user_pwd'])
        user = conn.user.post(password=updated_password)
        conn.user.login.post(user['username'], updated_password)
        user = conn.user.post(password=self.config['users']['user_pwd'])

    def test_user_logout(self):
        conn = Connection('Demo-User', self.config['users']['user_pwd'],
                          base_uri=self.SERVER, timeout=self.TIMEOUT,
                          login_url='user/login')
        user = conn.user.get()
        self.assertEqual(user['user_id'], conn.user_id,
                         'Failed to make sure we started out logged in')

        conn.user.logout.post()

        try:
            user = conn.user.get()  # this is suppose to fail
                                    # because we are logged out
        except Exception as ex:
            return

        raise BaseException("Failed to fail at getting "
                            "user info while logged out")