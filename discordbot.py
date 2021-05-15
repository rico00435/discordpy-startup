from discord.ext import tasks
import discord

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

channel_sent = None
@tasks.loop(seconds=10)
async def send_message_every_10sec():
    await channel_sent.send("test")

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(797040818794921984)
    send_message_every_10sec.start()

bot.run(token)
