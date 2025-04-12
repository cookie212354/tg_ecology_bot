from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
#pip install lxml
urls = ["https://www.vesti.ru/obshchestvo/ekologiya", "https://ria.ru/eco/","https://ecosphere.press/news/"]
url = "https://ria.ru/eco/"

TOKEN = ""  # <-- вставь сюда токен

# Советы по экологии
ECO_TIPS = [
    "🚴‍♂️ Используй велосипед вместо машины, когда это возможно.",
    "💡 Выключай свет, выходя из комнаты.",
    "🛍 Используй многоразовые сумки для покупок.",
    "🌿 Покупай локальные продукты, чтобы сократить углеродный след.",
    "🔋Экономьте воду, топливо.",
    "♻Сортируйте мусор.",
    "💰Отдавайте ненужные вещи",
]

# Экологические задания
ECO_TASKS = [
    "Не использовать пластиковые пакеты целый день",
    "Собрать батарейки и отнести в переработку",
    "Не использовать одноразовую посуду сегодня",
    "Посадить растение или полить домашние цветы",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 🌱! Я экобот. Вот что я умею:\n"
        "/news – Экологические новости\n"
        "/tip – Совет по экологии\n"
        "/task – Экозадание на сегодня\n"
        "/recycle – Найду пункты переработки в городе"
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(ECO_TIPS))

async def eco_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Твое экозадание:\n" + random.choice(ECO_TASKS))

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = random.choice(urls)
    try:
        response = requests.get(url)
        print(response)
        bs = BeautifulSoup(response.text,"lxml")
        if url == "https://ria.ru/eco/":
            temp = bs.find(class_='list-item__title color-font-hover-only')
            Messagetext = temp.get_text()
            print(Messagetext)
        elif url == "https://www.vesti.ru/obshchestvo/ekologiya":
            temp = bs.find(class_='list__title')
            Messagetext = temp.get_text()
            for test in temp:
                Linkt = test
        elif url == "https://ecosphere.press/news/":
            temp = bs.find(class_='elementor-heading-title elementor-size-default')
            Messagetext = temp.get_text()
            for test in temp:
                Linkt = test
    except:
        Link = "404"
        Messagetext = "Не удалось найти последние новости с выбранного сайта"

    await update.message.reply_text(Messagetext + "\n...\n Источник: " +url )

async def recycle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"♻️ Пункты переработки: попробуй на карте https://recyclemap.ru")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("tip", tip))
    app.add_handler(CommandHandler("task", eco_task))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("recycle", recycle))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
