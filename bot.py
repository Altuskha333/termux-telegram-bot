from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from opengpt import OpenGPT

# Создаем экземпляр OpenGPT
forefront = OpenGPT(provider="forefront", type="completion", options={...})

# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который может помочь вам с ответами на ваши вопросы.")

# Функция-обработчик текстовых сообщений
def echo(update, context):
    # Получаем текст сообщения от пользователя
    user_input = update.message.text

    # Генерируем ответ с помощью OpenGPT
    response = forefront.generate(user_input)

    # Отправляем ответ пользователю
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Создаем экземпляр Updater и добавляем обработчики команд и сообщений
updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запускаем бота
updater.start_polling()
updater.idle()
