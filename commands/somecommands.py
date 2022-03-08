import asyncio
import time
import discord
from discord.ext import commands

class SomeCommands(commands.Cog):
  """some simple commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command('ping')
  async def ping(self, ctx: commands.Context):
    """get latency"""
    start = time.time()
    message = await ctx.send('testing png...')
    end = time.time()
    await message.edit(content=f"pong! {round(self.bot.latency * 1000)}ms\napi: {round((end - start) * 1000)}ms")

  @commands.command('setstatus')
  @commands.cooldown(1, 30)
  async def setstatus(self, ctx: commands.Context, *, text: str):
    """set bot status"""
    await self.bot.change_presence(activity=discord.Game(name=text))

  # TODO: EXAMPLE COMMAND SPECIFIC ERROR HANDLING
  @setstatus.error
  async def setstatus_error(self, ctx: commands.Context, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f'`.setstatus` on cooldown: {round(error.retry_after)} seconds', delete_after=5)
      print(error)

def setup(bot: commands.Bot):
  bot.add_cog(SomeCommands(bot))
