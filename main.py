import discord
import os
import random

chance = 25

client = discord.Client()
token = os.getenv('TOKEN')

#Эта функция работает следующим образом: берется рандомное число от 0 до 100
# если шанс меньше этого числа, то нам похуй(True), а если шанс больше(False), то работаем дальше 
def check_chance():
    current = random.randrange(0, 100)      #подсказка: шанс зависит от длины интервала
    #для дебага
    #print(chance < current)
    #print(chance, current)
    return chance < current

#Эта функция смотрит сообщение пользователя и если оно соответсует требованиям - мы шлем ответку
def bot_respond(message):
  msg = str(message.content).lower()
  if msg.endswith('пизда'):
    return 'Да'
  if(msg.endswith('да') and not(msg.endswith('пизда'))):
    return 'Пизда'
  if(msg.endswith(' нет') or msg.endswith('нет')):
    return 'Пидора ответ'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message : str):
    if (message.author == client.user) or check_chance():
      return
    await message.channel.send(bot_respond(message))
    
client.run(token)