from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📚 Програма курсу", callback_data="program")],
        [InlineKeyboardButton("💰 Вартість", callback_data="price")],
        [InlineKeyboardButton("📅 Дати старту", callback_data="dates")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вітаю 💅 Оберіть розділ:", reply_markup=main_menu())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "program":
        text = "Тут буде програма курсу"
    elif query.data == "price":
        text = "Тут буде вартість"
    elif query.data == "dates":
        text = "Тут будуть дати старту"

    await query.edit_message_text(text, reply_markup=main_menu())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
