# Imports
import requests
from flask import Flask, request
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Print the value of webhookURL
webhookURL = os.getenv("SLACK_WEBHOOK_URL")
print("Webhook URL:", webhookURL)

# Endpoint to receive payload and send it to Slack
@app.route('/slack', methods=['POST'])
def receive_and_forward_payload():
    payload = request.json
    
    if payload:
        response = send_slack_message(payload)
        print("Response from Slack:", response)
        return 'Message sent to Slack successfully', 200
    else:
        return 'No payload received', 400

# Function to send Slack message
def send_slack_message(payload):
    if webhookURL:
        headers = {'Content-type': 'application/json'}
        r = requests.post(webhookURL, json=payload, headers=headers)
        return r.status_code
    else:
        return 'Webhook URL is not provided'

if __name__ == '__main__':
    # Run Flask app in debug mode
    app.run(debug=True)


"""
Test:
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, World!"}' http://localhost:5000/slack
"""