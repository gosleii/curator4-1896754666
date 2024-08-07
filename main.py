import telebot

bot = telebot.TeleBot("7267924298:AAGNaQaJpGaobV8-Vi3xdVOJy6DohYwGI8I")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "привет")


@bot.message_handler(commands=["new"])
def new_handler(message):
    bot.send_message(message.chat.id, "*ссылка*", parse_mode="markdown")


@bot.message_handler(commands=["cool"])
def cool_handler(message):
    bot.send_message(message.chat.id, "[золотое яблоко](https://goldapple.ru)", parse_mode="markdown")