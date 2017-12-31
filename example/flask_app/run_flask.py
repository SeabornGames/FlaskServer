""" This is to start the flask server when debugging """
import os
import sys
import traceback
import logging

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_path))
log = logging.getLogger(__name__)

try:
    from test.flask_app.settings.global_import import setup_flask
except Exception as ex:
    print("Exception in importing global_import with %s\n\n%s" % (ex, traceback.format_exc()))
    sys.exit()

try:
    #from test.flask_app.endpoints import endpoints
    #from seaborn.rest_client.endpoint import endpoints
    import endpoints
except Exception as ex:
    msg = "Exception in importing endpoints with %s\n\n%s" % \
          (ex, traceback.format_exc())
    log.error(msg)
    print(msg)
    sys.exit()

try:
    run = setup_flask.setup_run(endpoints)
except Exception as ex:
    msg = "Exception in setup flask with %s\n\n%s" % (
        ex, traceback.format_exc())
    log.error(msg)
    print(msg)
    sys.exit()

if __name__ == '__main__':
    log.debug("Starting Flask Service from Run")
    run()
