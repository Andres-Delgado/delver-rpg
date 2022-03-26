import discord
from discord.ext import commands
from discord import Color
import constants.icons as icons

class StoreUtils():
  def __init__(self):
    self.rando = 10

  async def show_store_embed(self, ctx: commands.Context):
    """"shows store menu"""

    # build embed - buy store
    embed = discord.Embed(title='Wut are ya buyin?', description='Temporary Instruction', color=Color.gold())
    embed.add_field(
      name='Buy',
      value='%s `healing potion (10g)`\n%s `stam potion (15g)`\n%s `dagger (50g)`' % (icons.ONE, icons.TWO, icons.THREE)
    )

    embed.add_field(name='Rare Item', value='%s Elvish Sword' % icons.RED, inline=False)
    embed.set_footer(text='*Dont let the door hit you on the way out*')

    # embed.add_field(name='3 dagger', value='50g')
    embed.set_thumbnail(url=icons.STORE_URL)
    message: discord.Message = await ctx.send(embed=embed)

    # add reaction options
    await message.add_reaction(icons.ONE)
    await message.add_reaction(icons.TWO)
    await message.add_reaction(icons.THREE)

class StoreCommands(commands.Cog):
  """Store specific commands"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command('store')
  async def create(self, ctx: commands.Context):
    """open shop"""

    store = StoreUtils()
    await store.show_store_embed(ctx)

def setup(bot: commands.Bot):
  bot.add_cog(StoreCommands(bot))
