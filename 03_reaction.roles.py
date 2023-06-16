import discord
from dotenv import load_dotenv
import os


load_dotenv()


token_key = os.getenv('DISCORD_BOT_TOKEN')



class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
      
        super().__init__(*args, **kwargs)
        self.target_message_id = 1119035383469064332

    async def on_ready(self):
        print(f'online, {self.user}')

    async def on_raw_reaction_add(self, payload):
        """
        Given a role based on emoji
        """

        if (payload.message_id != self.target_message_id):
            return 
        
        guild = self.get_guild(payload.guild_id)

        if(payload.emoji.name == '🐧'):
           role = discord.utils.get(guild.roles, name = 'Peguim person')
           await payload.member.add_roles(role)
        elif(payload.emoji.name == '😀'):
           role = discord.utils.get(guild.roles, name = 'Chocolate Lover')
           await payload.member.add_roles(role)
        elif(payload.emoji.name == '🥹'):
           role = discord.utils.get(guild.roles, name = 'monkey funcky')
           await payload.member.add_roles(role)


    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on emoji
        """

        if (payload.message_id != self.target_message_id):
            return 
        
        guild = self.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if(payload.emoji.name == '🐧'):
           role = discord.utils.get(guild.roles, name = 'Peguim person')
           await member.remove_roles(role)
        elif(payload.emoji.name == '😀'):
           role = discord.utils.get(guild.roles, name = 'Chocolate Lover')
           await member.remove_roles(role)
        elif(payload.emoji.name == '🥹'):
           role = discord.utils.get(guild.roles, name = 'smurf amarelo')
           await member.remove_roles(role) 


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)

client.run(token_key)