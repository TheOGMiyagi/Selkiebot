from random import choice
import time

from discord.ext import commands
import yt


seal_image_urls = []
with open("images/seal_images.res") as a: seal_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in seal_image_urls: seal_image_urls.remove('')
lewdSeal = "https://imgur.com/NNVMNmt"

sloth_image_urls = []
with open("images/sloth_images.res") as a: sloth_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in sloth_image_urls: sloth_image_urls.remove('')

dog_image_urls = []
with open("images/dog_images.res") as a: dog_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in dog_image_urls: dog_image_urls.remove('')

possum_image_urls = []
with open("images/possum_images.res") as a: possum_image_urls = [b.strip() for b in a.read().split('\n')]
while '' in possum_image_urls: possum_image_urls.remove('')
birthdayPoss = "https://imgur.com/IWV9ICR"

currentvc = None
farming = False


class ImagesCog(commands.Cog):
    """Cog for handling commands that return images.
    """
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with."""
        self.bot = bot
    
    @commands.group(name='image',
        aliases=['images',
            'picture',
            'pictures',
            'animal_image',
            'animal_images',
            'animal_picture',
            'animal_pictures'])
    #@commands.guild_only()
    async def animal_images(self, ctx):
        _subcommands = ('Seal', 
            'Dog',
            'Possum',
            'Sloth',
            'Birthday',
            'Lewd',
            'Dranz',
            'Yiff')
        await ctx.message.channel.send(f"Sub-Commands: {'\n> '.join(_subcommands)}")
    
    @animal_images.command(name='dog', aliases=['Dog', 'dogs', 'Dogs'])
    #@commands.guild_only()
    async def dog_images(self, ctx):
        """Sends dog pictures to the context channel.
        """
        _image = choice(dog_image_urls)
        await ctx.message.channel.send(_image)
    @animal_images.command(name='possum', aliases=['Possum', 'possums', 'Possums'])
    #@commands.guild_only()
    async def possum_images(self, ctx):
        """Sends possum pictures to the context channel.
        """
        _image = choice(possum_image_urls)
        await ctx.message.channel.send(_image)
    @animal_images.command(name='seal', aliases=['Seal', 'seals', 'Seals'])
    #@commands.guild_only()
    async def seal_images(self, ctx):
        """Sends seal pictures to the context channel.
        """
        _image = choice(seal_image_urls)
        await ctx.message.channel.send(_image)
    @animal_images.command(name='sloth', aliases=['Sloth', 'sloths', 'Sloths'])
    #@commands.guild_only()
    async def sloth_images(self, ctx):
        """Sends sloth pictures to the context channel.
        """
        _image = choice(sloth_image_urls)
        await ctx.message.channel.send(_image)

class MiscCommandsCog(commands.Cog):
    """Cog for non-image commands that don't deserve their own respective cog file.
    """
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with."""
        self.bot = bot
    
    @commands.command(name='birthday', aliases=['Birthday', 'BIRTHDAY'])
    #@commands.guild_only()
    async def birthday_possum(self, ctx):
        _image = birthdayPoss
        await ctx.message.channel.send(_image)
    
    @commands.command(name='lewd', aliases=['Lewd', 'LEWD'])
    #@commands.guild_only()
    async def lewd_seal(self, ctx):
        _image = lewdSeal
        await ctx.message.channel.send(_image)
    
    @commands.command(name='dranz', aliases=['Dranz', 'DRANZ'])
    #@commands.guild_only()
    async def dranz(self, ctx):
        _msg = 'Yeah, dude.'.format(ctx.message)
        await ctx.message.channel.send(_msg)
    
    @commands.command(name='yiff', aliases=['Yiff', 'YIFF'])
    #@commands.guild_only()
    async def yiff(self, ctx):
        _msg = 'yeef'.format(ctx.message)
        await ctx.message.channel.send(_msg)


def setup(bot):
    """Adds The Cog To The Client."""
    bot.add_cog(ImagesCog(bot))
    bot.add_cog(MiscCommandsCog(bot))
