from handlers import Url
from handlers import UrlList
from handlers import Host
from handlers import HostList
from discord.ext import commands
import discord

import discord
from discord.ext import commands

class Scoop(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.typing = False
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    @commands.command()
    async def options(self, ctx):
        # Create a message with clickable options
        print("hola")



def main():
    with open('token.txt' , 'r') as fp:
        TOKEN = fp.read()
    bot = Scoop(command_prefix='!')
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

