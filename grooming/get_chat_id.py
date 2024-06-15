# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
#
# TELEGRAM_TOKEN = '"6635696011:AAGkRV93FJxkI9k_B_XEvckmYsB_ud2riMA"'
#
#
# def start(update: Update, context: CallbackContext) -> None:
#     chat_id = update.message.chat_id
#     update.message.reply_text(f'Your Chat ID is: {chat_id}')
#
#
# def main() -> None:
#     updater = Updater(TELEGRAM_TOKEN)
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler("start", start))
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()
