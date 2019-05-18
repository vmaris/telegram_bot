# Вызываем бота в командной строке!!!

#Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

# bot - объект с помощью которого идет управление ботом 
# update - та информация которую прислал телеграм
def greet_user(bot, update):
    text = 'Вызван /strat'
    print(text)
    update.message.reply_text("Привет доброго времени суток")
    

#Функция, которая соединяется с платформой Telegram, "тело" нашего бота 
def main():
    mybot = Updater("723065458:AAHrWiozuZorwyKx-dTqvVMA5w_sYkfz3Ck",request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()


#вызываем функцию
main()

