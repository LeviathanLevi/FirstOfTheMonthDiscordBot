# FOTMBot.py
import os
import datetime

from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-$')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    response = 'Hi, I\'m a bot, every first of the month I\'ll post a link to a the Bone Thugs n Harmony - First Of The Month song.\nType -$add to be added to the mention list.\nType -$delete to be deleted from the mention list.\nReach out to Leviathan (Levi) for help.'
    await ctx.send(response)

@bot.command()
async def add(ctx):
    #check if they're already added:
    fo = open("mentionList.txt", "r")
    found = False
    namesInList = fo.read()
    for kv in namesInList.split(","):
        if kv == str(ctx.author.id):
            found = True
            namesInList = namesInList.replace(str(ctx.author.id)+',', '')
            fo.close()
            break

    if found == True:
        response = 'You are already added to the mention list.'
    else:
        fo = open("mentionList.txt", "a")
        fo.write(str(ctx.author.id) + ',')
        fo.close()
        response = 'You have been added to the mention list!'
    
    await ctx.send(response)
    
@bot.command()
async def delete(ctx):
    fo = open("mentionList.txt", "r")
    found = False
    namesInList = fo.read()
    for kv in namesInList.split(","):
        if kv == str(ctx.author.id):
            found = True
            namesInList = namesInList.replace(str(ctx.author.id)+',', '')
            fo.close()
            break

    if found == True:
        fo = open("mentionList.txt", "w")
        fo.write(namesInList)
        fo.close()
        response = 'You have been removed from the mention list!'
    else:
        response = 'You weren\'t in the mention list before so you can\'t be removed.'

    await ctx.send(response)

@tasks.loop(hours=6)
async def checkForFirstOfTheMonth():
    timestamp = datetime.datetime.now().day
    if timestamp == 1:
        await bot.wait_until_ready()
        channel = bot.get_channel(488489803051040791)
        #Mentions:
        mentionStr = ''
        fo = open("mentionList.txt", "r")
        namesInList = fo.read()
        for kv in namesInList.split(","):
            if kv != '':
                mentionStr = mentionStr + '<@' + kv + '> '
        
        await channel.send("IT'S THE FIRST OF THE MONTH. Listen to this song (Type -$help for bot help): https://www.youtube.com/watch?v=4j_cOsgRY7w&ab_channel=BoneThugsMusic " + mentionStr)
      
checkForFirstOfTheMonth.start()

bot.run(TOKEN)