import os
import asyncio
from telegram import Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

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

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("lista", lista))
    print("Botul rulează!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
