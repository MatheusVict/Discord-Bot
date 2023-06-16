from discord.ext import commands 
import discord
from dotenv import load_dotenv
import os

load_dotenv()

token_key = os.getenv('DISCORD_BOT_TOKEN')

# function's name is commad's name

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def info(context):
    """
    context (information about how the command was executed)

    !info
    """
    await context.send(context.guild)
    await context.send(context.author)
    await context.send(context.message.id)


@bot.command()
async def punch(context, arg):
    """
    !punch Justin
    """
    await context.send(f'Punched {arg}')

@bot.command()
async def double_punch(context, arg1, arg2):
    """
    !double_punch Justin Emanuel
    """
    await context.send(f'Punched {arg1} and {arg2}')

@bot.command()
async def roundhouse_kick(context, *args):
    """
    !roundhouse_kick Justin Emanuel João
    """
    everyone = ', '.join(args)
    await context.send(f'Roundhouse kiked {everyone}')

bot.run(token_key)