import telebot
import os

# توكن البوت (من BotFather)
TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "هلا بيك! ✨ البوت يشتغل تمام 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("البوت يشتغل...")
bot.infinity_polling()
