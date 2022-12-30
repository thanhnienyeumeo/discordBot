import discord
import os

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
client.run('MTA1NzM1MTg3OTA3NzY3MTA1Mw.GtR1TP.uvthnTotYS3i-vEQt3w7J_VnfaeS9uWjqaGhSk')