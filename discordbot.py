from discord.ext import tasks
import discord

client = discord.Client()

channel_sent = None

@tasks.loop(seconds=10)
    async def send_message_every_120min():
    await channel_sent.send("わわわ!d わわわbump")

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(797040818794921984)
    send_message_every_120min.start()
    
client.run("hogehogetoken")
