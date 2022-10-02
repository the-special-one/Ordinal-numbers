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

@client.event
async def on_member_join(member):
	commandes_channel: discord.TextChannel = client.get_channel("channel ID)
	await commandes_channel.send(content=f"Bienvenida sur le serveur {member.display_name} !") 

client.run("MY TOKEN")


