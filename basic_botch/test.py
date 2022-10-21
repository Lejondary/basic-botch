import discord
from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot # sets the bot variable so we can use it in cogs
        self._last_member = None

#	@commands.Cog.listener()
#	async def on_ready(self):
#		# an example event with cogs
#        # print(f'I ready')
	
	@commands.command()
	async def yee(self, ctx):
		# an example command with cogs
        await ctx.print(f'YEE')
        await ctx.send(f'YEEE')

async def setup(bot):
	await bot.add_cog(Test(bot))
