from telegram.ext import CommandHandler

async def start(update, context):
    await update.message.reply_text("ربات نسخه حرفه‌ای فعال است.")

start_handler = CommandHandler("start", start)
