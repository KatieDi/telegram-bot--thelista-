import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🛒 Lista Cumpărături", "💋 Pupici"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Bună! Ce vrei să faci?",
        reply_markup=reply_markup
    )

async def lista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = (
        "💌 Nu uita, așa cumperi tu cel mai bine! 😘\n\n"
        "🛒 *Lista de cumpărături:*\n\n"
        "🍅 Roșii\n"
        "🥚 Ouă\n"
        "🍞 Pâine\n\n"
        "Pup! 😘❤️"
    )
    await update.message.reply_text(mesaj, parse_mode="Markdown")

async def pupici(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("😘💋❤️ Pupici mulți!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🛒 Lista Cumpărături":
        await lista(update, context)
    elif text == "💋 Pupici":
        await pupici(update, context)

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lista", lista))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Botul rulează!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
