import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Render ke Environment Variables se token uthayega
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Main aapka Video Downloader Bot hoon. Mujhe link bhejiye.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text(f"🔍 Link mil gaya:\n`{url}`")

if __name__ == '__main__':
    # Bot application build karna
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands aur Messages ke handlers add karna
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot successfully start ho gaya hai...")
    
    # Bot ko run karna
    application.run_polling()
