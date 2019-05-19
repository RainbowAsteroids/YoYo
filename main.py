#!/usr/bin/env python3.6
import discord
from os import system as cmd
import re

client = discord.Client() # Discord client

#Please place your own IDs here!
repo_url = "https://github.com/RainbowAsteroids/YoYo"
owner_id = None
beta_token = ""
main_token = ""
token = main_token # bot token
muted = []
payload = []
unlocked = []
endings = ('yo', 'yo!', 'yo.', 'yo?', 'yo;', 'yo:')
helptext = """```
yo       : says yo back+1
f        : says f back
!yo mute : mutes the channel from posting yo's *
!yo payload : Lets YoYo yo-yo off of itself *
!yo help : this
!yo lock : locks/unlocks certain commands behind the "manage messages" permission *
* = requires manage messages permission if server is locked```
"""
r = re.compile("(?i)yo |yo!|yo\.|yo\?|yo:|yo;") #The regex for the program
async def permission(message, permission='manage_messages'):
    if type(message.channel) == discord.DMChannel or message.channel.id in unlocked or eval(f"message.channel.permissions_for(message.author).{permission}"):
        return True
    else:
        await message.channel.send(f'<@{message.author.id}> Hmm... seems like you don\'t have the "manage messages" permission, so I can\'t let you do that.')
        return False

@client.event
async def on_ready():
    global beta
    print(f"Logged in as {client.user.name}")
    beta = token == beta_token
    if beta: print('[INFO]: Yoyo is running in beta mode. Debug printouts enabled.')


@client.event
async def on_message(message):
    if message.author == client.user and not message.channel.id in payload: return
    
    if message.content.startswith('!yo'):
        msg = message.content[4:]
        if beta: print(f"[INFO]: msg = {msg}")
        
        if msg.startswith('mute'):
            if await permission(message):
                if not message.channel.id in muted:
                    muted.append(message.channel.id)
                    await message.channel.send('bye have a beautiful time, please say `!yo mute` to let me annoy you again')
                else:
                    muted.pop(muted.index(message.channel.id))
                    await message.channel.send("I sexually Identify as an Yo-yo. Ever since I was a boy I dreamed of flying up and down endlessly. People say to me that a person being a Yo-yo is impossible and I'm fucking retarded but I don't care, I'm beautiful. I'm having a plastic surgeon install a circular plastic body and white string. From now on I want you guys to call me \"Yo-yo\" and respect my right to zip around the room back and forth. If you can't accept me you're a yoaphobe and need to check your toy privilege. Thank you for being so understanding.")
        
        elif msg.startswith('help'):
            await message.channel.send(helptext)
        
        elif msg.startswith('close') or msg.startswith('kill'):
            if message.author.id == owner_id: 
                await message.channel.send('Sorry guys. It\'s my bedtime and I can\'t stay on much longer.')
                await client.close()
        
        elif msg.startswith('payload'):
            if await permission(message):
                if not message.channel.id in payload:
                    payload.append(message.channel.id)
                    await message.channel.send('Boy are you in for a hell of a time.')
                else:
                    payload.pop(payload.index(message.channel.id))
                    await message.channel.send('I don\'t blame you.')
        
        elif msg.startswith('lock'):
            if await permission(message):
                if not message.channel.id in unlocked:
                    await message.channel.send('Permission lock has been beaten by it\'s arch rival: bolt cutters.')
                    unlocked.append(message.channel.id)
                else:
                    unlocked.pop(unlocked.index(message.channel.id))
                    await message.channel.send('Guys it\'s **over**. The mods are shutting it down.')
        elif msg.startswith('git'):
            await message.channel.send(f'Bot created by Rainbow Asteroids: {repo_url}')
    
    elif 'yo ' in message.content.lower():
        if message.channel.id in muted: return
        yos = len(r.split(message.content))
        if message.content.lower().endswith('yo'): yos += 1
        await message.channel.send(('yo '*yos)[:-1]+'!')

    elif message.content.lower() in endings:
        await message.channel.send('yo yo!')
    
    elif endswith(message.content.lower()):
        await message.channel.send('yo yo!')

    elif message.content.lower() == 'f':
        await message.channel.send('```css\nF```')

client.run(token)
cmd('clear')
