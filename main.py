from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start_handler, message_handler
from config import BOT_TOKEN

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    print("🤖 RoshniBot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
