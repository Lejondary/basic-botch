import discord
from discord.ext import commands

import asyncio
import os
import constant

#intents.message_content = True

#bot = discord.Client()(command_prefix=constant.PREFIX, description="I'm a basic botch.", intents=intents)

client = discord.Client(intents=discord.Intents.default())

#class MyClient(client):
#    async def setup_hook(self):
#        print('Setting Up!')

async def main():
    print('Starting!')
    # Start Bot
    async with client:
        await client.start(constant.TOKEN)
    
asyncio.run(main())

#Old Way
##@bot.event
##async def on_ready():
##    print(f'Logged in as {bot.user}')
#
#@bot.command()
#async def load(ctx, extension):
#    await bot.load_extension(f'basic_botch.test')
#    #print('test loaded')
#
##async def main():
##    async with bot:
##        await bot.start(constant.TOKEN)
##
##asyncio.run(main())
#
##def main():
#    #@some event
#    #call events.py
#
#    #@etc
#    #call etc.py
#
#    #bot.run(constants.TOKEN)
#
##script vs. imported as module
##will run vs. only def runs
##if __name__ == '__main__':
#    #main()
#
##await asyncio.run(bot.run(constant.TOKEN))
#bot.run(constant.TOKEN)
#    #if no token error
#        #print error msg
#
