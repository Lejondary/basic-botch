import discord
from discord.ext import commands
#import asyncio

class Test(commands.Cog):
    def _init__(self, bot):
        self.bot = bot

#    @commands.Cog.listener()
#    async def on_ready(self):
#        print ('I ready')

    @commands.command()
    async def yee(self, ctx):
        await ctx.send('YEEE')

#async def setup(bot):
#    await bot.add_cog(Test(bot))

def setup(bot):
    bot.add_cog(Test(bot))
