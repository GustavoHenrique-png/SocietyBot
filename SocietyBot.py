from datetime import datetime
from unicodedata import name
import discord
from discord.ext import commands, tasks

bot = commands.Bot('!sb')


@bot.event
async def on_ready():
    print('Here is hoe society')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif 'xingamentos' in message.content:
        await message.channel.send('teu cu')

        await message.delete()
    await bot.process_commands(message)


@bot.command(name='oe')
async def Welcome(ctx):
    name = ctx.author.name
    answer = 'Olá, '+name+' bem vindo a nossa humilde sociedade'

    await ctx.send(answer)

#
#@tasks.loop(seconds='20')
#async def current_time():
 #   now = datetime.datetime.now()
  #  now = strftime('%Y-%m-%d %H:%M:%')
#
bot.run('OTkyOTA0NjAyNDI3MDgwNzM0.GXIBUZ.G3eCT__gMeFsGK2RkMrnKjrPEwrdlciWcG2iI4')
