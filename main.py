import discord
import apiCall
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
discordKey = os.getenv("DISCORD_KEY")
prefix = os.getenv("COMMAND_PREFIX")
bot = commands.Bot(command_prefix=prefix)
    
@bot.command()
async def item(ctx, *, x):
    """Gets item information"""
    name = x
    res = apiCall.Items()
    for a in res["items"].values():
        lowerName = a["name"].lower()
        if name.lower() in lowerName:
            embed = discord.Embed()
            embed.set_author(name=a["name"], icon_url=a["image"])
            embed.add_field(name="Description", value=a["description"], inline=False)
            embed.add_field(name="Buy Price", value="${:,}".format(a["buy_price"]))
            embed.add_field(name="Sell Price", value="${:,}".format(a["sell_price"]))
            embed.add_field(name="Market Price", value="${:,}".format(a["market_value"]))
            await ctx.send(embed=embed)

@bot.command()
async def travel(ctx, *, x):
    """Gets Travel Item Info"""
    name = x
    res = apiCall.Travel()
    itm = apiCall.Items()
    for k in res["stocks"].keys():
        location = ""
        if k == "mex":
            location = "Mexico"
        elif k == "cay":
            location = "Cayman Islands"
        elif k == "can":
            location = "Canada"
        elif k == "haw":
            location = "Hawaii"
        elif k == "uni":
            location = "United Kingdon"
        elif k == "arg":
            location = "Argentina"
        elif k == "swi":
            location = "Switzerland"
        elif k == "jap":
            location = "Japan"
        elif k == "chi":
            location = "China"
        elif k == "uae":
            location = "UAE"
        elif k == "sou":
            location = "South Africa"

        for i in res["stocks"][k]['stocks']:
            if name.lower() in i["name"].lower():
                for t in itm["items"].values():
                    if i["name"] == t["name"]:
                        embed = discord.Embed()
                        embed.set_author(name=t["name"], icon_url=t["image"])
                        embed.add_field(name="Description", value=t["description"], inline=False)
                        embed.add_field(name="Buy Price", value="${:,}".format(t["buy_price"]))
                        embed.add_field(name="Sell Price", value="${:,}".format(t["sell_price"]))
                        embed.add_field(name="Market Price", value="${:,}".format(t["market_value"]))
                        embed.add_field(name="Current Quantity", value="{:,}".format(i["quantity"]))
                        embed.add_field(name="Location", value=location)
    await ctx.send(embed=embed)

bot.run(discordKey)