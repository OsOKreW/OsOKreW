#OsOKreW by Giovy52845

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time

bot = commands.Bot(command_prefix='#')
client = discord.Client()

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)


@client.event
async def on_message(message):
    if message.content == "cookie":
await client.send_message(message.channel, ":cookie:")

client.run(str(os.environ.get('BOT_TOKEN')))
