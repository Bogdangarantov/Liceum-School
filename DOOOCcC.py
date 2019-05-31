from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pymysql
import apiai, json

updater = Updater(token='787296993:AAH3m0mVTrcLzMFu5wjaZrn5-LTTUoxrI7U')  # Токен API к Telegram
dispatcher = updater.dispatcher
cnx = pymysql.connect(user='wkfencjQr7',
                      password='RYEA7WmsRb',
                      host='remotemysql.com',
                      database='wkfencjQr7')
cursor = cnx.cursor()
query = "SELECT code_login FROM student"
cursor.execute(query)
result = cursor.fetchall()
# Запис у список всіх користувачів
final_result = [list(i) for i in result]
final_user = []
for i in range(len(final_result)):
            final_user.append(final_result[i][0])

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Hello, I`m  \n'
                          'Post bot\n'
                          'Drop_of_care Org.\n'
                          'If you dont know how to make\n'
                          ' a post you can use /help')
    bot.send_message(chat_id=update.message.chat_id, text='But if you dont need help,\n'
                                                          'Make your profile more cool,\n'
                                                          'Make a post, dont be like everyone else,\n'
                                                          ' be yourself')
    bot.send_message(chat_id=update.message.chat_id, text='Make a post:')

def textMessage(bot, update):
    login = str(update.message.text)
    res1_new = []
    res1 = login.split("}")
    for val in res1:
        val = val.strip()
        res1_new.append(val)


    if res1_new[0] in final_user:
        cursor = cnx.cursor()
        query = "SELECT email FROM student where code_login ='%s'" % res1_new[0]

        cursor.execute(query)
        result2 = cursor.fetchall()
        s1 = str(result2)
        s2 = s1.replace("'", "")
        s2 = s2.replace("(", "")
        s2 = s2.replace(")", "")
        s2 = s2.replace(",", "")
        email = s2
        cursor = cnx.cursor()
        query = "SELECT name FROM student where code_login ='%s'" % res1_new[0]
        cursor.execute(query)
        result2 = cursor.fetchall()
        s1 = str(result2)
        s3 = s1.replace("'", "")
        s3 = s3.replace("(", "")
        s3 = s3.replace(")", "")
        s3 = s3.replace(",", "")
        name = s3
        title = res1_new[1]
        bot.send_message(chat_id=update.message.chat_id, text=' your post is added to profile ')
        text = res1_new[2]
        tags = res1_new[3]

        cursor = cnx.cursor()
        query = "INSERT INTO post (id, email, name, title, tags, text) VALUES (NULL,'%s','%s','%s','%s','%s')" % (
        email, name, title, tags, text)
        cursor.execute(query)
        bot.send_message(chat_id=update.message.chat_id, text='Dear '+name + ' your post is added to profile\n '
                                                              'Do the same if you want to post smth again😊😊😊 ')


    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text = 'Invalid')

#Обработка команд

def helpCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='So, you need help\n'
                          'in writing message \n'
                          'to make a post\n'
                          'This link will help \n'
                          'you to solve this problem\n'
                          'https://telegra.ph/Example-of-sorrectly-written-message-to-Drop-of-Care-bot-04-08')


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
help_command_handler = CommandHandler('help', helpCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
Write_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(help_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(Write_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
