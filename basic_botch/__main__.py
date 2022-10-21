import discord
from discord.ext import commands

import asyncio
import os
import constants

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    client.run(constants.TOKEN)

if __name__ == '__main__':
    main()

