import discord
from discord.ext import commands
from youtube import Youtube
import time
import os

yt = Youtube()


intents = discord.Intents.all()


bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('.test'):
        connect = message.author.voice.channel
        await message.channel.send(connect)
    else:
        await bot.process_commands(message)


@bot.command()
async def s(ctx, arg):
    await ctx.send(arg)
    channel = ctx.author.voice.channel
    await channel.connect()


# @bot.command()
# async def join(ctx):
#     if not ctx.author.voice:
#         await ctx.send(f"voice channel m toh ja chutiye!")
#     else:
#         await ctx.author.voice.channel.connect()


@bot.command()
async def dc(ctx):
    if ctx.voice_client and ctx.author.voice:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send(f"hatt randi!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f"tere ghar m nahi ho m")


@bot.command(aliases=["p"])
async def play(ctx, url):

    if not ctx.author.voice:
        await ctx.send(f"voice channel m toh ja chutiye!")
    else:
        if not ctx.voice_client:
            voice = await ctx.author.voice.channel.connect()
        else:
            voice = ctx.voice_client
        voice.play(discord.FFmpegPCMAudio(
            executable="ffmpeg", source=yt.get_audio_link(url)))

        while voice.is_playing():
            time.sleep(.1)
        await voice.disconnect()


@bot.command(aliases=["bha"])
async def bhau(ctx, url="https://www.youtube.com/watch?v=8l45gbmoMTE"):

    if not ctx.author.voice:
        await ctx.send(f"voice channel m toh ja chutiye!")
    else:

        if not ctx.voice_client:
            voice = await ctx.author.voice.channel.connect()
        else:
            voice = ctx.voice_client
        voice.play(discord.FFmpegPCMAudio(
            executable="ffmpeg", source=yt.get_audio_link(url)))

        while voice.is_playing():
            time.sleep(.1)
        await voice.disconnect()


bot.run(os.getenv("token"))
