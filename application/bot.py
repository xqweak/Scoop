import asyncio
from handlers import Url
from handlers import UrlList
from handlers import Host
from handlers import HostList
from discord.ext import commands
import discord

def list_to_markdown(args_list: list):
    """Format a domain or url list to markdown for printing it."""
    texts = []
    for cont, i in enumerate(args_list):
        text = f"{cont}. {i}"
        texts.append(text)
    formatted = "\n".join(texts)
    return formatted

"""Define the bot with default intents"""
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    """On ready function runs ones the bot is logged in"""
    print(f'{bot.user} is running and ready to hack')

# Url Methods:

@bot.command()
async def scan_httpx(ctx, *args):
    """Scan with httpx for a UrlList using UrlList scan_nuclei method"""
    args = list(args)
    url_txt ="\n".join(args)
    url_list = UrlList(url_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Scanning with httpx: \n {pretty_advice} \n## Result: \n\n')
    outs = url_list.scan_httpx()
    results = [i.output for i in outs]
    # Need to return as list because discord ban large texts
    for i in results:
        if(i != ""):
            await ctx.send(i)
    await ctx.send("Done!")


@bot.command()
async def scan_katana(ctx, *args):
    """Crawl urls for a UrlList using UrlList's scan_katana method"""
    args = list(args)
    url_txt ="\n".join(args)
    url_list = UrlList(url_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Crawling with katana: \n {pretty_advice} \n## Result: \n\n')
    out = url_list.scan_katana()
    result = out.to_txt()
    # Need to return as list because discord ban large texts
    result_as_list = [i for i in result.split("\n") if i != ""]
    for i in result_as_list:
        await ctx.send(i)
    await ctx.send("Done!")

@bot.command()
async def scan_wayback(ctx, *args):
    """Search for old urls for a UrlList using UrlList's scan_wayback method"""
    args = list(args)
    url_txt ="\n".join(args)
    url_list = UrlList(url_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Searching for old urls in waybackmachines: \n {pretty_advice} \n## Result: \n\n')
    out = url_list.scan_waybackurls()
    result = out.to_txt()
    # Need to return as list because discord ban large texts
    result_as_list = [i for i in result.split("\n") if i != ""]
    for i in result_as_list:
        await ctx.send(i)
    await ctx.send("Done!")

@bot.command()
async def scan_dirsearch(ctx, *args):
    """Bruteforce urls for a UrlList using UrlList's scan_dirsearch method"""
    args = list(args)
    url_txt ="\n".join(args)
    url_list = UrlList(url_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Bruteforcing urls with dirsearch for: \n {pretty_advice} \n## Result: \n\n')
    out = url_list.scan_dirsearch()
    result = out.to_txt()
    # Need to return as list because discord ban large texts
    result_as_list = [i for i in result.split("\n") if i != ""]
    for i in result_as_list:
        await ctx.send(i)
    await ctx.send("Done!")

# Host methods:

@bot.command()
async def scan_subfinder(ctx, *args):
    """Scan subdomains for a HostList using HostList scan_subfinder method"""
    args = list(args)
    host_txt ="\n".join(args)
    host_list = HostList(host_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'finding subdomains for \n {pretty_advice} \n## Result: \n\n')
    out = host_list.scan_subfinder()
    result = out.to_txt()
    # Need to return as list because discord ban large texts
    result_as_list = [i for i in result.split("\n") if i != ""]
    for i in result_as_list:
        await ctx.send(i)
    await ctx.send("Done!")

@bot.command()
async def scan_naabu(ctx, *args):
    """Scan subdomains for a HostList using HostList scan_naabu method"""
    args = list(args)
    host_txt ="\n".join(args)
    host_list = HostList(host_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Scanning with naabu \n {pretty_advice} \n## Result: \n\n')
    out = host_list.scan_naabu()
    result = out.to_txt()
    # Need to return as list because discord ban large texts
    result_as_list = [i for i in result.split("\n") if i != ""]
    for i in result_as_list:
        await ctx.send(i)
    await ctx.send("Done!")


@bot.command()
async def scan_nuclei_full(ctx, *args):
    """
    Scan subdomains for a HostList or  UrlList using HostList scan_nuclei
    method and return EVERY log that nuclei throws.
    """
    args = list(args)
    host_txt ="\n".join(args)
    host_list = HostList(host_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Scanning with nuclei \n {pretty_advice} \n## Result: \n\n')
    outs = host_list.scan_nuclei()
    results = [i.output for i in outs]
    # Need to return as list because discord ban large texts
    for i in results:
        for j in i:
            if(j != ""):
                await ctx.send(j)
    await ctx.send(j)
    
@bot.command()
async def scan_nuclei(ctx, *args):
    """
    Scan subdomains for a HostList or  UrlList using HostList scan_nuclei
    method and return ONLY vulnerabilities. 
    """
    args = list(args)
    host_txt ="\n".join(args)
    host_list = HostList(host_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Scanning with nuclei \n {pretty_advice} \n## Result: \n\n')
    outs = host_list.scan_nuclei()
    results = [i.output for i in outs]
    # Need to return as list because discord ban large texts
    for i in results:
        for j in i:
            if(j != "" and ("[info]" not in j)):
                await ctx.send(j)
    await ctx.send(j)

@bot.command()
async def scan_httprobe(ctx, *args):
    """Scan subdomains for a HostList using HostList scan_httprobe method"""
    args = list(args)
    host_txt ="\n".join(args)
    host_list = HostList(host_txt)
    pretty_advice = list_to_markdown(args)
    await ctx.send(f'Scanning with httprobe \n {pretty_advice} \n## Result: \n\n')
    out = host_list.scan_httprobe()
    result = out.to_txt()
    # Need to return as list because discord ban large texts
    result_as_list = [i for i in result.split("\n") if i != ""]
    for i in result_as_list:
        await ctx.send(i)
    await ctx.send("Done!")


# Main function
if __name__ == "__main__":
    with open('token.txt', 'r') as fp:
        TOKEN = fp.read()
    bot.run(TOKEN)
