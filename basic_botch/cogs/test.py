import discord
from discord.ext import commands

class Test(commands.Cog):
    def _init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Test Cog Listening!', flush = True)

    @commands.command()
    async def TestCog(self, ctx):
        await ctx.send('Test Cog Commanded!')
        await ctx.send('TEST YEEEE!')

async def setup(bot):
    await bot.add_cog(Test(bot))
