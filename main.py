import json
import discord
from discord.ext import commands
from discord.flags import Intents

with open("config.json") as configfile:
    configdata = json.load(configfile)

intents = Intents.all()

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_message(msg):
    if msg.content == "scatter":
        await msg.channel.send('ok')
    await bot.process_commands(msg)


@bot.command(name="hi")
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.send(f"Hello {name}!")

@bot.command(name="ping")
async def hi(ctx):
    await ctx.reply("Pong!")

bot.run(configdata["token"])
