import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

# OTQ5MzQ4OTY2NjA3MjQ1Mzky.YiJEHw.klFNg13xwyuyDuDJAl8dtzmJxz8

load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)
# bot.load_extension("commands.somecommands")
bot.load_extension('commands.playercommands')
bot.run(getenv('TOKEN'))

# TODO: EXCEPTION HANDLER VS COMMAND SPECIFIC
