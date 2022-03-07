import discord
from discord.ext import commands
from discord import Color
import icons 

class PlayerCommands(commands.Cog):
  """Player specific commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.command('createchar')
  async def createchar(self, ctx: commands.Context, *, text: str):
    """create character"""
    embed = discord.Embed(title=text, description='Choose your class!', color=Color.green())
    embed.add_field(name=icons.WARRIOR + ' Warrior', value='Party Buff: dmg reduction', inline=False)
    embed.add_field(name=icons.MAGE + ' Mage', value='Party Buff: amplify consumables', inline=False)
    embed.add_field(name=icons.ROGUE + ' Rogue', value='Party Buff: dmg buff', inline=False)
    embed.add_field(name=icons.RANGER + ' Ranger', value='Party Buff: reduce stamina consumption', inline=False)
    message = await ctx.send(embed=embed)

    await message.add_reaction(icons.WARRIOR)
    await message.add_reaction(icons.MAGE)
    await message.add_reaction(icons.ROGUE)
    await message.add_reaction(icons.RANGER)

    # wait for reaction
    # react with X to confirm
    # insert to db

def setup(bot: commands.Bot):
  bot.add_cog(PlayerCommands(bot))

