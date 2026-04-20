import os
import re
import json
import requests


def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def send_slack_message(message: str) -> bool:
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps({'text': message}))
        return response.status_code == 200
    except Exception:
        return False
