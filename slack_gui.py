import tkinter as tk
from tkinter import messagebox
import requests
import json

def send_message():
    payload_str = text_entry.get('1.0', tk.END).strip()  # Get the payload as a string
    if payload_str:  # Check if the payload is not empty
        response = send_slack_message(payload_str)  # Pass the payload string
        messagebox.showinfo("Message Sent", f"Response from Slack server: {response}")
    else:
        messagebox.showerror("Error", "Please enter a message")

def send_slack_message(payload_str):
    try:
        payload = json.loads(payload_str)  # Parse the input string as JSON
        url = 'http://localhost:5000/slack'
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, json=payload, headers=headers)
        return r.text
    except json.JSONDecodeError as e:
        return f'Error: Invalid JSON payload - {e}'

# GUI setup
root = tk.Tk()
root.title("Slack Block Kit Sender")

# Text entry for Slack Block Kit code
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
