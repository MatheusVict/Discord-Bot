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
    
@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message. \n'
        f'Before: {before.content}\n'
        f'After {after.content}'
    )

@client.event
async def on_reaction_add(reaction, user):
   await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')




client.run(token_key)