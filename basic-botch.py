# Imports
import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv('.env')

# Variables
prefix = os.getenv('PREFIX')
token = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix): 
        await message.channel.send('YEEE!')

client.run(token)
