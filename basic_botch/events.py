#import asyncio
import constant
from discord.ext import commands


# Handles Messages and Responses

class Yee(commands.Cog):
    def __init__(self, bot):
         self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.send(f"I'm ready for some YEEs")

        #if message.content.startwith(constant.PREFIX):
        #    await message.channel.send('YEEE!')

    @commands.command()
    async def yee(self):
        await self.bot.send(f'Yee!')

#class Glossary(commands.Cog):
#    def __init__(self, bot):
#        self.bot = bot
#        
#    @commands.command(name='glossary')
#    #if message.content.startwith(constant.PREFIX):
#        cog = bot.get_cog('Yee')
#        commands = cog.get_commands()
#        print([c.name for c in commands])

async def setup(bot):
    await bot.add_cog(Yee(bot))
#    bot.add_cog(Glossary(bot))

#@client.event
#async def on_ready():
#    print(f'We have logged in as {client.user}')
