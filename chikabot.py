import discord
import random
import os
from discord.ext import commands
from discord.ext import tasks

client = commands.Bot(command_prefix ='!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Minecraft'))
    print('Bot ready.')

@client.command()
async def test(ctx):
    await ctx.send(f'Ok')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')



client.run('NzUwMTgwMTAxNDU0NTYxMzEx.X02xqQ.C5uhK_8wmULk3bg2sIn6ejyRszc')
