import Image
import telegram
from telegram.ext import Updater, CommandHandler


def prepare_token(filename):
    file=open(filename, 'r')
    token=file.read()
    file.close()
    return token

ttoken=prepare_token('ttoken.txt')
bot=Updater(ttoken)
dispatcher=bot.dispatcher

def start(update, context):
    context.bot.send_photo(update.effective_chat.id, photo=Image.prepare_data_for_send("Cat.jpg"))

start_handler=CommandHandler('start', start)
dispatcher.add_handler(start_handler)

bot.start_polling()
bot.idle()