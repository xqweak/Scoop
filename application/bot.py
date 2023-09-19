from handlers import Url
from handlers import UrlList
from handlers import Host
from handlers import HostList
from discord.ext import commands
import discord



# Main function
if __name__ == "__main__":
    with open('token.txt', 'r') as fp:
        TOKEN = fp.read()
    bot.run(TOKEN)
