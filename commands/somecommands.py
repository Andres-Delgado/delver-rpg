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

  @setstatus.error
  async def setstatus_error(self, ctx: commands.Context, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f'`.setstatus` on cooldown: {round(error.retry_after)} seconds', delete_after=5)
      print(error)

  @commands.command('status')
  async def status(self, ctx: commands.Context):
    embed = discord.Embed(title='Current Status', description='Currently out in a dungeon!')
    embed.set_author(name="SoggyFroggy")
    embed.add_field(name="Field 1", value="Not an inline field!", inline=False)
    embed.add_field(name="Field 2", value="An inline field!", inline=True)
    embed.add_field(name="Field 3", value="Look I'm inline with field 2!", inline=True)
    embed.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

    message = await ctx.send(embed=embed)
    await message.add_reaction('\u2705')
    await message.add_reaction('\u274C')

    check = lambda r, u: u == ctx.author and str(r.emoji) in '\u2705\u274C'

    try:
      reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=30)
    except asyncio.TimeoutError:
      await ctx.send('too long to respond')
      return

    if str(reaction.emoji) == '\u2705':
      await ctx.send('ayyee')

def setup(bot: commands.Bot):
  bot.add_cog(SomeCommands(bot))
