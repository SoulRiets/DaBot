import discord
import os
import random


client = discord.Client()
token = os.getenv('TOKEN')

def checkChance():
    chance = 20
    current = random.randrange(0, 100)
    return chance > current

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message : str):
    if (message.author == client.user):
        return
    if not(checkChance()):
        return
    msg = str(message.content).lower()
    if msg.endswith('пизда'):
      await message.channel.send('Да')
    if(msg.endswith('да') and not(msg.endswith('пизда'))):
        await message.channel.send('Пизда')

client.run(token)