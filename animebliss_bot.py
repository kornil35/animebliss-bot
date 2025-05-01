
import requests
import time
import random
from threading import Thread
from flask import Flask

# === CONFIG ===
TOKEN = "7761435776:AAFUZjqj9BUxfMWI12Re6H3Tvx3Qb66FblE"
CHANNEL = "@animeblisshub"
API_URL = "https://api.telegram.org/bot" + TOKEN
WAIFU_API = "https://waifu.pics/api/sfw/waifu"
POST_INTERVAL_SECONDS = 60  # 2 hours

# === Flask Setup ===
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!", 200

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# === Captions and Hashtags ===
CAPTIONS = [
    "She’s kinda cute, not gonna lie 😳",
    "Saw her and thought of you 💙",
    "Be honest… you’d totally simp 😌",
    "Another day, another waifu 😎",
    "If this showed up in your feed, it’s fate ✨",
    "Looks like someone’s new favorite 👀",
    "You weren't ready for this level of adorable 🫣",
    "Don’t even pretend she’s not top tier 💅",
    "Your phone needed some beauty today 📱",
    "Okay but why does she kinda go hard 🔥",
    "Daily reminder that 2D > 3D 💯",
    "Caught you looking 😏",
    "Just a little gift for your timeline 🎁",
    "Too wholesome for this world 🌍",
    "Sometimes you just need to stop and stare 🫶",
    "Tell me she’s not elite. I dare you 😤",
    "You’re welcome, btw 😌",
    "Bet this is your new wallpaper 💻",
    "She’s giving 'main character energy' 🔮"
]

HASHTAGS = "#anime #waifu #cutegirl #2dgirls #aesthetic #animebliss #manga #animeart #dailywaifu"

# === Core Functions ===
def get_waifu_image():
    try:
        res = requests.get(WAIFU_API)
        if res.status_code == 200:
            return res.json().get("url")
    except Exception as e:
        print("Error fetching image:", e)
    return None

def send_photo(photo_url, caption):
    data = {
        "chat_id": CHANNEL,
        "photo": photo_url,
        "caption": caption
    }
    try:
        res = requests.post(API_URL + "/sendPhoto", data=data)
        print("POST status:", res.status_code)
    except Exception as e:
        print("Error sending photo:", e)

# === Launch ===
if __name__ == "__main__":
    Thread(target=run_flask).start()
    while True:
        img_url = get_waifu_image()
        base_caption = random.choice(CAPTIONS)
        full_caption = f"{base_caption}\n\nFollow @animeblisshub\n{HASHTAGS}"
        if img_url:
            print("Sending:", img_url)
            send_photo(img_url, full_caption)
        else:
            print("No image retrieved.")
        time.sleep(POST_INTERVAL_SECONDS)
