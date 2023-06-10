import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
sampah_anorganik =  ["plastik","besi","baja","emas"]
sampah_organik =  ["nasi padang","ayam","kayu","daun"]
# sampah = ["organik" , "anorganik"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
        
@bot.command()
async def pilih(ctx , sampah):
        if sampah in sampah_organik:
            await ctx.send("masukkan ke sampah sampah organik")
    

        if sampah in sampah_anorganik:
            await ctx.send("masukkan ke sampah sampah anorganik")
   
    # await ctx.send("nama sampah")
    # if msg.content in sampah_organik:
    #     await ctx.send("sampah oraganik")
bot.run("MTEwNjgwNTAxMDI5NTE3MzE3MA.Gpygzb.eVjkyiBgc5pmUBfTLR2Y8buACTOnotFuYjO1cM")
