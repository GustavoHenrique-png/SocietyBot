from discord.ext import commands
import requests

class Crypto(commands.Cog):
    """Send to user a valor of a crypto."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='binance')
    async def cripto(self, ctx, coin, base):

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


def setup(bot):
    bot.add_cog(Crypto(bot))
