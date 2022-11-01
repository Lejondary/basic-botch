import discord
from discord.ext import commands

import sys
import os
#import asyncio # For use AFTER bot login
import constant

intents = discord.Intents.default()
intents.message_content = True # Allows bot to check message content
intents.members = True # Allows bot to track member/user updates

class BasicBotch(commands.Bot):

    # Setups the bot before websocket login 
    async def setup_hook(self):

        # Prints bot username when successfully connected on Discord
        print(f'Logged in as {self.user} on Discord!\n', flush = True)

        # Prints its creator's owner id
        print(f'Herro, I was created by {self.owner_id}\n')

        # Load extensions in Cogs folder
        print(f'Loading Cogs...\n')
        #await self.load_extension('cogs.test')
        await self.load_extension('cogs.events')
        print(f'Finished Loading Cogs!\n')

botch = BasicBotch(command_prefix=constant.PREFIX, description="I'm a basic botch.", intents=intents)
botch.run(constant.TOKEN)
# Notifies when bot has logged off and disconnected from Discord 
print(f'Logged out of {botch.user} on Discord!\n')

# Asynchronous setup AFTER bot login
#async def main():
#    print(f'Starting!')
#    # Start Bot
#    async with client:
#        await client.start(constant.TOKEN)
#    
#asyncio.run(main())
