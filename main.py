# Imports
import requests
import json
from flask import Flask, request
from dotenv import load_dotenv, dotenv_values
import os

# Initialize Flask app
app = Flask(__name__)

# Global variable to store incoming Slack message
slackMessage = None

# WebhookURL secret
load_dotenv()
webhookURL = (os.getenv("SECRET"))

# Endpoint to receive Slack messages
@app.route('/slack', methods=['POST'])
def receive_slack_message():
    global slackMessage
    slackMessage = request.json
    return 'Received Slack message successfully', 200

# Function to send Slack message
def send_slack_message(message):
    if webhookURL:
        r = requests.post(webhookURL, json=message)
        return r.status_code
    else:
        return 'Webhook URL is not provided'

# Example usage: Sending the stored Slack message
def send_stored_message():
    global slackMessage
    if slackMessage:
        response = send_slack_message(slackMessage)
        print(response)
    else:
        print("No Slack message received yet")

'''
if __name__ == '__main__':
    # Run Flask app in debug mode
    app.run(debug=True)
'''

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)