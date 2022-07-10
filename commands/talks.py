from discord.ext import commands

class Talks(commands.Cog):
    """Talks with user on discord."""

    def __init__(self,bot):
        self.bot = bot
    
def setup(bot):
    bot.add_cog(Talks(bot))

