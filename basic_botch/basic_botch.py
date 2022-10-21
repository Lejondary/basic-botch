import discord
from discord.ext import commands

import asyncio
import os
import constant

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=constant.PREFIX, description="I'm a basic botch.", intents=intents)

#def main():
    #@some event
    #call events.py

    #@etc
    #call etc.py

    #bot.run(constants.TOKEN)

#script vs. imported as module
#will run vs. only def runs
#if __name__ == '__main__':
    #main()

bot.run(constant.TOKEN)
    #if no token error
        #print error msg

