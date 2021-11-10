"""
10/11/2021
КИРИЛЛ-LOTIN TELEGRAM BOT
Muallif: Ramazon Xolmo'minov
"""
import telebot
from transliterate import to_cyrillic, to_latin
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "2136185128:AAGCmh6k65joNd7lx4SJRSiryaEAmb7TenA"  # <-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)


# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Bu usul bilan foydalanuvchi nomini olishimiz mumkin 1
    name = str(message.from_user.full_name)
    bot.send_message(message.from_user.id, 'Assalom aleykum ' + name + '\tLotin-Kirill-Lotin botiga xush kelibsiz!')

    # username = (
    #     message.from_user.username
    # )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin 2
    # xabar = f"Assalom aleykum, {username} Lotin-Kirill-Lotin botiga xush kelibsiz!"
    # xabar += "\n\nMatningizni yuboring:"
    # bot.reply_to(message, xabar)

    # matnlar uchun mas'ul funksiya


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()

if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)
