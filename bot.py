from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5869824244:AAHScxoK4VeMxfa9IKnhobO9OKuQEPFUu9g")

API_ID = int(os.environ.get("API_ID", "20997778"))

API_HASH = os.environ.get("API_HASH", "55080b3d001b4027e7bcb9ca8d112ca5")

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
