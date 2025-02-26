import os
import time
from applicationinsights.flask.ext import AppInsights
from flask import Flask


# create Flask app
app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY") 
#app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'xx-c1b6-4c52-beb4-bf55db27df07' 

appinsights = AppInsights(app)


# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/fail')
def fail():
    a=1+b
    return 'Hello, World!'


@app.route('/sleep')
def sleep():
    time.sleep(2)
    return 'Hello, World + 2s!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Listen on port 8000