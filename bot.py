import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

app = Client(
    "video_downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("👋 Hello! Main aapka Video Downloader Bot hoon.")

@app.on_message(filters.text & ~filters.command("start"))
async def handle_link(client, message):
    url = message.text
    await message.reply_text(f"🔍 Link mil gaya:\n`{url}`")

app.run()
