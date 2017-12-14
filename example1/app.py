"""
This example uses regular threads and is adapted from:
https://stackoverflow.com/a/22900255
"""

import time
import datetime
import threading
import atexit
from flask import Flask

POOL_TIME = 2

# variables that are accessible from anywhere
commonDataStruct = {'counter': 0, 'now': datetime.datetime.now().isoformat()}
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
yourThread = threading.Thread()

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return str(threading.get_ident()) + "\n" + str(commonDataStruct)

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
        with dataLock:
            # Do your stuff with commonDataStruct Here
            commonDataStruct['counter'] += 1
            commonDataStruct['now'] = datetime.datetime.now().isoformat()
            # Set the next thread to happen
            yourThread = threading.Timer(POOL_TIME, doStuff, ())
            yourThread.start()   

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, threaded=True, use_reloader=False)
