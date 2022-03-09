import asyncio
import discord
import icons

from discord import Color
from discord.ext import commands

class PlayerUtils():

  def __init__(self, bot: commands.Bot, ctx: commands.Context, name: str):
    self.bot = bot
    self.ctx = ctx
    self.name = name

  # TODO: OPTIMIZE THIS PLS
  def check(self):
    return lambda r, u: u == self.ctx.author and str(r.emoji) \
      in icons.WARRIOR + icons.MAGE + icons.ROGUE + icons.RANGER + icons.X

  async def wait_for_reaction(self, message: discord.message, timeout: int):
    """get user reaction, returns None if timeout or invalid reaction"""

    try:
      # wait for reaction
      reaction, user = await self.bot.wait_for('reaction_add', check=self.check(), timeout=timeout)

      # this check might be done already by self.check()
      if user.id == self.ctx.author.id:
        return reaction

    # timeout - display error embed
    except asyncio.TimeoutError:
      await message.clear_reactions()
      timeout_embed = discord.Embed(title='%s - %s' % (self.ctx.author.name, self.name), color=Color.red())
      timeout_embed.add_field(name='Character Creation Timed Out!', value='input `.createchar <character_name>` to attempt again', inline=False)
      await message.edit(embed=timeout_embed)

    return None

  async def select_character_embed(self, message: discord.message = None):
    """menu for character selection"""

    # build embed
    embed = discord.Embed(title=self.name, description='Choose your class!', color=Color.green())
    embed.add_field(name=icons.WARRIOR + ' Warrior', value='Party Buff: dmg reduction', inline=False)
    embed.add_field(name=icons.MAGE + ' Mage', value='Party Buff: amplify consumables', inline=False)
    embed.add_field(name=icons.ROGUE + ' Rogue', value='Party Buff: dmg buff', inline=False)
    embed.add_field(name=icons.RANGER + ' Ranger', value='Party Buff: reduce stamina consumption', inline=False)

    # send embed
    if message:
      await message.clear_reactions()
      await message.edit(embed=embed)
    else:
      message = await self.ctx.send(embed=embed)

    # add reaction options
    await message.add_reaction(icons.WARRIOR)
    await message.add_reaction(icons.MAGE)
    await message.add_reaction(icons.ROGUE)
    await message.add_reaction(icons.RANGER)

    # get user reaction
    reaction = await self.wait_for_reaction(message, 10)
    return message, reaction

  async def confirm_character_embed(self, message: discord.message, reaction: icons):
    """menu for character confirmation"""

    # build embed
    embed = discord.Embed(title=self.name, color=Color.green())
    embed.set_thumbnail(url=icons.ROGUE_URL)
    embed.add_field(name='%s CLASS_NAME' % reaction, value='CLASS DESCRIPTION HERE', inline=False)
    embed.set_footer(text='%s to confirm - %s to pick another class' % (reaction, icons.X))

    # add reaction options
    await message.clear_reactions()
    await message.edit(embed=embed)
    await message.add_reaction(reaction)
    await message.add_reaction(icons.X)

    # get user reaction
    reaction = await self.wait_for_reaction(message, 10)
    return message, reaction

  async def show_summary_embed(self, message: discord.message, reaction: icons):
    """display character summary"""

    embed = discord.Embed(title='%s %s - lv 1' % (reaction, self.name), description='ClASS_NAME Exp 0/100', color=Color.light_grey())
    embed.set_thumbnail(url=icons.ROGUE_URL)
    embed.add_field(name='Health', value='20/20')
    embed.add_field(name='Stamina', value='20/20')
    embed.add_field(name='Armor', value='10/10')

    embed.add_field(name='Armor', value='%s Leather Chestpiece' % icons.WHITE_LG, inline=False)
    embed.add_field(name='Weapon', value='%s Simple Dagger' % icons.GREEN, inline=False)
    embed.add_field(name='Accessory', value='%s Isildur\'s Bane' % icons.BLUE, inline=False)
    embed.add_field(name='Equiped Item', value='2x Lesser Healing Potion (+10)', inline=False)
    embed.add_field(name='Inventory (10 gold)', value='1x Lesser Stamina Potion (+5)')
    embed.set_footer(text=self.ctx.author.name)

    await message.clear_reactions()
    await message.edit(embed=embed)

  async def character_creation(self):
    """loops through character creation embed menus, returns user's selected class"""

    message, reaction = None, None
    while reaction is None:
      # select character - break loop if None (timeout)
      message, reaction = await self.select_character_embed(message)
      if reaction is None: return None

      # confirm character - break loop if None (timeout)
      message, reaction = await self.confirm_character_embed(message, reaction)
      if reaction is None: return None

      # user did not confirm character
      if str(reaction) == str(icons.X):
        reaction = None


    await self.show_summary_embed(message, reaction)
    return reaction

# NEED SOMEONE TO TEST REACTIONS IN BETWEEN STEPS
class PlayerCommands(commands.Cog):
  """Player specific commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command('create')
  async def create(self, ctx: commands.Context, *, name: str):
    """create character"""

    # create character
    player_utils = PlayerUtils(self.bot, ctx, name)
    char = await player_utils.character_creation()

    # timeout - exit command
    if (char is None): return

    await ctx.send('Input `.menu` to get started!')

    # TODO: SAVE CHAR TO DB
    # TODO: player_utils.show_summary_embed(character)

def setup(bot: commands.Bot):
  bot.add_cog(PlayerCommands(bot))
