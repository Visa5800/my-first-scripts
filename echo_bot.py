import telebot

BOT_TOKEN = '8206544952:AAHiG5qZPFBq5l5s3r9oitwgI9OI2w9yNPY'#нужный токен бота
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

if __name__ == '__main__':
    bot.infinity_polling()