from setuptools import setup, find_packages
import os
import sys

VER = sys.version_info[:2]
ENV_MOD = 'lib/python%d.%d/site-packages' % VER
DATA_DIR = '/seaborn/flask_server/blueprint/unity_bindings/cs_templates/'
RELATIVE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FILES = os.listdir(RELATIVE_PATH+DATA_DIR)

setup(
    name='seaborn-flask-server',
    version='0.0.1',
    description='Seaborn helper wrapper around Flask',
    long_description='This is a wrapper around the standard flask app with '
                     'conventions, helpers, middleware, setup, '
                     'autogeneration of client bindings',
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/FlaskServer',
    packages=['seaborn']+['seaborn.' + i
                          for i in find_packages(where = './seaborn')],
    data_files=[(ENV_MOD + DATA_DIR,[DATA_DIR + file for file in DATA_FILES])],
    # todo Mike look for a better solution here
    install_requires=[
        "pip>=9.0.1",
        "Flask>=0.11.1",
        "Flask-DebugToolbar==0.10.0",
        "Flask-Login>=0.3.2",
        "Flask-Migrate>=2.0.0",
        "Flask-Script==2.0.5",
        "Flask-SQLAlchemy>=2.1",
        "Flask-Testing>=0.6.1",
        "Flask-WTF>=0.13.1",
        "gevent>=1.1.2",
        "greenlet>=0.4.10",
        "markupSafe==0.23",
        "requests>=2.11.1",
        "simplejson>=3.8.2",
        "six>=1.10.0",
        "SQLAlchemy>=1.1.1",
        "test-chain>=0.0.1",
        "Werkzeug>=0.11.11",
        "WTForms>=2.1",
        "psycopg2>=2.7.1",
        'seaborn-meta',
        'seaborn-logger',
        'seaborn-timestamp',
    ],
    extras_require={'test': ['test-chain',
                             'seaborn-request-client'],
                    },
    license='MIT License',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
