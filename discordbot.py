from discord.ext import tasks
import discord

client = discord.Client()

channel_sent = None

@tasks.loop(minutes=1)
async def send_message_every_120min():
    await channel_sent.send("!d bump")


@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(any_channel_id)
    send_message_every_120min.start()


   
client.run("hogehogetoken")
