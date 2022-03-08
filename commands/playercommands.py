import asyncio
import discord
import icons

from discord import Color
from discord.ext import commands

class PlayerUtils():

  def __init__(self, bot: commands.Bot, ctx: commands.Context):
    self.bot = bot
    self.ctx = ctx

  def check(self, ctx: commands.Context):
    return lambda r, u: u == ctx.author and str(r.emoji) \
      in icons.WARRIOR + icons.MAGE + icons.ROGUE + icons.RANGER + icons.X

  async def wait_for_reaction(self, message: discord.message, name: str, timeout: int):
    """ get user reaction
        returns None if timeout or invalid reaction"""

    try:
      # wait for reaction
      reaction, user = await self.bot.wait_for('reaction_add', check=self.check(self.ctx), timeout=timeout)

      # this check might be done already by self.check()
      if user.id == self.ctx.author.id:
        return reaction

    # timeout - display error embed
    except asyncio.TimeoutError:
      await message.clear_reactions()
      timeout_embed = discord.Embed(title='%s - %s' % (self.ctx.author.name, name), color=Color.red())
      timeout_embed.add_field(name='Character Creation Timed Out!', value='input `.createchar character_name` to attempt again', inline=False)
      await message.edit(embed=timeout_embed)

    return None

  async def select_character_embed(self, ctx: commands.Context, name: str):
    """embed menu for character selection"""

    # build embed
    embed = discord.Embed(title='%s - %s' % (ctx.author.name, name), description='Choose your class!', color=Color.green())
    embed.add_field(name=icons.WARRIOR + ' Warrior', value='Party Buff: dmg reduction', inline=False)
    embed.add_field(name=icons.MAGE + ' Mage', value='Party Buff: amplify consumables', inline=False)
    embed.add_field(name=icons.ROGUE + ' Rogue', value='Party Buff: dmg buff', inline=False)
    embed.add_field(name=icons.RANGER + ' Ranger', value='Party Buff: reduce stamina consumption', inline=False)

    # add reaction options
    message = await ctx.send(embed=embed)
    await message.add_reaction(icons.WARRIOR)
    await message.add_reaction(icons.MAGE)
    await message.add_reaction(icons.ROGUE)
    await message.add_reaction(icons.RANGER)

    # get user reaction
    reaction = await self.wait_for_reaction(message, name, 5)
    return message, reaction

  async def confirm_character_embed(self, ctx: commands.Context, message: discord.message, name: str, reaction: icons):
    """embed menu for character confirmation"""

    # build embed
    embed = discord.Embed(title='%s - %s' % (ctx.author.name, name), color=Color.green())
    embed.set_thumbnail(url=icons.ROGUE_URL)
    embed.add_field(name=reaction, value='CLASS DESCRIPTION HERE', inline=False)
    embed.set_footer(text="%s to confirm - %s to pick another class" % (reaction, icons.X))

    # add reaction options
    await message.clear_reactions()
    await message.edit(embed=embed)
    await message.add_reaction(reaction)
    await message.add_reaction(icons.X)

    # get user reaction
    reaction = await self.wait_for_reaction(message, name, 5)
    return message, reaction

  async def character_creation(self, bot: commands.Bot, ctx: commands.Context, name: str):
    """ loops through character creation embed menus
        returns user's selected class"""

    # TODO: CREATE LOOP

    # select character - break loop if None (timeout)
    message, reaction = await self.select_character_embed(self.ctx, name)
    if reaction is None: return None

    # confirm character - break loop if None (timeout)
    message, reaction = await self.confirm_character_embed(self.ctx, message, name, reaction)
    if reaction is None: return None

    # reloop if user did not confirm
    if str(reaction) == str(icons.X):
      await self.ctx.send('reloop character create')
    else:
      return reaction

    return None


# NEED SOMEONE TO TEST REACTIONS IN BETWEEN STEPS
class PlayerCommands(commands.Cog):
  """Player specific commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command('createchar')
  async def createchar(self, ctx: commands.Context, *, name: str):
    """create character"""

    # create character
    player_utils = PlayerUtils(bot=self.bot, ctx=ctx)
    char = await player_utils.character_creation(self.bot, ctx, name)

    # timeout - exit command
    if (char is None): return
    await ctx.send('%s created %s - %s!!' % (ctx.author.name, char, name))

    # TODO: INSTANTIATE AND SAVE CHARACTER
    # TODO: CREATE CHARACTER SUMMARY EMBED


def setup(bot: commands.Bot):
  bot.add_cog(PlayerCommands(bot))
