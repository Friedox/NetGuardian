# bot/handlers.py

import asyncio

from telegram import Update
from telegram.ext import CallbackContext
from scans.scan import perform_scan  # Import the scan function
from scans.nmap import perform_scan as nmap_perform_scan
from scans.paramiko import perform_scan as paramiko_perform_scan
from scans.scapy import perform_scan as scapy_perform_scan
from scans.socket import perform_scan as socket_perform_scan
from scans.urllib import perform_scan as urllib_perform_scan


# Command handler functions
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to the Security Scan Bot! Use /help to see available commands.")


async def scan(update: Update, context: CallbackContext):
    await update.message.reply_text("Initiating security scan...")

    # Perform the scans
    result1 = await perform_scan()  # This is from the initial import
    print(result1)
    result2 = await nmap_perform_scan()  # This is from the Nmap module
    print(result2)
    # result3 = await paramiko_perform_scan()  # This is from the Paramiko module
    # print(result3)
    result4 = await scapy_perform_scan()  # This is from the Scapy module
    print(result4)
    result5 = await socket_perform_scan()  # This is from the Socket module
    print(result5)
    result6 = await urllib_perform_scan()  # This is from the Urllib module
    print(result6)

    # Construct and send scan results back to user
    scan_results_text = (
        f"Initial Scan: {result1}\n"
        f"Nmap Scan: {result2}\n"
        f"Paramiko Scan: {result3}\n"
        f"Scapy Scan: {result4}\n"
        f"Socket Scan: {result5}\n"
        f"Urllib Scan: {result6}\n"
    )
    await update.message.reply_text(scan_results_text)


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
