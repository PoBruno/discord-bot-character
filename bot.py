import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='mongatron ', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.load_extension('cogs.character_interactions')
    bot.load_extension('cogs.random_interactions')

if __name__ == "__main__":
    bot.run(TOKEN)
