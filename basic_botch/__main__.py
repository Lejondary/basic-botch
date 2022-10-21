import discord
from discord.ext import commands

import asyncio
import os
import constants

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=constants.PREFIX, description="I'm a basic botch.", intents=intents)

def main():
    bot.run(constants.TOKEN)

if __name__ == '__main__':
    main()

