from flask import Flask, request, jsonify
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

# Initialize Flask App
app = Flask(__name__)

# Replace with your Application Insights Instrumentation Key
INSTRUMENTATION_KEY = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY")

# Configure Logging with Application Insights
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = AzureLogHandler(connection_string=f"InstrumentationKey={INSTRUMENTATION_KEY}")
logger.addHandler(handler)

@app.route('/')
def home():
    logger.info("Home route was accessed")  # Log to App Insights
    return "Hello, Flask App with Application Insights!"

@app.route('/event', methods=['POST'])
def log_event():
    data = request.json
    logger.info(f"Received event: {data}")
    return jsonify({"message": "Event logged to Application Insights"}), 200

@app.route('/error')
def trigger_error():
    try:
        raise Exception("This is a test exception for Application Insights")
    except Exception as e:
        logger.exception("Exception occurred!")  # Log exception to App Insights
        return jsonify({"error": "An error occurred!"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
