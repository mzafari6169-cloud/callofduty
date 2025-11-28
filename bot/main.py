from telegram.ext import ApplicationBuilder
from bot.core.loader import BOT_TOKEN
from bot.handlers.start import start_handler
from bot.admin.panel import admin_handler

def run():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(start_handler)
    app.add_handler(admin_handler)
    app.run_polling()

if __name__ == "__main__":
    run()
