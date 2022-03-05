import discord
from discord.ext import commands

class PlayerCommands(commands.Cog):
  """Player specific commands"""

  # warrior = '\u2694'
  # mage = '\u1F9D9'
  # rogue = '\u1F5E1'
  # ranger = '\u1F3F9'

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.command('createchar')
  async def createchar(self, ctx: commands.Context):
    """create character"""
    embed = discord.Embed(title='Create Character Menu', description='Choose your class!')
    embed.add_field(name='Warrior', value='Party Buff: dmg reduction', inline=False, icon_url='\u2694')
    # embed.add_field(name='Mage', value='Party Buff: amplify consumables', inline=False, icon_url=self.mage)
    # embed.add_field(name='Rogue', value='Party Buff: dmg buff', inline=False, icon_url=self.rogue)
    # embed.add_field(name='Ranger', value='Party Buff: reduce stamina consumption', inline=False, icon_url=self.ranger)
    message = await ctx.send(embed=embed)

    await message.add_reaction('\u2694')
    await message.add_reaction('\u1F9D9')
    await message.add_reaction('\u1F5E1')
    await message.add_reaction('\u1F3F9')

def setup(bot: commands.Bot):
  bot.add_cog(PlayerCommands(bot))

