from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # <-- вставь сюда токен

# Советы по экологии
ECO_TIPS = [
    "🚴‍♂️ Используй велосипед вместо машины, когда это возможно.",
    "💡 Выключай свет, выходя из комнаты.",
    "♻️ Сортируй отходы дома.",
    "🛍 Используй многоразовые сумки для покупок.",
    "🌿 Покупай локальные продукты, чтобы сократить углеродный след.",
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
        "/eco_task – Экозадание на сегодня\n"
        "/recycle <город> – Найду пункты переработки в городе"
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(ECO_TIPS))

async def eco_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Твое экозадание:\n" + random.choice(ECO_TASKS))

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌍 Последние эко-новости можно найти тут: https://ecoportal.su/news.php")

async def recycle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = " ".join(context.args) if context.args else None
    if not city:
        await update.message.reply_text("❗Укажи город: /recycle Москва")
        return
    await update.message.reply_text(f"♻️ Пункты переработки в городе {city}: попробуй на карте https://recyclemap.ru")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tip", tip))
    app.add_handler(CommandHandler("eco_task", eco_task))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("recycle", recycle))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
