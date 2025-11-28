from telegram.ext import CommandHandler
async def admin(update, context):
    await update.message.reply_text("پنل ادمین نسخه حرفه‌ای آماده است.")

admin_handler = CommandHandler("admin", admin)
