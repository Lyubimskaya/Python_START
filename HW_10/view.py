from logger import log
import model
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time


async def greetings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Вывод приветствия и меню.'''
    show_menu = ('/exit - Выход \n'
                 '/show - Загрузить из файла и вывести на экран \n'
                 '/add - Добавить новую запись\n(Пример: "/add Имя Фамилия номер телефона дата рождения место работы)\n',)

    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    f'Вы находитесь в телефонном справочнике')
    time.sleep(3)
    await update.message.reply_text(show_menu[0])