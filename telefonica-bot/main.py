import json

import discord
from discord.ext import commands

# Settings dictionary
config = json.load(open('cfg.json'))

# Bot Object
bot = commands.Bot(config['prefix'])


@bot.event
async def on_ready():
    print(f'Online | {bot.user}')


@bot.event
async def on_message(message):
    channel_id = message.channel.id

    if channel_id == 964477202668331078:
        await message.delete()

    await bot.process_commands(message)


@bot.command(name='imRH')
async def configure_rh_role(ctx):
    channel_id = ctx.channel.id

    if channel_id == 964477202668331078:
        user = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='RH')

        await user.add_roles(role)

        channel_response = discord.utils.get(ctx.guild.channels, id=964500234556301363)

        await channel_response.send(f'O {user.roles[1]} {user.mention} entrou no servidor!')


@bot.command(name='imES')
async def configure_estagiario_role(ctx):
    channel_id = ctx.channel.id

    if channel_id == 964477202668331078:
        user = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='Estagiário')

        await user.add_roles(role)

        channel_response = discord.utils.get(ctx.guild.channels, id=964500234556301363)

        await channel_response.send(f'O {user.roles[1]} {user.mention} entrou no servidor!')


bot.run(config['token'])
