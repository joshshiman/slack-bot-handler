# This will handle scheduling and sending Slack messages

# Imports
import requests
import json

# WebhookURL secret
webhookURL = input('What is the webhook URL \n >')

# Read JSON message data
with open('slackMessage.json') as f:
   slackMessage = json.load(f)

# curl request function
def curl_request(message, webhook):
    r = requests.post(webhook, json= message)
    r.status_code

# Make a curl request to webhookURL
response = curl_request(slackMessage, webhookURL)

# Make a curl request to webhookURL
print(response)

