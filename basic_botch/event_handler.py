# Imports

# Events
#@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(basic_botch.prefix):
        await message.channel.send('YEEE!')
