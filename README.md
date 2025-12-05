# Slack Block Kit Payload Scheduler
Intended for scheduling, and delivering formatted Slack Messages

## Getting Started

1. First ensure that you have Python and Git installed

- `sudo install python3`
- `sudo install git-all`

2. Clone the repostiory by running this in the terminal

- `git clone https://github.com/joshshiman/SlackBotHandler.git`

3. Navigate to the project directory

- `cd SlackBotHandler`

4. Next install all dependencies

`sudo pip3 install -r requirements.txt`

5. Create a `.env` file

- `touch .env`

6. Add webhook to your `.env` file

- `echo SLACK_WEBHOOK_URL={your secret here}`

7. Run the server

- `app.py`

## Testing

`curl -X POST http://127.0.0.1:5000/slack/command -d 'token=TEST_TOKEN' -d 'team_id=T0001' -d 'team_domain=example' -d 'channel_id=C2147483705' -d 'channel_name=test' -d 'user_id=U2147483697' -d 'user_name=Steve' -d 'command=/announce' -d 'text=We are introducing new features to improve your experience. Stay tuned for updates!' -d 'response_url=https://hooks.slack.com/commands/1234/5678'`
