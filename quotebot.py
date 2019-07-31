import discord
import os

# invite: https://discordapp.com/api/oauth2/authorize?client_id=605969794583232542&scope=bot&permissions=67584

client = discord.Client()

@client.event # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.author.name} ({message.author}) says \"{message.content}\" in channel #{message.channel}")

    if "fly me to the moon" in message.content.lower():
        await message.channel.send("Enjoy :) https://www.youtube.com/watch?v=kTxRm9HD7lo")

client.run(os.environ.get("BOT_TOKEN"))

