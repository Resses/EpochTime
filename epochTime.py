from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def getTime():
    # Reference: https://wiki.python.org/moin/WorkingWithTime
    return str(int(time.time()))

if __name__ == "__main__":
    app.run()
