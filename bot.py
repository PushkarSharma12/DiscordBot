import discord
import random
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready!')

#@client.event
#async def on_member_join(member):
    #channel = client.get_channel(753546114086469692)
    #await channel.send(f'{member} has joined the server!')

#@client.event
#async def on_member_remove(member):
    #channel = client.get_channel(753546114086469692)
    #await channel.send(f'{member} has left the server!')
#@client.event
#async def on_typing(channel,user,when):
#    await channel.send(f'{user} is typing in {channel} at {when}')

@client.command(aliases=["8ball","Ball","LuckyBall"])
async def _8ball(ctx, *, question):
    responses = [ "It is certain.",
                "It is decidedly so.",
                " Without a doubt.",
                " Yes – definitely.",
                " You may rely on it.",
                " As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                " Better not tell you now.",
                "Cannot predict now.",
                " Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful.",
                ]
    try:
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    except MissingRequiredArgument:
        await ctx.send('Ah! You didnt write the question.')
    except:
        print("Something else went wrong")
    

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def dab(ctx):
    await ctx.send(f'o/')

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello! {ctx.message.author.mention}')

client.run('NzUzNjAxNTIwMjA4OTY5ODY4.X1okGw.1LelMvjOA8lhyNjnslOPItswzuk')