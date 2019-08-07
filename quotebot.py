import discord
import os
import quotes
import random

# invite: https://discordapp.com/api/oauth2/authorize?client_id=605969794583232542&scope=bot&permissions=67584

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.author.name} ({message.author}) says \"{message.content}\" in channel #{message.channel}")

    guild = client.get_guild(605965627097743402) # get the server using its ID

    # BOT COMMANDS

    # list the number of members
    if "!membercount" in message.content.lower() or "!count" in message.content.lower():
        await message.channel.send(f"```{guild.member_count}```") # find a way to subtract number of bots!!!!!!

    # play "Fly Me To The Moon"
    if "!fly me to the moon" in message.content.lower():
        await message.channel.send("Enjoy :) https://www.youtube.com/watch?v=kTxRm9HD7lo")

    # go offline
    if "!logout" in message.content.lower() or "!leave" in message.content.lower() or "!bye" in message.content.lower():
        await message.channel.send("Goodbye :wave:")
        await client.close()
    
    # list the members along with their status
    if "!memberlist" in message.content.lower():
        
        for m in guild.members:
            await message.channel.send(f"```{m.display_name}::{m.top_role} ({m.status})```")
    
    # list the members that have been banned from the server
    if "!banlist" in message.content.lower():

        for m in await guild.bans():
            await message.channel.send(f"```{m.user}::{m.reason}```")

    # list the number of people online, offline, idle, and dnd (do not disturb)
    if "!statusreport" in message.content.lower() or "!statuses" in message.content.lower():
        offline = 0
        online = 0
        idle = 0
        dnd = 0

        for m in guild.members:
            
            if str(m.status) == "offline":
                offline += 1

            elif str(m.status) == "online":
                online += 1

            elif str(m.status) == "idle":
                idle += 1

            elif str(m.status) == "dnd":
                dnd += 1

        await message.channel.send(f"```Offline: {offline}\nOnline: {online}\nIdle: {idle}\nDnd: {dnd}```")

    # lists quotes found for given argument (media)
    if "!quotelist " in message.content.lower():

        media = message.content.lower().replace("!quotelist ","")

        await message.channel.send(f"_**{media.upper()} QUOTES**_")
        
        quote_list = quotes.get_quotes(media)

        if quote_list == []:
            await message.channel.send("Sorry, no quotes were found :/")

        else:
            for quote in quote_list:
                await message.channel.send(f"```{quote}```")

    # lists a single quote for the given argument (media)
    if "!quote " in message.content.lower():

        media = message.content.lower().replace("!quote ","")

        quote_list = quotes.get_quotes(media)

        if quote_list == []:
            await message.channel.send("Sorry, no quotes were found :/")

        else:
            await message.channel.send(f"```{random.choice(quote_list)}```")

# run the bot
client.run(os.environ.get("BOT_TOKEN"))

