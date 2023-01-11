import telebot
import khayyam
from telebot import types
from telegram._utils import markup

bot = telebot.TeleBot("5831279883:AAHD-k_pRH8RXkeXNx8XeS76B9K2HPiuzvY", parse_mode=None)

print('started!')


@bot.message_handler(commands=['start'])
def send_start(message):
    print(message)
    bot.reply_to(message, 'سلام، من مهدی هستم')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "شما می توانید با استفاده از کلمات 'زمان'،'ساعت'، 'تاریخ' زمان دقیق امروز را دریافت کنید! ")


@bot.message_handler(content_types=['photo', 'sticker'])
def send_content_message(message):
    bot.reply_to(message, 'حتما باید از کلمه مورد نظر استفاده بکنید')


@bot.message_handler(func=lambda message: message.from_user.username == message.chat.id)
def send_to_user_message(message):
    bot.reply_to(message, '')

    for i in


@bot.edited_message_handler(commands=['noise'])
def send_edited_message(message):
    bot.send_message(chat_id=message.chat.id, text='من دیدم که پیامت رو تغییر دادی ناقولا')


def date():
    return khayyam.JalaliDatetime.today().strftime('%A %d %B 5Y')


@bot.message_handler(commands=['date'])
def send_date_message(message):
    bot.send_message(chat_id=message.chat.id, text=date())


@bot.message_handler(commands=['dice'])
def send_game_dice(message):
    bot.send_dice(chat_id=message.chat.id)  # کامنت کردم چون تو نسخه وب بازی تاس نداره


@bot.message_handler(commands=['close'])
def send_game_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id=message.chat.id, text='خدافظ بازیکن', reply_markup=markup)


@bot.message_handler(commands=['game'])
def send_game(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('/dice')
    btn2 = types.KeyboardButton('/help')
    btn3 = types.KeyboardButton('/close')
    btn4 = types.KeyboardButton('/date')

    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id=message.chat.id, text='دوست داری چکار کنی؟', reply_markup=markup)


# @bot.message_handler(func=lambda msg: message_user)
# def message_user(message):
#     bot.reply_to(message, )
#
#     if text in ('زمان', 'ساعت', 'تاریخ'):
#         result = khayyam.JalaliDatetime.today().strftime('%A %d %B 5Y')
#     else:
#         result = "شما می توانید با استفاده از کلمات 'زمان'،'ساعت'، 'تاریخ' زمان دقیق امروز را دریافت کنید! "
#
#     message.text(result)


bot.infinity_polling()
