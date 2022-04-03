import time

from discord.ext import commands
import yt


class YTCog(commands.Cog):
    """Cog for commands that utilize the 'yt' module.
    """
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with."""
        self.bot = bot
    
    @commands.group(name='yt', aliases='YT')
    @commands.guild_only()
    async def yt(self, ctx, url):
        global currentvc
        chan = ctx.message.author.voice_channel
        if currentvc is not None:
            await currentvc.disconnect()
        ch = await self.bot.join_voice_channel(chan)
        player = await ch.create_ytdl_player(url)
        player.start()
        currentvc = ch
    @yt.command(name='play', aliases=['Play', 'PLAY'])
    @commands.guild_only()
    async def yt_play(self, ctx, url):
        global currentvc
        chan = ctx.message.author.voice_channel
        if currentvc is not None: await currentvc.disconnect()
        ch = await self.bot.join_voice_channel(chan)
        player = await ch.create_ytdl_player(url)
        player.start()
        currentvc = ch
    @yt.command(name='stop', aliases=['Stop', 'STOP'])
    @commands.guild_only()
    async def yt(self, ctx):
        global currentvc
        await currentvc.disconnect()


def setup(bot):
    """Adds The Cog To The Client.
    """
    bot.add_cog(YTCog(bot))
