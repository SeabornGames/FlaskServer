""" This is to start the flask server when debugging """
import os
import sys
from seaborn_logger.logger import log, setup_stdout_logging

# This is needed so endpoints can all import the same global_import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

stage = "importing global_import"

try:
    from settings.global_import import setup_flask
    stage = "importing endpoints"
    import endpoints
    stage = "setup flask"
    run = setup_flask.setup_run(endpoints)
except Exception as ex:
    log.exception(ex)
    sys.exit(1)

if __name__ == '__main__':
    log.debug("Starting Flask Service from Run")
    run()
