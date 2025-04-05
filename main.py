#pip install python-telegram-bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Start command: greet user
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Добро пожаловать в Экологического бота! 🌍\nМожете использовать следующие команды:\n/help - Помощь\n/tips - Получить Факт\n')

# Help command: list all available commands
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Доступные Команды:\n/start - Запусить бота\n/help - Помощь\n/tips - Получить Факт\n')

# Tips command: give ecological tips
def tips(update: Update, context: CallbackContext) -> None:
    tips_list = [
        "Сокращайте, повторно используйте и перерабатывайте отходы, чтобы свести их к минимуму",
        "Используйте многоразовые пакеты, бутылки и контейнеры",
        "Экономьте воду, устраняя протечки и используя эффективное оборудование",
        "Посадите дерево или разбейте сад, чтобы улучшить качество воздуха",
        "Информируйте других о проблемах окружающей среды.",
        "Пользуйтесь общественным транспортом, ездите на велосипеде или ходите пешком вместо того, чтобы садиться за руль",
        "Поддерживайте местный и устойчивый бизнес"
    ]
    
    update.message.reply_text(f"🌱 Экологический факт: {tips_list[-1]}")  # Send a random tip

