import discord
from discord.ext import commands

import sys
import os
#import asyncio # For use AFTER bot login
import constant # Imports constant.py with all .env file variables

intents = discord.Intents.default()
intents.message_content = True # Allows bot to check message content
intents.members = True # Allows bot to track member/user updates

class BasicBotch(commands.Bot):

    # Setups the bot before websocket login 
    async def setup_hook(self):

        # Prints bot username when successfully connected on Discord
        print(f'-----------------\nLogged in as {self.user} on Discord!\n-----------------', flush = True)

        # Fetches and prints owner username from imported ID with API call 
        owner = await self.fetch_user(self.owner_id) # Retrieves discord username from owner ID
        print(f'-----------------\nHerro, I was created by {owner}!\n-----------------\n')

        # Loops through Cogs folder to Load all extensions ending in .py 
        #print(f'-----------------\nLoading Cogs...\n-----------------\n')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
        #print(f'-----------------\nFinished Loading Cogs!\n-----------------\n')
    
# Instantiates bot and defines command prefix, description, required intents, owner ID, and command case sentitivity
botch = BasicBotch(command_prefix=constant.PREFIX, description="I'm a basic botch.", intents=intents, owner_id = constant.OWNER, case_insensitive=True)

# Runs the bot after setup completion
botch.run(constant.TOKEN, reconnect = True)

# Notifies when bot has stopped running, logged off, and disconnected from Discord 
print(f'-----------------\nLogged out of {botch.user} on Discord!\n-----------------\n')

# Asynchronous setup AFTER bot login
#async def main():
#    print(f'Starting!')
#    # Start Bot
#    async with client:
#        await client.start(constant.TOKEN)
#    
#asyncio.run(main())
