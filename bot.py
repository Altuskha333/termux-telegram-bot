импортировать   случайный

 время  импорта

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# функция для обработки команды /start

def start(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте, мне надо выдать права администрации чтобы я могла читать сообщения и анализировать их")

# функция для повторения сообщения

def repeat_message(context):

    messages = context.bot.get_chat(context.job.context).get('messages')

    if messages:

        message = random.choice(messages)

        context.bot.send_message(chat_id=context.job.context, text=message)

# функция для обработки сообщений

def echo(update, context):

    messages = context.bot.get_chat(update.effective_chat.id).get('messages', [])

    messages.append(update.message.text)

    context.bot.set_chat(update.effective_chat.id, {'messages': messages})

# функция для запуска бота

def main():

    # создаем экземпляр Updater и передаем токен бота

    updater = Updater(token='6288706593:AAFz6bQ4ErJiUG_9KuX1pn4QwDhWpc7p84Y', use_context=True)

    # получаем объект диспетчера для регистрации обработчиков

    dispatcher = updater.dispatcher

    # регистрируем обработчики команд

    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)

    # регистрируем обработчики сообщений

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(echo_handler)

    # запускаем повторение сообщений

    job_queue = updater.job_queue

    job_queue.run_repeating(repeat_message, interval=random.randint(60, 1800), context=update.effective_chat.id)

    # запускаем бота

    updater.start_polling()

    # останавливаем бота при нажатии Ctrl+C

    updater.idle()

if __name__ == '__main__':

    main()

    
