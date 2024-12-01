import telebot

# Вставьте ваш токен от BotFather
TOKEN = '6810377873:AAGtTn8CUrwtzqAXiMp9Q8uDJrjotOt9G7s'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот. Напиши что-нибудь, и я отвечу!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

# Запуск бота
bot.polling()
