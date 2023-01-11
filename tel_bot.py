from telegram.ext import *
import khayyam

API_KEY = "5709135989:AAEltBKQTIcdrvMKQ6zmDLGD7RwF9XI8N-c"

print('Bot started!')


def start_command(update, context):
    return update.message.reply_text('سلام، مهدی هستم!')


def help_command(update, context):
    return update.message.reply_text(
        "شما می توانید با استفاده از کلمات 'زمان'،'ساعت'، 'تاریخ' زمان دقیق امروز را دریافت کنید! ")


def message(update, context):
    txt = str(update.message.text).lower()

    if txt in ('زمان', 'ساعت', 'تاریخ'):
        result = khayyam.JalaliDatetime.today().strftime('%A %d %B 5Y')
    else:
        result = "شما می توانید با استفاده از کلمات 'زمان'،'ساعت'، 'تاریخ' زمان دقیق امروز را دریافت کنید! "

    update.message.reply_text(result)


updater = Updater(API_KEY, update_queue=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start_command))
dp.add_handler(CommandHandler('help', help_command))
dp.add_handler(MessageHandler(filters.Text, message))

updater.start_polling(5)
updater.idle()
