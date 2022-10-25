import discord
from discord.ext import commands

import sys
import os
#import asyncio # For use AFTER bot login
import constant

intents = discord.Intents.default()
intents.message_content = True

class BasicBotch(commands.Bot):

    # Setups the bot before websocket login 
    async def setup_hook(self):
        print(f'Logged in as {self.user} on Discord.', flush = True)

        # Load extensions in Cogs folder
        await self.load_extension('cogs.test')

botch = BasicBotch(command_prefix=constant.PREFIX, description="I'm a basic botch.", intents=intents)
botch.run(constant.TOKEN)

# Asynchronous setup AFTER bot login
#async def main():
#    print(f'Starting!')
#    # Start Bot
#    async with client:
#        await client.start(constant.TOKEN)
#    
#asyncio.run(main())
