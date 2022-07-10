from datetime import datetime
from pydoc import describe
from tkinter import E
from turtle import color
from unicodedata import name
from urllib import response
from cv2 import DescriptorMatcher
import discord
from numpy import tile
import requests
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


@bot.event
async def on_reaction_add(reaction, user):
    if(reaction.emoji == '🍌'):
        role = user.guild.get_role(995544384793759915)
        await user.add_roles(role)
    else:
        pass


@bot.command(name='oe')
async def send_hello(ctx):
    name = ctx.author.name
    answer = 'Olá, '+name+' bem vindo a nossa humilde sociedade'

    await ctx.send(answer)


@bot.command(name='binance')
async def cripto(ctx, coin, base):

    try:
        response = requests.get(
            f'https://api3.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')

        content = response.json()
        price = content.get('price')

        if(price):
            await ctx.send(f'O {coin}/{base} ta valendo {price}')
        else:
            await ctx.send(f'Essa moeda ai {coin}/{base}, ce acabou de inventar')
    except:
        await ctx.send(f'Tem parada errada ai irmão')


@bot.command(name='calc')
async def calculate_expression(ctx, *expression):

    expression = ''.join(expression)
    response = eval(expression)

    await ctx.send('Calculei que: '+str(response))


@bot.command(name='fotinha')
async def get_random_image(ctx):
    urlImage = 'https://picsum.photos/1920/1080'

    embed = discord.Embed(tile='teste', descrition='teste2', color=0x000000)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_image(url=urlImage)
    embed.add_field(name='API', value='viadage né')
    embed.add_field(name='Ex:', value=urlImage, inline=False)

    await ctx.send(embed=embed)


# @tasks.loop(seconds='20')
# async def current_time():
 #   now = datetime.datetime.now()
  #  now = strftime('%Y-%m-%d %H:%M:%')
#
bot.run('OTkyOTA0NjAyNDI3MDgwNzM0.GLhTmG.eTeQhoes6cl9w3mAFVz4unWag6ekvdwcAtUeaE')

# https://picsum.photos/200/300
