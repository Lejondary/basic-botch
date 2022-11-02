import discord
import constant
from discord.ext import commands

# Yee Cog with description defined 
class Yee(commands.Cog, description='I YEEE! when you yee.'):
    def __init__(self, bot):
         self.bot = bot
        
    # Notifies when bot is online to yee to specified channel in console and discord
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'*****************\nBasic Bot(ch) Operational to YEEE!\n*****************\n', flush = True)
        channel = self.bot.get_channel(1032366477661188166) # Channel ID input
        await channel.send(f"Basic Bot(ch) Online to YEEE!")

    # Yee command
    # Able to YEEE! in any channel
    @commands.command()
    async def yee(self, ctx): 
        await ctx.send(f'YEEE!')

async def setup(bot):
    await bot.add_cog(Yee(bot))

# Notifies when extension has unloaded
async def teardown(bot):
    await bot.remove_cog(Yee(bot))
    print(f'~~~~~~~~~~~~~~~~~\nYee Cog Unloaded!\n~~~~~~~~~~~~~~~~~\n')
