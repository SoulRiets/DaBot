import discord
import os
import random

chance = 25

client = discord.Client()
token = os.getenv('TOKEN')

def checkChance():
    current = random.randrange(0, 100)
    return chance > current

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message : str):
    if ((message.author == client.user) and not(checkChance())):
        return
    msg = str(message.content).lower()
    if msg.endswith('пизда'):
      await message.channel.send('Да')
    if(msg.endswith('да') and not(msg.endswith('пизда'))):
        await message.channel.send('Пизда')

client.run(token)