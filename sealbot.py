"""SelkieBot by Pantywitch

Required 3RD-Party Libraries:
    - discord
    - yt
"""
import os

import discord
from discord.ext import commands


PREFIXES = ["!",
    "sel!",
    "Sel!"
    "selkie!",
    "Selkie!"]
#* Instantiates An Instance Of The Bot() Class.
bot = commands.Bot(command_prefix=PREFIXES,
	intents=discord.Intents.all())

with open("images/security.res") as a: securitytmp = [b.strip() for b in a.read().split('\n')]
security_settings = {}
for a in securitytmp:
    if ':' in a:
        b,c = a.split(':')
        security_settings[b] = c


#* Loads cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Cog: {filename[:-3].title().replace("_", "")} loaded.')
    elif filename.endswith('_cogs') or filename == "__pycache__":
        continue
    else:
        print(f'Cog: Unable to load {filename[:-3]}')


#* Module Code
def main():
    """Main Method
    """
    bot.run(security_settings["token"])


#? Driver Code
if __name__ == "__main__":
    main()
