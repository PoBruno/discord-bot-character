from discord.ext import commands
from utils.chatgpt_api import generate_character_response

class CharacterInteractions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='speak')
    async def speak(self, ctx, *, prompt):
        response = generate_character_response(prompt)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(CharacterInteractions(bot))
