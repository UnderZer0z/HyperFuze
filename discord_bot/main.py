import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import webScraper 


# setting up .env vels
load_dotenv(dotenv_path='discord_bot/.env')
token = os.getenv('TOKEN')

# =========================================
# =========================================


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}!'.format(client))

# =========================================


@client.event
async def on_command_error(ctx, error):
    if isinstance(error , commands.MissingRequiredArgument):
        addserver = discord.Embed( title="Add a Server to list:", 
        description="כדי להוסיף שרת לאתר הנה הוסף את הפרטים הבאים. \n !add Name Game Server-IP Port")
        addserver.add_field( name='Name:',value='שם השרת', inline=False)
            # addserver.add_field( name='Description:',value='תיאור לגבי השרת', inline=False) # removed for simplicity reasons.
        addserver.add_field( name='Game:',value='לאיזה משחק השרת שלך?', inline=False)
        addserver.add_field( name='Server-IP:',value='כתובת האייפי של שרת המשחק', inline=False)
        addserver.add_field( name='Port:',value='כתובת הפורט של השרת', inline=False)
        await ctx.send(embed=addserver)

# =========================================


@client.command()
async def add(ctx, name , game , ip , port ):
    print(name , game , ip , port)
    webScraper.track_game(game,ip,port)
    print(ctx.author)
    await ctx.send("Server was add to HyperFuze DataBase! :)")
    
    
# =========================================
    

client.run(token)



