from discord.ext import commands , tasks
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
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

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
