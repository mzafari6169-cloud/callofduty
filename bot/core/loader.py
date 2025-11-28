from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMINS").split(",")))
PAYMENT_INFO = os.getenv("PAYMENT_CARD")
