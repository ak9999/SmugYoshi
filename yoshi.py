#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import re
import asyncio


# Create bot
bot = commands.Bot(command_prefix='?', description="Very smug community management.")
badwords = set()  # Set of words you may not like, no duplicates.


try:
    auth_token = os.environ['DISCORD_TOKEN']
except:
    exit('Exiting: DISCORD_TOKEN not defined')

# Get bad words from file?
try:
    badwordslist = open('badwords.txt', 'r')
    badwords = {words.strip('\n') for words in list(badwordslist)}
except:
    print('Could not get list of bad words.')


# Define client event functions.
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')


@bot.command(description='For banning words.')
async def blacklist(*words : str):
    '''Adds a word to the badwords list.'''
    global badwords
    for word in words:
        badwords.add(word.lower())


@bot.command(description='Whispers current bad word set to user.')
async def print_blacklist():
    '''Prints out blacklist.'''
    global badwords
    await bot.whisper(f'Banned words list: {str(badwords)}')


@bot.command(description="Echoes what the user said.")
async def echo(*, message: str):
    await bot.say(message)


@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    '''Bot says when the user joined the server.'''
    if member is None:
        member = ctx.message.author
    await bot.say(f'{member} joined at {member.joined_at}')


@bot.listen('on_message')
async def del_badwords(message):
    if set(re.split('[\'\"\[\]{}()\s]', message.content.lower())) & badwords:
        await bot.delete_message(message)


bot.run(auth_token)  # Run needs to be passed a bot token in string form.
