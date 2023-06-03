
from settings import settings
import discord
# import * - adalah cara cepat untuk mengimpor semua file di perpustakaan
from bot_logic import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan memindahkan hak istimewa
client = discord.Client(intents=intents)


# Setelah bot siap, ia akan mencetak namanya!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Saat bot menerima pesan, bot akan mengirimkan pesan di saluran yang sama!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Saya! Saya bot!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emoji1'):
        await message.channel.send('-_-') 
    elif message.content.startswith('$kamusiapa?'):
        await message.channel.send('Saya bot')
    elif message.content.startswith('$help'):
        await message.channel.send('kamu bisa memerintahkan dalam beberapa macam perintah \nmisalnya : \n 1.$hello \n 2.$smile \n 3.$coin \n 4.$pass \n 5.$emoji1 \n 6.$kamusiapa? \n 7.$help \n 8.$rank')
    elif message.content.startswith('$rank'):
        await message.channel.send('grandmaster ml , ff heroic')
    


client.run(settings["TOKEN"])
