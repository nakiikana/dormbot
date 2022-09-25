import telebot
from telebot import types
bot = telebot.TeleBot('5449910290:AAH75ykYZEN-S2bVBj-bDbHua3_vONwTEGY')
@bot.message_handler()
def schedule(message):
    if message.text == 'Расписание' or message.text == 'расписание':
        markup = types.ReplyKeyboardMarkup()
        #дополнительные кнопки можно добавлять аналогичным образом (не забудь сделать верстку клавиатуры ниже*)
        une = types.InlineKeyboardButton('Коменданты')
        deux = types.InlineKeyboardButton('Паспортный стол')
        trois = types.InlineKeyboardButton('Соц.отдел')
        quatre = types.InlineKeyboardButton('Второй отдел(военка)')
        markup.row(une, deux)
        markup.row(trois, quatre)
        if message.text == 'Коменданты':
            bot.send_message(message.chat.id, f'ПН-ЧТ: 9.30 - 17.45\nПТ: 9.30 - 16.30\nОбед: 12.30 - 13.30\nНочной комендант работает с 18.00', parse_mode='html')
        if message.text == 'Паспортный стол':
            bot.send_message(message.chat.id, f'ПН-ВТ: 9.30 - 17.00\nСP: 9.30 - 12.30\nЧТ: 9.30 - 17.00\nПТ: 9.30 - 12.30\nОбед: 12.30 - 13.30', parse_mode='html')
        if message.text == 'Соц.отдел':
            bot.send_message(message.chat.id, f'ПН-ЧТ: 10.00 - 17.30\nПТ: 10.00 - 16.30\nОбед: 14.00 - 15.00', parse_mode='html')
bot.polling(non_stop=True)
