import telebot
bot = telebot.TeleBot('6808960809:AAGYcovbN7nUXuUGcUSwonMdcuI0TMMGjrI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Бот начал работу', parse_mode='Markdown')

@bot.message_handler(commands=['Hi'])
def main(message):
    bot.send_message(message.chat.id, 'Бот приветствует вас', parse_mode='Markdown')

@bot.message_handler(commands=['Mainframe'])
def main(message):
    bot.send_message(message.chat.id, '[ССЫЛКА] (https://pastebin.com/clone/2sTf3jDA)')


bot.infinity_polling()