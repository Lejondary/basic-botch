import discord
from discord.ext import commands

# Test Cog 
class Test(commands.Cog, description='Test category description.'):
    def _init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'*****************\nTest Cog Event!\n*****************', flush = True)

    # Commands
    @commands.command(brief='TestCog command brief description.', description='TestCog command full description.')
    async def TestCog(self, ctx):
        await ctx.send('TestCog Commanded!')
        await ctx.send('TEST YEEEE!')

async def setup(bot):
    await bot.add_cog(Test(bot))

async def teardown(bot):
    await bot.remove_cog(Test(bot))
    print(f'~~~~~~~~~~~~~~~~~\nTest Cog Unloaded!\n~~~~~~~~~~~~~~~~~\n')
