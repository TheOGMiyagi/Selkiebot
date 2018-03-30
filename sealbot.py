import discord
from random import choice
import yt
import time

client = discord.Client()

with open("security.res") as a: securitytmp = [b.strip() for b in a.read().split('\n')]
security_settings = {}
for a in securitytmp:
    if ':' in a:
        b,c = a.split(':')
        security_settings[b] = c

seal_image_urls = []
with open("seal_images.res") as a: seal_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in seal_image_urls: seal_image_urls.remove('')
lewdSeal = "https://imgur.com/NNVMNmt"

sloth_image_urls = []
with open("sloth_images.res") as a: sloth_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in sloth_image_urls: sloth_image_urls.remove('')

dog_image_urls = []
with open("dog_images.res") as a: dog_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in dog_image_urls: dog_image_urls.remove('')

possum_image_urls = []
with open("possum_images.res") as a: possum_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in possum_image_urls: possum_image_urls.remove('')
birthdayPoss = "https://imgur.com/IWV9ICR"

currentvc = None
farming = False

@client.event
async def on_message(message):
    global currentvc
    global farming
    # Per the discord.py docs this is to not have the bot respond to itself
    if message.author == client.user:
        return
    #Help
    elif message.content.startswith('!help'):
        msg = 'commands: seal, dog, possum, sloth, birthday, lewd, dranz, yiff.'.format(message)
        await client.send_message(message.channel, msg)
    #SEAL IMAGES
    elif message.content.startswith('!seal'):
        location = choice(seal_image_urls)
        await client.send_message(message.channel, location)
    #SEAL IMAGES
    elif message.content.startswith('!dog') or message.content.startswith('!pup'):
        location = choice(dog_image_urls)
        await client.send_message(message.channel, location)
    #SLOTH IMAGES
    elif message.content.startswith('!sloth'):
        location = choice(sloth_image_urls)
        await client.send_message(message.channel, location)
    #POSSUM IMAGES
    elif message.content.startswith('!possum') or message.content.startswith('!opossum'):
        location = choice(possum_image_urls)
        await client.send_message(message.channel, location)
    #Post birthday possum
    elif message.content.startswith('!birthday'):
        location = birthdayPoss
        await client.send_message(message.channel,location)
    #Post that one seal gif
    elif message.content.startswith('!lewd') or message.content.startswith('!nsfw'):
        location = lewdSeal
        await client.send_message(message.channel,location)
    #you know what this does
    elif message.content.startswith('!dranz'):
        msg = 'Yeah, dude.'.format(message)
        await client.send_message(message.channel, msg)
    #YIFFYIFFYIFFYIFFYIFFYIFFYIFF
    elif message.content.startswith('!yiff'):
        msg = 'yeef'.format(message)
        await client.send_message(message.channel, msg)
    #elif message.content.startswith('!yt'):
        #url = message.content.split()[1]
        #chan = message.author.voice_channel
        #if currentvc is not None: await currentvc.disconnect()
        #ch = await client.join_voice_channel(chan)
        #player = await ch.create_ytdl_player(url)
        #player.start()
        #currentvc = ch
    #elif message.content.startswith('!play'):
        #url = yt.yt_search(message.content[6:])[0]
        #chan = message.author.voice_channel
        #if currentvc is not None: await currentvc.disconnect()
        #ch = await client.join_voice_channel(chan)
        #player = await ch.create_ytdl_player(url)
        #player.start()
        #currentvc = ch
    #elif message.content.startswith('!stop'):
        #await currentvc.disconnect()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(security_settings["token"])
