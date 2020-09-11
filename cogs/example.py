import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
import random

class Example(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready!')
    
    @commands.command(aliases=["8ball","Ball","LuckyBall"])
    async def _8ball(self,ctx, *, question):
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
    @commands.command()      
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')
    @commands.command()
    async def dab(self,ctx):
        await ctx.send(f'o/')
    @commands.command()
    async def hello(self,ctx):
        await ctx.send(f'Hello! {ctx.message.author.mention}')
    @commands.command()
    async def kick(self,ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, id=753530652279701546)
        if role in ctx.message.author.roles:
            await member.kick(reason = reason)
            await ctx.send(f"{member.name} Just got Kicked for {reason}")
        else:
            await ctx.send("<access denied because of improper role message>")

    @commands.command()
    async def ban(self,ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, id=753530652279701546)
        if role in ctx.message.author.roles:
            await member.ban(reason = reason)
            await ctx.send(f"{member.name} Just got Banned for {reason}")
        else:
            await ctx.send("Access denied because of improper role message!")
    @commands.command()
    async def clear(self, ctx, number=5):
        role = discord.utils.get(ctx.guild.roles, id=753530652279701546)
        if role in ctx.message.author.roles:
            await ctx.channel.purge(limit=number)
        else:
            await ctx.send("Access denied because of improper role message!")

    @commands.command()
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        role = discord.utils.get(ctx.guild.roles, id=753530652279701546)
        if role in ctx.message.author.roles:
            for banned in banned_users:
                user = banned.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    message = "You just got Unbanned from ClapzyServer"
                    await ctx.send(f'{user.mention} Just got Unbanned')
                    return
                else:
                    await ctx.send(f'{member} is not Banned')
        else:
            await ctx.send("Access denied because of improper role message!")

def setup(client):
    client.add_cog(Example(client))