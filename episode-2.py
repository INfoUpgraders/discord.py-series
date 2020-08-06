import discord
from discord.ext import commands


client = commands.Bot(command_prefix=';')
client.remove_command('help')


@client.event
async def on_ready():
    activity = discord.Activity(name='YouTube!', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Ready")


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Help Command", 
    color=0x7289DA, timestamp=ctx.message.created_at)
    embed.add_field(name="Ping", value="`;ping` - returns `Pong!`", inline=False)
    embed.add_field(name="Website", value="[Click Here](https://infoupgraders.com/)", inline=True)
    embed.add_field(name="Support", value="https://discord.gg/rtddhcC", inline=True)
    embed.set_author(name=f"{ctx.author.display_name}", url="https://infoupgraders.com/", icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_image(url=client.user.avatar_url)
    await ctx.send(embed=embed)


client.run('TOKEN HERE')
