import os
from dotenv import load_dotenv

load_dotenv('.env')

PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('BOT_TOKEN')
