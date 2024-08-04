import config
from discord.ext import commands
import httpx

url = 'http://localhost:8000/postmessage/'
client = commands.Bot(command_prefix='!', self_bot=True)

@client.event
async def on_ready():
    print(f'{client.user} in the house!')

@client.event
async def on_message(message):
    target_channel_id = config.joffs_channel 
    if message.channel.id == target_channel_id:
        discord_message = message.content 
        print(discord_message)

        # Send the raw string directly to our server
        async with httpx.AsyncClient() as client:
            await client.post(url, content=discord_message)

token = config.discord_token
client.run(token)