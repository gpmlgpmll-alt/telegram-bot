import telebot

# توكن البوت من BotFather
TOKEN = "6991340590:AAHExa9Idc3OB-IeuQy_7dU-3DJ1KymMH_c"

bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "هلا بيك! ✨ البوت يشتغل تمام 🚀")

# يكرر أي رسالة يكتبها المستخدم
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("..البوت يشتغل")
bot.infinity_polling()
