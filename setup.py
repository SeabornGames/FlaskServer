from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='seaborn-flask-server',
    version='1.0.0',
    description='Seaborn helper wrapper around Flask',
    long_description=long_description,
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/FlaskServer',
    packages=['seaborn_flask_server'],
    package_data={
        'seaborn.flask_server.blueprint.unity_bindings.cs_templates':
              [
                  "api_initialize.cs",
                  "api_monitor.cs",
                  "behaviors.cs",
                  "custom_api.cs",
                  "models.cs",
                  "namespace.cs",
                  "operations.cs",
              ],
        },
    install_requires=[
        "configparser",
        "pip",
        "Flask",
        "Flask-DebugToolbar",
        "Flask-Login",
        "Flask-Migrate",
        "Flask-Script",
        "Flask-SQLAlchemy",
        "Flask-Testing",
        "Flask-WTF",
        "gevent",
        "greenlet",
        "markupSafe",
        "requests",
        "simplejson",
        "six",
        "SQLAlchemy",
        "test-chain",
        "Werkzeug",
        "WTForms",
        "psycopg2",
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
