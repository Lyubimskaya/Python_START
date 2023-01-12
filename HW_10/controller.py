import view
import model
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def start():
    """Стартовая функция"""

    bot_token = "введите токен"
    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", view.greetings))
    app.add_handler(CommandHandler("show", view.show_book))
    app.add_handler(CommandHandler("add", view.add_contact))

    app.run_polling()