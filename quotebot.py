import discord
import os

# invite: https://discordapp.com/api/oauth2/authorize?client_id=605969794583232542&scope=bot&permissions=67584

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.author.name} ({message.author}) says \"{message.content}\" in channel #{message.channel}")

    guild = client.get_guild(605965627097743402)

    if "!membercount" in message.content.lower() or "!count" in message.content.lower():
        await message.channel.send(f"```{guild.member_count}```") # find a way to subtract number of bots!!!!!!

    if "!fly me to the moon" in message.content.lower():
        await message.channel.send("Enjoy :) https://www.youtube.com/watch?v=kTxRm9HD7lo")

    if "!logout" in message.content.lower() or "!leave" in message.content.lower() or "!bye" in message.content.lower():
        await message.channel.send("Goodbye :wave:")
        await client.close()

    if "!memberlist" in message.content.lower():
        
        for m in guild.members:
            await message.channel.send(f"```{m.display_name}::{m.top_role} ({m.status})```")

    if "!banlist" in message.content.lower():

        for m in await guild.bans():
            await message.channel.send(f"```{m.user} {m.reason}```")

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

        await message.channel.send(f"Offline: {offline}\nOnline: {online}\nIdle: {idle}\nDnd: {dnd}")


client.run(os.environ.get("BOT_TOKEN"))

