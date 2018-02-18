""" This will accept command prompt commands to do events like
    init db, drop db, create_endpoints.
    It will run the service but isn't the only way to run the service
"""
import os
import sys
from seaborn_flask_server.setup.manager import setup_manager
from example_flask_app.settings.global_import import setup_flask


def main():
    root_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(root_path))

    if 'runserver' in sys.argv and '--port' not in sys.argv:
        sys.argv += ['--port', str(setup_flask.configuration.SERVER_PORT)]
    if len(sys.argv) < 2: # this is optional
        sys.argv.append('bindings')
    import example_flask_app.endpoints as endpoints

    setup_flask.setup_endpoints(endpoints)
    manager = setup_manager(setup_flask)
    manager.run()
    print("That's All Folks")


if __name__ == '__main__':
    main()
