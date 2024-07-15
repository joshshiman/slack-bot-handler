from flask import Flask, request, jsonify
import requests
import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
import logging

app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize IBM Watson ModelInference Client
api_key = os.getenv('IBM_API_KEY')
ibm_url = os.getenv('IBM_URL')
project_id = "0d75047b-d340-4c7c-af1e-78f325ae52a0"

if not api_key or not ibm_url:
    raise ValueError("IBM_API_KEY and IBM_URL must be set in environment variables")

credentials = {
    "apikey": api_key,
    "url": ibm_url
}
model_inference = ModelInference(model_id="ibm/granite-13b-chat-v2", credentials=credentials, project_id=project_id)

@app.route('/slack/command', methods=['POST'])
def handle_slack_command():
    # Extract the command text from the Slack command
    data = request.form
    command_text = data.get('text')
    
    # Prepare the prompt with more context for the command text
    prompt = f"Create a Slack announcement for the IBM Technology Zone channel based on the following details:\n\nAnnouncement Details: {command_text}\n\nThe structure should include a headline, a concise summary, key points, and a call to action."
    
    params = {
        "decoding_method": "greedy",
        "max_new_tokens": 200,
        "min_new_tokens": 50,
        "stop_sequences": [],
        "repetition_penalty": 1
    }
    
    # Make the API call to IBM
    try:
        logging.debug(f"Sending prompt to IBM API: {prompt}")
        response = model_inference.generate(prompt=prompt, params=params)
        logging.debug(f"Response from IBM API: {response}")
        
        # Extract the generated text from the response
        result_text = response['results'][0]['generated_text'] if response['results'] else "No text generated"
        logging.debug(f"Generated text: {result_text}")

        # Send the result as an announcement to a Slack channel
        slack_announcement(result_text)
        return jsonify({'status': 'success', 'data': result_text})
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)})

def slack_announcement(text):
    # Ensure the SLACK_WEBHOOK_URL is set in the environment variables
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    if not slack_webhook_url:
        raise ValueError('Missing SLACK_WEBHOOK_URL')

    slack_data = {
        "text": text
    }

    response = requests.post(slack_webhook_url, json=slack_data)

    if response.status_code != 200:
        raise ValueError(f'Request to Slack returned an error {response.status_code}, the response is: {response.text}')

if __name__ == '__main__':
    app.run(debug=True)
