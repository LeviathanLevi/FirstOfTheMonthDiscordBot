# FOTMBot.py
import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-$')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    response = 'Hi, I\'m a bot created by Levi, every first of the month I\'ll post a link to a the Bone Thugs n Harmony - First of the month song\nType add followed by the name to add someone to the mention list when the bot posts.\nType delete followed by the name to remove a person from the mention list.\n example "-$add Leviathan" or "-$delete Leviathan"'
    await ctx.send(response)

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
    found = 0
    namesInList = fo.read()
    print(namesInList) #debug
    for kv in namesInList.split(","):
        print(kv) #debug
        if kv == name:
            found = 1
            namesInList = namesInList.replace(name+',', '')
            fo.close()
            break

    if found == 1:
        print(namesInList + "Test") #debug
        fo = open("mentionList.txt", "w")
        fo.write(namesInList)
        fo.close()
        response = 'Removed: {} from the mention list.'.format(name)
    else:
        response = 'Could not find: {} in the mention list.'.format(name)

    await ctx.send(response)



bot.run(TOKEN)