
from decouple import config
from discord.ext import commands, tasks

bot = commands.Bot('!sb')

TOKEN = config('token')
bot.run(TOKEN)
