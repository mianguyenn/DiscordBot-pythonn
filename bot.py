# Import Discord Package
import discord

# Client
client = discord.Client()

@client.event
async def on_ready():
# DO STUFF
    general_channel = client.get_channel(524220488000471040)

    await general_channel.send('Poyo!')

        
@client.event
async def on_message(message):
    
    if message.content == 'its okay':
         general_channel = client.get_channel(524220488000471040)
         await general_channel.send('to be gayy')


# run the client
client.run('ODg1NzI0NDcyOTExNDY2NTQ3.YTrNMg.XSKwXB1fL5PSdbnBnZIMQ11YJAY')