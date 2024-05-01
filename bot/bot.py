# bot/bot.py


from telegram.ext import Application, CommandHandler
from handlers import start, scan, schedule, notifications, help_command

from config.config import BOT_TOKEN


def main():
    # Build the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("scan", scan))
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("notifications", notifications))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot with polling
    application.run_polling(1.0)


if __name__ == '__main__':
    main()
