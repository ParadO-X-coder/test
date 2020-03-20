import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Ку')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Привет', 'Пока', 'Ку')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1, )


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAIMQl5z0ZfrFuXeUqWxrEctJNZUKj1kAAKoxgACY4tGDCMnj8K31kxfGAQ')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text == 'Ку':
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAIMRF5z0aQlOwG4ZRY8dIqo5TC3_B4RAALGAwACnNbnCpvlWJkwtHPSGAQ')
    else:
        bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
