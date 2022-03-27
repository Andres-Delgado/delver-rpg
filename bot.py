import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv


load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)
bot.load_extension('commands.playercommands')
bot.load_extension('commands.storecommands')
bot.load_extension('commands.sillycommands')
bot.run(getenv('TOKEN'))

# TODO: EXCEPTION HANDLER VS COMMAND SPECIFIC
