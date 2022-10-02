import discord


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
	print("Le bot Vicente est prêt.")

@client.event
async def on_message(message):
	if message.content.lower() == "ping":
		await message.channel.send("pong")
		await message.channel.send("pong")

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
"""
@client.event
async def on_message(message):

	if message.content.startswith("!hot"):
		nombre = int(message.content.split()[1])
		await message.channel.send(f"{random.randint(1,nombre)}")"""

@client.event
async def on_member_join(member):
	commandes_channel: discord.TextChannel = client.get_channel(932009769844244510)
	await commandes_channel.send(content=f"Bienvenida sur le serveur {member.display_name} !") 

client.run("OTI1NTQ1NTQ4OTEwNTYzNDIw.Ycurdg.0TX3NA5O1kTavxGRNA3j7Zu16Cw")


