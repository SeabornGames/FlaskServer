""" This will accept command prompt commands to do events like
    init db, drop db, create_endpoints.
    It will run the service but isn't the only way to run the service
"""
import sys

from seaborn.flask_server.setup.manager import setup_manager
from settings.global_import import setup_flask


def main():
    if 'runserver' in sys.argv and not '--port' in sys.argv:
        sys.argv += ['--port', str(setup_flask.configuration.SERVER_PORT)]
    if len(sys.argv) < 2:
        sys.argv.append('bindings')
    #import endpoints

    setup_flask.setup_endpoints(endpoints)
    manager = setup_manager(setup_flask)
    manager.run()
    print("That's All Folks")


if __name__ == '__main__':
    main()
