from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Sum_polynom import get_sum_pol
from Sum_polynom import fold_pols
from Sum_polynom import convert_pol


async def sum_pol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    pol1 = input_num[1]
    print(pol1)
    pol2 = input_num[2]
    print(pol2)
    pol_1 = convert_pol(pol1)
    print(pol_1)
    pol_2 = convert_pol(pol2)
    pol = fold_pols(pol_1, pol_2)

    await update.message.reply_text(f'ответ: {get_sum_pol(pol)} ')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} ')
    await update.message.reply_text(f'Введите полинромы через пробел после команды /sum 9*x^5+7*x^4+7*x^3+9*x^2+6*x+17=0 3*x^2+2*x+1=0')




bot_token = "ваш token"
app = ApplicationBuilder().token(bot_token).build()
app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("sum", sum_pol))

app.run_polling()