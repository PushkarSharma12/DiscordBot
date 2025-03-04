import discord
from discord.ext import commands,tasks
from discord.ext.commands.errors import MissingRequiredArgument
import random

class Example(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        
        # server = self.client.get_guild(754942615501144114)
        # members = server.members
        # for member in members:
        #     try:
        #         pushkar = self.client.get_user(531345753994559488)
        #         if member != pushkar:
        #             await member.kick(reason = "nothing")
        #             print (f"Kicked {member.name}")
        #         else :
        #             print(f"Donot Kick {pushkar.name}")
        #     except Exception:
        #         print (f"Couldn't Kick {member.name}")
        await self.client.change_presence(status = discord.Status.idle, activity=discord.Game('Amoung Us'))
        
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
        except Exception as error:
            await ctx.send('Ah! You didnt write the question.')
        except Exception as e:
            print("Something else went wrong")
    @commands.command()      
    async def ping(self,ctx):
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')
    @commands.command()
    async def dab(self,ctx):
        await ctx.send(f'o/')
    @commands.command()
    async def hello(self,ctx):
        answers = [f"Hello! {ctx.message.author.mention}",
                    "Hello! You stupid child.",
                    "Shut up moron!",
                    "I'll beat you up!"]
        await ctx.send(f'{random.choice(answers)}')
    @commands.command()
    @commands.has_any_role('Moderator', 'Clapzy')
    async def kick(self,ctx, member : discord.Member, *, reason=None):
            try:
                await member.kick(reason = reason)
                await ctx.send(f'{member.name} has been Kicked for {reason}.')
            except Exception as error:
                await ctx.send("You dont have appropriate role!")
    @commands.command()
    async def join(self,ctx):
        await ctx.send(f'JOIN HEIST')
    @commands.command()
    async def hi(self,ctx):
        await ctx.send(f'Hi @here !')

    @commands.command()
    async def kill(self,ctx,*member : discord.Member):
        responses = ["Squished to death.",
                    " Crampled to death",
                    " Without a doubt Killed badly.",
                    " Soft boned and cracked to death.",
                    " killed by everyone.",
                    ]
        if(member):
            await ctx.send(f'{(member[0])} was {random.choice(responses)}')

        else:
            await ctx.send(f'{ctx.message.author} was {random.choice(responses)}')

    @commands.command()
    @commands.has_any_role('Moderator', 'Clapzy')
    async def ban(self,ctx, member : discord.Member, *, reason=None):
        try:
            await member.ban(reason = reason)
            await ctx.send(f"{member.name} Just got Banned for {reason}")
        except Exception as error:
            await ctx.send(error)
    @commands.command()
    @commands.has_any_role('Moderator', 'Clapzy')
    async def clear(self, ctx, number=5):
        
        await ctx.channel.purge(limit=number)

    @commands.command()
    @commands.has_any_role('Moderator', 'Clapzy')
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for banned in banned_users:
            user = banned.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                message = "You just got Unbanned from ClapzyServer"
                await ctx.send(f'{user.mention} Just got Unbanned')
                return
            else:
                await ctx.send(f'{member} is not Banned')
        

def setup(client):
    client.add_cog(Example(client))