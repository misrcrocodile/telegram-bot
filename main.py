import telebot
import os

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()

# import yfinance as yf
# aapl= yf.Ticker("aapl")
# print(aapl)
