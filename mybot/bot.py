import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, filters, MessageHandler, CommandHandler
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('Вызван /start')
    await update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def main():
    application = ApplicationBuilder().token(settings.API_KEY).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    logging.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()