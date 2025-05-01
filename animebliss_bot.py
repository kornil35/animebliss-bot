
import requests
import time
from threading import Thread
from flask import Flask

TOKEN = "7761435776:AAFUZjqj9BUxfMWI12Re6H3Tvx3Qb66FblE"
CHANNEL = "@animeblisshub"
API_URL = "https://api.telegram.org/bot" + TOKEN
WAIFU_API = "https://waifu.pics/api/sfw/waifu"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!", 200

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def get_waifu_image():
    res = requests.get(WAIFU_API)
    if res.status_code == 200:
        return res.json().get("url")
    return None

def send_photo_to_channel(photo_url):
    data = {
        "chat_id": CHANNEL,
        "photo": photo_url,
        "caption": "Today’s featured anime girl ✨\nFollow @animeblisshub for more~"
    }
    requests.post(API_URL + "/sendPhoto", data=data)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    while True:
        img_url = get_waifu_image()
        if img_url:
            send_photo_to_channel(img_url)
            print("Sent:", img_url)
        else:
            print("Failed to get image.")
        time.sleep(10800)  # 3 hours
