import discord
import random
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, MissingRole
import os
from discord.utils import get
from discord.ext.commands.core import check
allowed_roles = ["753530652279701546","753532082743017472"]

client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx, extension):
    role = discord.utils.get(ctx.guild.roles, id=753530652279701546)
    if role in ctx.message.author.roles:
        client.load_extension(f'cogs.{extension}')
        await ctx.send("loaded")

@client.command()
async def unload(ctx, extension):
    role = discord.utils.get(ctx.guild.roles, id=753530652279701546)
    if role in ctx.message.author.roles:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send("unloaded")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
client.run('NzUzNjAxNTIwMjA4OTY5ODY4.X1okGw.1LelMvjOA8lhyNjnslOPItswzuk')