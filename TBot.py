import Image
import telebot
from telebot import types


def prepare_token(filename):
    file=open(filename, 'r')
    token=file.read()
    file.close()
    return token

ttoken=prepare_token('ttoken.txt')
bot=telebot.TeleBot(ttoken)
    
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.from_user.id, photo=Image.prepare_data_for_send("Cat.jpg"))

try:
    bot.polling(none_stop=True, interval=0)
except KeyboardInterrupt:
    sys.exit()