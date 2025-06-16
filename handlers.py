from telegram import Update
from telegram.ext import CallbackContext
from config import PUBLIC_GROUP_ID

def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Type the name of the file you're looking for.")

def message_handler(update: Update, context: CallbackContext):
    query = update.message.text.lower()
    search_link = f"https://t.me/c/{str(PUBLIC_GROUP_ID)[4:]}/1"  # Dummy message link
    update.message.reply_text(f"Searching for: {query}\nHere’s a sample link: {search_link}")
