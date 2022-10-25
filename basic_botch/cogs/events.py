import discord
import constant
from discord.ext import commands

class Yee(commands.Cog):
    def __init__(self, bot):
         self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Basic Bot(ch) Online to YEEE!\n', flush = True)
        channel = self.bot.get_channel(1032366477661188166) # Channel ID input
        await channel.send(f"Basic Bot(ch) online to YEEE!")

        #if message.content.startWith(constant.PREFIX):
        #    await message.channel.send('YEEE!')

    @commands.command()
    async def yee(self, ctx):
        await ctx.send(f'YEEE!')

async def setup(bot):
    await bot.add_cog(Yee(bot))
