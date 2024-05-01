# bot/handlers.py

import asyncio

from telegram import Update
from telegram.ext import CallbackContext
from scans.scan import perform_scan  # Import the scan function


# Command handler functions
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to the Security Scan Bot! Use /help to see available commands.")


async def scan(update: Update, context: CallbackContext):
    await update.message.reply_text("Initiating security scan...")
    # Perform the scan
    scan_result = await perform_scan()

    # Send scan results back to user
    await update.message.reply_text(scan_result)


async def schedule(update: Update, context: CallbackContext):
    await update.message.reply_text("Setting up scheduled scan...")


async def notifications(update: Update, context: CallbackContext):
    await update.message.reply_text("Managing notifications...")


async def help_command(update: Update, context: CallbackContext):
    # Display help information
    help_text = """
    Available commands:
    /start - Start interacting with the bot.
    /scan - Initiate a network security scan.
    /schedule - Set up a scheduled scan.
    /notifications - Manage notification preferences.
    /help - Display help information.
    """
    await update.message.reply_text(help_text)
