from discord.ext import commands
import discord

class SillyCommands(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot
    # self.bureau = 943930062519021580
    # self.hue = 270777655496802304
    self.soggy_general = 750112550166986896
    self.admin = 211188620076253186

  @commands.command('send', hidden=True)
  async def send(self, ctx: commands.Context, *, text: str):
    if ctx.author.id != self.admin: return
    channel: discord.TextChannel = self.bot.get_channel(self.soggy_general)
    await channel.send(text)

  @commands.command('react', hidden=True)
  async def react(self, ctx: commands.Context, message_id: int, reaction: str):
    if ctx.author.id != self.admin: return
    channel: discord.TextChannel = self.bot.get_channel(self.soggy_general)
    msg: discord.Message = await channel.fetch_message(message_id)
    await msg.add_reaction(reaction)

  @commands.command('dm', hidden=True)
  async def dm(self, ctx: commands.Context, user_id: int, *, text: str):
    if ctx.author.id != self.admin: return
    user: discord.User = self.bot.get_user(user_id)
    await user.send(text)

def setup(bot: commands.Bot):
  bot.add_cog(SillyCommands(bot))
