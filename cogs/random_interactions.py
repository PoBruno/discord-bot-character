import random
from discord.ext import commands
from utils.chatgpt_api import generate_character_response

class RandomInteractions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if random.random() < 0.1:  # 10% chance de responder aleatoriamente
            response = generate_character_response(message.content)
            await message.channel.send(response)

def setup(bot):
    bot.add_cog(RandomInteractions(bot))
