import requests

TELEGRAM_TOKEN = "6635696011:AAGkRV93FJxkI9k_B_XEvckmYsB_ud2riMA"
TELEGRAM_CHAT_ID = "6184606004"


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
