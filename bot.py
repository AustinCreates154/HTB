import discord
from discord.ext import commands

htb = commands.Bot(command_prefix='h!')

@htb.event
async def on_ready():
    print('I am using')
    print(bot.user.name)
    print('As my body. And mu ID is')
    print(bot.user.id)
    print('=============')
    
@htb.command(pass_context=True)
@check.has_permission(kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.send('{} Has been kicked from HypeServer. Bye-Bye!'.format(discord.Member))
    await ctx.guild.kick(user)
        
@htb.command(pass_context=True)
@check.has_permission(ban_members=True)
async def ban(ctx, user: discord.Member)
    await ctx.send('{} Has been permently banned from HypeServer!! :hammer:'.format(discord.Member))
    await ctx.guild.ban(user)
