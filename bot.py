 # bot.py
import os
import time
import discord
import random


TOKEN = ("Sorry, can't tell you that!")

@bot.event
async def on_ready():
    print(
        f'{bot.user} is connected to discord!'
    )
        
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to the server!"
    )
 
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
        
    if "lasagna" in message.content.lower() or "lasagne" in message.content.lower():
        response = "did somebody say lasagna?"
        await message.channel.send(response)

    if message.content.lower() == "garfdaily":
        localtime = time.gmtime()
        if len(str(localtime.tm_mday)) == 1:
            day = "0" + str(localtime.tm_mday)
            print (day)
        else:
            day  = localtime.tm_mday
                
        garfFileName = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/2019/"+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+day+".gif"
        
        await message.channel.send(garfFileName)
        print ("A user requested this comic:", garfFileName)
    
    if message.content.lower() == "garftrivia":
        trivias = ["Trivia fact #1: Garfield is an orange cat"]
        await message.channel.send(random.choice(trivias))

bot.run(TOKEN)
