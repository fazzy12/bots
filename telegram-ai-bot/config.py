# config.py
import os

# Telegram bot token from BotFather
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')

# Hugging Face API token for AI-generated tips
HUGGING_FACE_API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN', 'YOUR_HF_API_TOKEN')
