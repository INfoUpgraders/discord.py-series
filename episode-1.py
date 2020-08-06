import discord
from discord.ext import commands


client = commands.Bot(command_prefix=';')


@client.event
async def on_ready():
    activity = discord.Activity(name='YouTube!', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Ready")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


client.run('TOKEN HERE')
