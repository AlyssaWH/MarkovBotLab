
import os
import discord
import markov

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send(markov.make_text(markov.chains))
        #await message.channel.send(markov.make_text("Im a big random string of text"))
#client.run('your token here')
client.run(os.environ['DISCORD_TOKEN'])

