from datetime import datetime
from unicodedata import name
from urllib import response
import discord
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


@bot.command(name = 'oe')
async def send_hello(ctx):
    name = ctx.author.name
    answer = 'Olá, '+name+' bem vindo a nossa humilde sociedade'

    await ctx.send(answer)

@bot.command (name = 'binance')
async def cripto(ctx,coin,base ):

    try: 
        response = requests.get(f'https://api3.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')

        content = response.json()
        price = content.get('price')

        if(price):
            await ctx.send(f'O {coin}/{base} ta valendo {price}')
        else:
            await ctx.send(f'Essa moeda ai {coin}/{base}, ce acabou de inventar')
    except:
        await ctx.send(f'Tem parada errada ai irmão')

@bot.command(name = 'calc')
async def calculate_expression(ctx,*expression):

    expression = ''.join(expression)
    response = eval(expression)

    await ctx.send('Calculei que: '+str(response))

#@tasks.loop(seconds='20')
#async def current_time():
 #   now = datetime.datetime.now()
  #  now = strftime('%Y-%m-%d %H:%M:%')
#
bot.run('OTkyOTA0NjAyNDI3MDgwNzM0.GA9SzY.2u_NOkNUWe1a9XY6CAPe9F1KV1Zs5vNSnxlyr8')
