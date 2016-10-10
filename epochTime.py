from flask import Flask
import time
import os
app = Flask(__name__)

@app.route("/")
def getTime():
    # Reference: https://wiki.python.org/moin/WorkingWithTime
    return str(int(time.time()))

if __name__ == "__main__":
# http://stackoverflow.com/questions/17260338/deploying-flask-with-heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
