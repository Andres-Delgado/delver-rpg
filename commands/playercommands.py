import asyncio
import discord
from discord import Color
from discord.ext import commands

import constants.icons as icons
from player.player import Player

class PlayerUtils():
  def __init__(self, bot: commands.Bot, ctx: commands.Context, name: str, message: discord.Message = None):
    self.bot = bot
    self.ctx = ctx
    self.name = name
    self.message = message

  # TODO: OPTIMIZE THIS PLS
  def check(self):
    return lambda r, u: u == self.ctx.author and str(r.emoji) \
      in icons.WARRIOR + icons.MAGE + icons.ROGUE + icons.RANGER + icons.X

  async def wait_for_reaction(self, timeout: int):
    """get user reaction, returns None if timeout or invalid reaction"""

    try:
      # wait for reaction
      reaction, user = await self.bot.wait_for('reaction_add', check=self.check(), timeout=timeout)

      # this check might be done already by self.check()
      if user.id == self.ctx.author.id:
        return reaction

    # timeout - display error embed
    except asyncio.TimeoutError:
      await self.message.clear_reactions()
      timeout_embed = discord.Embed(title=self.name, color=Color.red())
      timeout_embed.add_field(name='Character Creation Timed Out!', value='input `.create <character_name>` to attempt again', inline=False)
      timeout_embed.set_footer(text=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)
      await self.message.edit(embed=timeout_embed)

    return None

  async def select_character_embed(self) -> icons:
    """menu for character selection"""

    # build embed
    embed = discord.Embed(title=self.name, description='Choose your class!', color=Color.green())
    embed.add_field(name=icons.WARRIOR + ' Warrior', value='Party Buff: dmg reduction', inline=False)
    embed.add_field(name=icons.MAGE + ' Mage', value='Party Buff: amplify consumables', inline=False)
    embed.add_field(name=icons.ROGUE + ' Rogue', value='Party Buff: dmg buff', inline=False)
    embed.add_field(name=icons.RANGER + ' Ranger', value='Party Buff: reduce stamina consumption', inline=False)
    embed.set_footer(text=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)

    # send embed
    if self.message is None:
      self.message = await self.ctx.send(embed=embed)
    else:
      await self.message.clear_reactions()
      await self.message.edit(embed=embed)

    # add reaction options
    await self.message.add_reaction(icons.WARRIOR)
    await self.message.add_reaction(icons.MAGE)
    await self.message.add_reaction(icons.ROGUE)
    await self.message.add_reaction(icons.RANGER)

    # get user reaction
    reaction = await self.wait_for_reaction(10)
    return reaction

  async def confirm_character_embed(self, reaction: icons) -> icons:
    """menu for character confirmation"""

    # TODO: MOVE OUT OF HERE PLS
    class_name, icon_url = '', ''
    if str(reaction) == str(icons.WARRIOR):
      class_name = 'WARRIOR'
      icon_url = icons.WARRIOR_URL
    elif str(reaction) == str(icons.MAGE):
      class_name = 'MAGE'
      icon_url = icons.MAGE_URL
    elif str(reaction) == str(icons.ROGUE):
      class_name = 'ROGUE'
      icon_url = icons.ROGUE_URL
    elif str(reaction) == str(icons.RANGER):
      class_name = 'RANGER'
      icon_url = icons.RANGER_URL

    # build embed
    embed = discord.Embed(title='%s %s' % (reaction, self.name), color=Color.green())
    embed.set_thumbnail(url=icon_url)
    embed.add_field(\
      name=class_name,\
      value='CLASS DESCRIPTION HERE\n\n%s to confirm - %s to pick another class' % (reaction, icons.X)
    )
    embed.set_footer(text=self.ctx.author.name)#, icon_url=self.ctx.author.avatar_url)

    # add reaction options
    await self.message.clear_reactions()
    await self.message.edit(embed=embed)
    await self.message.add_reaction(reaction)
    await self.message.add_reaction(icons.X)

    # get user reaction
    reaction = await self.wait_for_reaction(10)
    return reaction

  async def character_creation(self) -> icons:
    """loops through character creation embed menus, returns user's selected class"""

    reaction = None
    while reaction is None:
      # select character - break loop if None (timeout)
      reaction = await self.select_character_embed()
      if reaction is None: return None

      # confirm character - break loop if None (timeout)
      reaction = await self.confirm_character_embed(reaction)
      if reaction is None: return None

      # user did not confirm character
      if str(reaction) == str(icons.X):
        reaction = None

    return reaction

  async def show_summary_embed(self, player: Player):
    """display character summary embed"""

    embed = discord.Embed(\
      title='%s %s - lv %s' % (player.clas_icon, player.name, player.level), \
      description=' %s Exp - %s/%s' % (player.class_name, player.experience, player.experience_max), \
      color=Color.light_grey()
    )
    embed.set_thumbnail(url=player.class_icon_url)
    embed.add_field(name='Hp', value='%s/%s' % (player.health, player.health_max))
    embed.add_field(name='Stam', value='%s/%s' % (player.stamina, player.stamina_max))
    embed.add_field(name='Armor', value=player.armor)

    embed.add_field(name='Gear', value=player.gear, inline=False)
    embed.add_field(name='Weapon', value=player.weapon, inline=False)
    # embed.add_field(name='Accessory', value='%s Isildur\'s Bane' % icons.BLUE, inline=False)
    # embed.add_field(name='Equiped Item', value='2x Lesser Healing Potion (+10)', inline=False)
    # embed.add_field(name='Inventory (10 gold)', value='1x Lesser Stamina Potion (+5)')
    embed.set_footer(text=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)

    await self.message.clear_reactions()
    await self.message.edit(embed=embed)

  def instantiate_player(self, reaction: icons) -> Player:
    class_name = ''
    hp, stam, armor = 20, 20, 10

    if str(reaction) == str(icons.WARRIOR):
      class_name = 'WARRIOR'
      armor = 15
    elif str(reaction) == str(icons.MAGE):
      class_name = 'MAGE'
    elif str(reaction) == str(icons.ROGUE):
      class_name = 'ROGUE'
    elif str(reaction) == str(icons.RANGER):
      class_name = 'RANGER'
      stam = 25

    return Player(self.ctx.author.id, class_name, self.name, hp, stam, armor)

# NEED SOMEONE TO TEST REACTIONS IN BETWEEN STEPS
class PlayerCommands(commands.Cog):
  """Player specific commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command('create')
  async def create(self, ctx: commands.Context, name: str):
    """create character"""

    # create character
    player_utils = PlayerUtils(self.bot, ctx, name)
    reaction = await player_utils.character_creation()

    # timeout - exit command
    if (reaction is None): return

    # TODO: MOVE TO CHARACTER CLASSES
    # initPlayer(self.ctx.author.id, class_name, self.name)
    # instantiate player object
    player = player_utils.instantiate_player(reaction)
    await player_utils.show_summary_embed(player)

    # await ctx.send('Input `.menu` to get started!')

    # TODO: SAVE CHAR TO DB

def setup(bot: commands.Bot):
  bot.add_cog(PlayerCommands(bot))
