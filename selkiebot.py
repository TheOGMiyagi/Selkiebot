import discord
from random import choice

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

@client.event
async def on_message(message):
    # Per the discord.py docs this is to not have the bot respond to itself
    if message.author == client.user:
        return
    #If the bot sees the command !yo we will respond with our msg string
    elif message.content.startswith('!yo'):
        msg = 'Yo {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #SEAL IMAGES
    elif message.content.startswith('!seal'):
        location = choice(seal_image_urls)
        await client.send_message(message.channel, location)
    #Post that one seal gi
    elif message.content.startswith('!lewd') or message.content.startswith('!nsfw'):
        location = lewdSeal
        await client.send_message(message.channel,location)
    #say "yeah, dude" whenever someone types !8ball
    elif message.content.startswith('!8ball'):
        msg = 'Yeah, dude.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!dranz'):
        msg = 'Yeah, dude.'.format(message)
        await client.send_message(message.channel, msg)
    #YIFFYIFFYIFFYIFFYIFFYIFFYIFF
    elif message.content.startswith('!yiff'):
        msg = 'yeef'.format(message)
        await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(security_settings["token"])