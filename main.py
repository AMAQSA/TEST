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
    elif message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')
    else:
        await message.channel.send("Tidak dapat memproses perintah ini, maaf")

client.run(settings["TOKEN"])
