
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
POST_INTERVAL_SECONDS = 60  # Change to 1800 for 30 min or 3600 for 1 hour

# === Flask Setup for Render pinging ===
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!", 200

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# === More human-like caption pool ===
CAPTIONS = [
    "She’s kinda cute, not gonna lie 😳\nFollow @animeblisshub",
    "Saw her and thought of you 💙\nFollow @animeblisshub",
    "Be honest… you’d totally simp 😌\nFollow @animeblisshub",
    "Another day, another waifu 😎\nFollow @animeblisshub",
    "If this showed up in your feed, it’s fate ✨\nFollow @animeblisshub",
    "Looks like someone’s new favorite 👀\nFollow @animeblisshub",
    "You weren't ready for this level of adorable 🫣\nFollow @animeblisshub",
    "Don’t even pretend she’s not top tier 💅\nFollow @animeblisshub",
    "Your phone needed some beauty today 📱\nFollow @animeblisshub",
    "Okay but why does she kinda go hard 🔥\nFollow @animeblisshub",
    "Daily reminder that 2D > 3D 💯\nFollow @animeblisshub",
    "Caught you looking 😏\nFollow @animeblisshub",
    "She’s not even trying and still perfect 🥲\nFollow @animeblisshub",
    "Just a little gift for your timeline 🎁\nFollow @animeblisshub",
    "Too wholesome for this world 🌍\nFollow @animeblisshub",
    "Tell me she’s not elite. I dare you 😤\nFollow @animeblisshub",
    "Sometimes you just need to stop and stare 🫶\nFollow @animeblisshub",
    "Soft, sweet, and deadly… just your type, right?\nFollow @animeblisshub",
    "You’re welcome, btw 😌\nFollow @animeblisshub",
    "Bet this is your new wallpaper 💻\nFollow @animeblisshub",
    "She’s giving 'main character energy' 🔮\nFollow @animeblisshub",
    "Rate her out of 10. I dare you 💯\nFollow @animeblisshub",
    "When she appears, everything else fades away ✨\nFollow @animeblisshub",
    "If she smiled at you, your whole day would be better 😭\nFollow @animeblisshub",
    "Don’t scroll past. This is peak 🍥\nFollow @animeblisshub"
]

# === Core Functions ===
def get_waifu_image():
    try:
        res = requests.get(WAIFU_API)
        if res.status_code == 200:
            return res.json().get("url")
    except Exception as e:
        print("Error fetching image:", e)
    return None

def send_photo_to_channel(photo_url, caption):
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

# === Run Everything ===
if __name__ == "__main__":
    Thread(target=run_flask).start()
    while True:
        img_url = get_waifu_image()
        caption = random.choice(CAPTIONS)
        if img_url:
            print("Sending:", img_url)
            send_photo_to_channel(img_url, caption)
        else:
            print("No image retrieved.")
        time.sleep(POST_INTERVAL_SECONDS)
