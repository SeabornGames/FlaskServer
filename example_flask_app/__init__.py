""" This is the start routine for Apache """

if __name__ == '__main__':
    from .run_flask import run, log
    log.debug("Starting Flask Service from Apache")
    run()
