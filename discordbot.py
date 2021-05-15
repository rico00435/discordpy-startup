from discord.ext import tasks
import discord

client = discord.Client()

BOT_TOKEN = "hogehoge"
CHANNEL_ID = 817359255703257098
channel_sent = None

@tasks.loop(minutes=120)
    channel_sent = client.get_channel(CHANNEL_ID)
    async def send_message_every_120min():
    await channel_sent.send("!d bump")

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(any_channel_id)
    send_message_every_120min.start()
    
    client.run(BOT_TOKEN)
