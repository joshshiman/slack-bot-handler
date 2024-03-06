# This will handle scheduling and sending Slack messages
import requests
import json

with open('webhookURL.txt') as f:
    webhookURL = f.read()

with open('slackMessage.json') as f:
   slackMessage = json.load(f)

def curl_request(message, url):
    r = requests.post('url', json= message)
    r.status_code

# Make a curl request to webhookURL
response = curl_request('slackMessage','webhookURL')

# Make a curl request to webhookURL
print(response)

