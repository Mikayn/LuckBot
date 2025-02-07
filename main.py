import nextcord
from dotenv import load_dotenv
import os
from random import randint
import re

load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True
client = nextcord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"Logging in as {client.user}")

@client.event
async def on_message(message):
    msg = message.content 

    if message.author == client.user: 
        return
    
    if msg.startswith("?luck"):

        if matches := re.match(r"^(\?luck)(\d+) (\d+)$", msg):
            maxNum = int(matches.group(2))
            userChoice = int(matches.group(3))

            if maxNum < 2:
                await message.channel.send("Your choice cannot be guarenteed, 0 or less than 0! ")
            
            if maxNum < userChoice:
                await message.channel.send("Your choice is out of range! ")

            else:
                botChoice = randint(1, maxNum)
                if botChoice == userChoice:
                    await message.channel.send("Congratulations! You are extremely lucky. :D")
                else:
                    await message.channel.send("Unfortunate. :( ")

        else:
            await message.channel.send("The format is '?luckMAXNUM CHOICE' (For example: ?luck100 10)" )


client.run(os.getenv("TOKEN"))