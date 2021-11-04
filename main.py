import discord
from discord import channel
from discord import message
from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

channel_id = '####' #CHANNEL ID

#evento PRUEBA1
@client.event
async def on_reaction_add(reaction, user):
     if reaction.emoji == '⭐':
        print('PRUEBA')
        channel = client.get_channel(channel_id) #channel id here
        await channel.send(reaction.message.content)

#TOKEN
client.run('TOKEN')