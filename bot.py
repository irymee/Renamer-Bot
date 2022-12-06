from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5054196357:AAEemWiF-_D2YYWtpuxb18fdUGcY5dhsrW0")

API_ID = int(os.environ.get("API_ID", "11948995"))

API_HASH = os.environ.get("API_HASH", "cdae9279d0105638165415bf2769730d")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
