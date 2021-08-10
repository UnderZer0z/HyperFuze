import discord
import os
import json
from dotenv import load_dotenv


# setting up .env vels
load_dotenv(dotenv_path='discord_bot/.env')
token = os.getenv('TOKEN')


# bot script stats here
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == '🤖add-discord-server':
        if message.content.startswith('!add'):
            await message.channel.send('')
    else:
        return







client.run(token)