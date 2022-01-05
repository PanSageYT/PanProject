#{}devtoolkit - Toolkit for Developers.
import glob
import json
import os

import discord
from discord.ext import commands

from discord_components import Button, ButtonStyle

import utils

config = {}
with open(f"config.json", encoding='utf8') as data:
    config = json.load(data)

#botClient = commands.Bot(command_prefix = config['prefix'])

def GetFiles():
    file = []
    for x in glob.glob("dev/*.py"):
        file.append(x)
    return file

async def Cmd(message):
    try:
        if(not(utils.is_owner_of_bot(message.author.id))):
            return False

        embedVar = discord.Embed(title="Dev Toolkit", description="for Pan-Project Bot.", color=0x00ffff)
        ar = [[]]
        for x in GetFiles():
            with open(x, "r") as f:
                t = f.readline().replace("#", "")
                t = t.replace("{HASH}", "#")
                embedVar.add_field(name=t.split("-")[0], value=t.split("-")[1], inline=False)
                ar[0].append(Button(style=ButtonStyle.blue, label=t.split("-")[0], custom_id=t.split("-")[0]))
        await message.channel.send(embed=embedVar, components=ar)

        #interaction = await botClient.wait_for("button_click", check=lambda i: i.component.label == "Error Check")
        #await interaction.send(content="Here you go!", embed=errorcheck.ReturnCmd())

    except Exception as e:
        await utils.save_error(str(message.content), os.path.basename(__file__), e)
        await message.channel.send("Error. I saved error in my error database, my creator will check out.")



