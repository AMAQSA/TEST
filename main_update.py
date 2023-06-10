# import discord
# from discord.ext import commands
# import os
# import random

# intents = discord.Intents.default()
# intents.message_content = True

# bot = commands.Bot(command_prefix='$', intents=intents)

# # Dan inilah cara Kamu mengganti nama file dari variabel!


# @bot.event
# async def on_ready():
#     print(f'We have logged in as {bot.user}')

# @bot.command()
# async def hello(ctx):
#     await ctx.send(f'Hi! I am a bot {bot.user}!')

# @bot.command()
# async def heh(ctx, count_heh = 5):
#     await ctx.send("he" * count_heh)

# @bot.command()
# async def mem(ctx):
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#                     picture = discord.File(f)
#     # with open('images/meme1.jpg', 'rb') as f:
#     #     # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
#     #     picture = discord.File(f)
#    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
#     await ctx.send(file=picture)


# bot.run("MTEwNjgwNTAxMDI5NTE3MzE3MA.Gt9E7v.MjiLCojrFKFXdY9-hlF6RfAcnYHrRr1NiY9__I")

import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def tambah(ctx , tambah1 , tambah2):
    await ctx.send(int(tambah1) + int(tambah2))

@bot.command()
async def perkalian(ctx , perkalian1 , perkalian2):
    await ctx.send(int(perkalian1) * int(perkalian2))

@bot.command()
async def pembagian(ctx , pembagian1 , pembagian2):
    await ctx.send(int(pembagian1) // int(pembagian2))
    


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    # with open('images/meme1.jpg', 'rb') as f:
    #     # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
    #     picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def hewan(ctx):
    img2_name = random.choice(os.listdir('image'))
    with open(f'image/{img2_name}', 'rb') as f:
                    picture = discord.File(f)
    # with open('images/meme1.jpg', 'rb') as f:
    #     # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
    #     picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

# buat ngasih gambar bebek
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# buat ngasih gambar anjing
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Setelah kita memanggil perintah bebek (dog), program akan memanggil fungsi get_dog_image_url'''
    
    image2_url = get_dog_image_url()
    await ctx.send(image2_url)


organik = ["daun","sayur","kulit pisang"]
anorganik = ["plastik","besi","kabel"]

@bot.command()
async def pilih(ctx, sampah):
    if sampah in organik:
        await ctx.send("Masukkan dalam sampah organik")
    elif sampah in anorganik:
        await ctx.send("Masukkan dalam sampah anorganik")




bot.run("MTEwNjgwNTAxMDI5NTE3MzE3MA.Gpygzb.eVjkyiBgc5pmUBfTLR2Y8buACTOnotFuYjO1cM")