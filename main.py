import json
import discord
import random
from discord.ext import commands
from discord.flags import Intents

with open("config.json") as configfile:
    configdata = json.load(configfile)

intents = Intents.all()

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print("Bot Ready")

@bot.event
async def on_message(msg):
    if msg.content.upper() == "SCATTER" and (msg.author.id == configdata['dev_id'] or msg.author.id in configdata['priv_ids']):
        voice_channels = msg.guild.voice_channels
        for channel in voice_channels:
            for member in channel.members:
                destination = voice_channels[random.randrange(0, len(voice_channels), 1)]
                await member.edit(voice_channel=destination)
    await bot.process_commands(msg)

@bot.command(name="ping")
async def hi(ctx):
    await ctx.reply("Pong!")

bot.run(configdata["token"])
