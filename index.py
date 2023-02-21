import discord

## This is the config file, you can delete this if you want.

import json

with open('./config/config.json') as f:
    config = json.load(f)
    token = config['token']

###########################################################

class client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower().startswith('!ping'):
            await message.reply('Pong!')


intents = discord.Intents.all()
intents.message_content = True

client = client(intents=intents)
client.run(token)
