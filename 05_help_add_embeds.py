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
# remove commands default
bot.remove_command('help')


# Custom help command embeded
@bot.command()
async def help(context):

    embed = discord.Embed(
        title = 'Bot Commands',
        description = 'Welcome to the help section. Here are all the commands for this game!',
        color = discord.Colour.dark_orange()
    )

    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/103688000?v=4')
    embed.add_field(
        name = '!help',
        value = 'List all of the commands',
        inline = False
    )
    embed.add_field(
        name = '!punch',
        value = 'Punch another player',
        inline = False
    )
    embed.add_field(
        name = '!roundhouse_kick',
        value = 'Roundhouse kick many players',
        inline = False
    )

    await context.send(embed=embed)
    

@bot.command()
async def punch(context, arg):
    """
    This command punches another player
    """
    await context.send(f'Punched {arg}')


@bot.command()
async def roundhouse_kick(context, *args):
    """
    This command kick many players from house
    """
    everyone = ', '.join(args)
    await context.send(f'Roundhouse kiked {everyone}')

bot.run(token_key)