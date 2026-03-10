import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def lista_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send the shopping list message."""
    message = """💌 Nu uita, așa cumperi tu cel mai bine! 😘\n🛒 Lista de cumpărături:\n🍅 Roșii\n🥚 Ouă\n🍞 Pâine\nPup! 😘❤️"""
    await update.message.reply_text(message)

def main():
    """Start the bot."""
    # Get token from environment variable
    token = os.getenv('BOT_TOKEN')
    if not token:
        raise ValueError("BOT_TOKEN environment variable is not set")
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Add command handler
    application.add_handler(CommandHandler("lista", lista_command))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
