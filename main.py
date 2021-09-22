import os
import random
import discord
import youtube_dl

from discord.ext import commands
from dotenv import load_dotenv
from flask import ctx

from keep_alive import keep_alive

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = commands.Bot(command_prefix='.', help='Responds with an ultra whack, true-to-form Justin Macalis Quote!')


@client.event
async def message(message):
    if client.user.id != message.author.id:

        if 'poo' in message.content:
            await message.channel.send('poopie')

        if 'dyke' in message.content:
            await message.channel.send('https://imgur.com/yzBkxqr')

        if 'probot back' in message.content:
            await message.channel.send('https://imgur.com/sZUKN34')

        if 'probot sad' in message.content:
            await message.channel.send('https://imgur.com/pPw7cxV')

        if 'probot happy' in message.content:
            await message.channel.send('https://imgur.com/F8UVoTS')

        if 'probot palpitate' in message.content:
            await message.channel.send('https://tenor.com/view/heart-beat-gif-11130010')

        if 'probot out' in message.content:
            await message.channel.send('https://imgur.com/1w3hkZV')

        if 'probot in' in message.content:
            await message.channel.send('https://imgur.com/PMsz450')

        if 'eryk' in message.content:
            await message.channel.send('https://imgur.com/XucZNYs')

        if 'james' in message.content:
            await message.channel.send('https://tenor.com/view/james-gif-21370572')

        if 'xylophone' in message.content:
            await message.channel.send('https://imgur.com/n7gKDfZ')

        if 'stink' in message.content:
            await message.channel.send('Your butt stinks')

        if 'fuck' in message.content:
            await message.channel.send('Its fine')

        if 'short' in message.content:
            await message.channel.send('5 foot 3 but attitude 6 foot 2')

        if 'chimp' in message.content:
            await message.channel.send(
        'https://cdn.discordapp.com/attachments/425396946325471235/808810346940596255/flattenscalejpeg_quality70.png')

        if 'stock' in message.content:
            await message.channel.send('Yall see dogecoin went up?')

        if 'suck' in message.content:
            dogwater_quotes = [
                'Literally free?',
                'Dogwater?',
                'Earnings check oh wait you have none?',
                'Dollar tree headset?',
                'Your literally lost?',
            ]

            response = random.choice(dogwater_quotes)
            await message.channel.send(response)

        if 'brb' in message.content:
            await message.channel.send('I gotta go too my mom is calling')

        if 'burn' in message.content:
            await message.channel.send('https://cdn.ebaumsworld.com/mediaFiles/picture/2192630/84352249.jpg')

        if 'nick' in message.content:
            await message.channel.send('https://i.pinimg.com/originals/d9/a8/53/d9a853e8c7a849a7a17ba0d07e91aa02.jpg')

        if 'haley' in message.content:
            await message.channel.send('https://imgur.com/kmOenKc')

        if 'hanna' in message.content:
            await message.channel.send('https://imgur.com/a/6Wh3yDB')
            await client.process_commands(message)

    if 'sal' in message.content:
        await message.channel.send('https://imgur.com/wEd7eyf')
        await client.process_commands(message)

    if 'justin' in message.content:
        await message.channel.send(
            'https://static.wikia.nocookie.net/be-like-bro/images/c/cf/Chad.jpg/revision/latest/scale-to-width-down/834?cb=20180403173350')
        await client.process_commands(message)

    if 'trans' in message.content:
        await message.channel.send('https://i.imgur.com/9aHXsU4.png')
    await client.process_commands(message)

    if 'fix' in message.content:
        await message.channel.send('https://imgur.com/Np5Ezcq')
    await client.process_commands(message)

    if 'basketball' in message.content:
        await message.channel.send('https://imgur.com/dNJEZDs')

    await client.process_commands(message)

    @client.command()
    async def play():
        url: str
        song_playing = os.path.isfile("song.mp3")

        try:
            if song_playing:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Bot aint connected dog.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Aint no shit playing dumby")


client.command()


async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Its literally playing")


client.command()


async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.event
async def on_ready():
    print('Houston we are a go for launch')


# @client.event(SERVER)
# async def join(ctx):
#   channel = ctx.message.author.voice.voice_channel
#  await client.join_voice_channel(channel)


# @client.event(SERVER)
# async def leave(ctx):
#   server = ctx.message.server
#   voice_client = client.voice_client_in(server)
#  await voice_client.disconnect()


@client.command(name='Hanna')
async def hanna(ctx):
    HannaGar_quotes = [
        'Oh hey',
        'Its fine',
        'Ummm I dont know ',
        'The math just doesnt add up, 5 furnaces and 6 million jews? doesnt work',
        'Wanna see one of my dogs?',
        'I love stealing Grants hoodies',
        'Tommy Boy is the best movie ever made',
        'I HATE chicken parm',
        'Wanna get Mexican?',
        'OMG Big Mouth is so funny',
        'You\'re like totally a dumptruck',
        'hehe',
    ]
    response = random.choice(HannaGar_quotes)
    await ctx.send(response)


@client.command(name='dog', help='Randomly selects a picture of one of Hannas beautiful creatures')
async def pooger(ctx):
    PicsOf_Dogs = [
        'https://cdn.discordapp.com/attachments/807179505977786371/808815116845580298/image0.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815177763782667/image0.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815390494818347/image0.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815390867062784/image1.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815454574870558/image0.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815557809537064/image0.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815635236782120/image0.jpg',
        'https://cdn.discordapp.com/attachments/807179505977786371/808815822176911380/image0.jpg',
    ]
    response = random.choice(PicsOf_Dogs)
    await ctx.channel.send(response)


@client.command(name='roll', help='Simulates rolling dice. In the format: .roll_dice #ofdice #ofsides')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@client.command(name='number', help='picks a random number between 0-100')
async def rand(ctx):
    numb = [
        str(random.choice(range(0, 100)))
    ]
    await ctx.send(', '.join(numb))


@client.command(name='ping')
async def ping_pong(ctx):
    await ctx.send("PONGY WONGY")


@client.command(name='coolest')
async def coolest_kid(ctx):
    await ctx.send('https://imgur.com/l4gbK6B')


@client.command(name='bobby')
async def yugi_oh(ctx):
    await ctx.send("https://www.youtube.com/watch?v=fBBWHfXbP3o")


@client.command(name='literature')
async def chimpy(ctx):
    await ctx.send("https://www.youtube.com/watch?v=lTfGBCe-vpk")


@client.command(name='args', help='using the "." command type a statement you would like me to say :P')
async def arg_list(ctx, *args):
    response = ""

    for arg in args:
        response = response + " " + arg
        await ctx.send(response)


keep_alive()
client.run(TOKEN)
