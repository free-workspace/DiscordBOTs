import json

import discord
from discord.ext import commands


config = json.load(open('config.json'))


bot = commands.Bot(command_prefix=config['default_prefix'])


@bot.event
async def on_ready():
    print(f'ONLINE | {bot.user}')


@bot.command(name='config')
async def set_configurations(ctx):
    pass


@bot.command(name='server')
async def minecraft_server(ctx, *args: str):
    try:
        event = args[0].lower()
    except IndexError:
        await ctx.send('Comando inválido.\nTente: $server <start/stop/consol>')
    else:
        if event == 'start':
            pass
        elif event == 'stop':
            pass
        elif event == 'consol':
            pass
        else:
            await ctx.send('Comando inválido.\nTente: $server <start/stop/consol>')


bot.run(config['token'])
