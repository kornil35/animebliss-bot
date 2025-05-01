
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
    try:
        res = requests.get(WAIFU_API)
        if res.status_code == 200:
            return res.json().get("url")
    except Exception as e:
        print("Error fetching image:", e)
    return None

def send_photo_to_channel(photo_url):
    data = {
        "chat_id": CHANNEL,
        "photo": photo_url,
        "caption": "Today’s featured anime girl ✨\nFollow @animeblisshub for more~"
    }
    try:
        res = requests.post(API_URL + "/sendPhoto", data=data)
        print("POST status:", res.status_code)
    except Exception as e:
        print("Error sending photo:", e)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    while True:
        img_url = get_waifu_image()
        if img_url:
            print("Sending image:", img_url)
            send_photo_to_channel(img_url)
        else:
            print("No image to send.")
        time.sleep(60)  # every 1 minute
