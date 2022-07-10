from discord.ext import commands

class Reaction(commands.Cog):
    """Give a charge to user through reactions."""

    def __init__(self,bot):
        self.bot = bot
    
    #events
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if(reaction.emoji == '🍌'):
            role = user.guild.get_role(995544384793759915)
            await user.add_roles(role)
        else:
            pass
    
def setup(bot):
    bot.add_cog(Reaction(bot))

