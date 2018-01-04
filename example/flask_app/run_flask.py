""" This is to start the flask server when debugging """
import logging
import os
import sys
import traceback

# This is needed so endpoints can all import the same global_import
root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(root_path))
log = logging.getLogger(__name__)

stage = "importing global_import"
try:
    #from seaborn.flask_server.setup import setup_flask
    from settings.global_import import setup_flask
    stage = "importing endpoints"       #TODO resolve relative import issues 'example_flask_app'
    if __name__ == '__main__':
        import endpoints
    else:
        import flask_app.endpoints as endpoints
    #from endpoints import __init__ as endpoints
    stage = "setup flask"
    run = setup_flask.setup_run(endpoints)
except Exception as ex:
    msg = "Exception in %s with %s\n\n%s" % (
        stage, ex, traceback.format_exc())
    log.critical(msg)
    print(msg)
    sys.exit()

if __name__ == '__main__':
    #1log.debug("Starting Flask Service from Run")
    run()
