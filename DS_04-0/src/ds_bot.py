import telebot
import requests
import my_token

token = my_token.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  # жду пока вверут команду /start
def start_message(message):
    bot.send_message(message.chat.id, "Введите свой вопрос, на который хотите получить ответ да или нет")


@bot.message_handler(content_types=['text'])
def answer(message):
    res = requests.get('https://yesno.wtf/api').json()
    bot.send_video(message.chat.id, res['image'])

if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling()
