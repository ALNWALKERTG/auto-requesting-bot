import re
import os
from os import environ
from pyrogram import enums

import asyncio
import json
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

# basic information
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
PORT = os.environ.get("PORT", "8080")
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

# for force subscribe[Your Force Sub Channel Username Without @ (eg:- sd_bots)]
F_SUB = os.environ.get("FORCE_SUB", "") 

# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "movierockersmr")     
DATABASE_URI  = os.environ.get("DB_URL", "mongodb+srv://movierockersmr:hida@cluster0.kguc0y4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")
