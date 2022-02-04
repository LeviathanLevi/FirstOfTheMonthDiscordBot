# FOTMBot.py
import os
import discord
import datetime

from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-$')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    response = 'Hi, I\'m a bot created by Levi, every first of the month I\'ll post a link to a the Bone Thugs n Harmony - First of the month song\nType add followed by the name to add someone to the mention list when the bot posts.\nType delete followed by the name to remove a person from the mention list.\n example "-$add Leviathan" or "-$delete Leviathan" The mention feature actually isn\'t working rn, I\'ll fix it in the future'
    await ctx.send(response)

#TODO: Add and delete need to be remade to use individuals user IDs for mentioning in the future
@bot.command()
async def add(ctx, name):
    fo = open("mentionList.txt", "a")
    fo.write(name + ',')
    fo.close()
    response = 'Added: {} to the mention list.'.format(name)
    await ctx.send(response)

@bot.command()
async def delete(ctx, name):
    fo = open("mentionList.txt", "r")
    found = False
    namesInList = fo.read()
    for kv in namesInList.split(","):
        if kv == name:
            found = True
            namesInList = namesInList.replace(name+',', '')
            fo.close()
            break

    if found == True:
        fo = open("mentionList.txt", "w")
        fo.write(namesInList)
        fo.close()
        response = 'Removed: {} from the mention list.'.format(name)
    else:
        response = 'Could not find: {} in the mention list.'.format(name)

    await ctx.send(response)

@tasks.loop(hours=6)
async def checkForFirstOfTheMonth():
    timestamp = datetime.datetime.now().day
    if timestamp == 1:
        await bot.wait_until_ready()
        channel = bot.get_channel(488489803051040791)
        #channel = bot.get_channel(642555024328622090) music channel for testing
        #mentions:
        # mentionStr = ''
        # fo = open("mentionList.txt", "r")
        # namesInList = fo.read()
        # for kv in namesInList.split(","):
        #     mentionStr = mentionStr + '@' + kv + ' '
        await channel.send("IT'S THE FIRST OF THE MONTH. Listen to this song: https://www.youtube.com/watch?v=4j_cOsgRY7w&ab_channel=BoneThugsMusic . This bot was made by Levi, type '-$help' for help ")
      
checkForFirstOfTheMonth.start()

bot.run(TOKEN)