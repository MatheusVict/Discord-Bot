import discord
from dotenv import load_dotenv
import os


load_dotenv()


token_key = os.getenv('DISCORD_BOT_TOKEN')


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is now online')
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    
    if(message.content == 'hello there'):
        await message.channel.send('GENERAL KNOBI')
        await message.add_reaction('\N{THUMBS UP SIGN}')

    if (message.content.startswith('$hello')):
        await message.channel.send('Hello!')

client.run(token_key)