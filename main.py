import asyncio
import random
import string
import time
from string import ascii_lowercase
import bs4
import discord
from discord import FFmpegPCMAudio
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from youtube_dl import YoutubeDL
import math

app = commands.Bot(command_prefix="pls ")

link = ['https://discord.gg']
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


alpha = list(ascii_lowercase)
# bigalpha = string.upper(alpha)

@app.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 접속해주세요")

@app.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 그 채널에 속해있지 않아요")

@app.command()
async def URL재생(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

app.run(token)