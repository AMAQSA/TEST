import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)




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
    await ctx.send(file=picture)

@bot.command()
async def hewan(ctx):
    img2_name = random.choice(os.listdir('image'))
    with open(f'image/{img2_name}', 'rb') as f:
                    picture = discord.File(f)
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


organik = ["daun","sayur","kulit", "pisang"]
anorganik = ["plastik","besi","kabel"]

@bot.command()
async def pilih(ctx, sampah):
    if sampah in organik:
        await ctx.send("Masukkan dalam sampah organik")
    elif sampah in anorganik:
        await ctx.send("Masukkan dalam sampah anorganik")

@bot.command()
async def tolong(ctx):
    await ctx.send("pengguna bisa memasukkan beberapa perintah yaitu:\n1.help\n2.hello\n3.heh\n4.tambah contoh (tambah 10 23)\n5.perkalian contoh(perkalian 4 10)\n6.pembagian contoh(pembagian 10 2)\n7.mem\n8.hewan\n9.duck\n10dog\n11.memberi tahu pengguna tempat sampah apa yang cocok dengan barang tersebut contoh(pilih plastik)bot akan menjawab.kata yang bisa di gunakan yaitu daun,sayur,kulit,pisang,plastik,besi,kabel")


bot.run("MASUKKAN TOKEN MU DISINI!")
