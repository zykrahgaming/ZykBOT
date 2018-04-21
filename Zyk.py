$ heroku create myapp --buildpack heroku/python
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
bot_prefix= "."
client = commands.Bot(command_prefix=bot_prefix)

chat_filter = ["PINEAPPLE", "PIZZA"]
bypass_list = []

@client.event
async def on_ready ():
	print("Bot Online!")
	
@client.event
async def on_message(message):
	if message.content == "cookie":
		await client.send_message(message.channel, ":cookie:")

@client.event
async def on_message(message):
	if message.content.upper().startswith('!PING'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))
	if message.content.upper().startswith('!SAY'):
		userID = message.author.id
		if message.author.id == "221241527240884224":
			args = message.content.split(" ")
			#args[0] = !SAY
			#args[1] = Hey
			await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
		else:
			await client.send_message(message.channel, "<@%s> You don't have permission to use this command!" % (userID))
	if message.content.upper().startswith('!AMIADMIN'):
		if "437220942830108683" in [role.id for role in message.author.roles]:
			await client.send_message(message.channel, "You are an Admin")
		else:
			await client.send_message(message.channel, "You are not an Admin")
	
client.run("NDM3MTg5MDc2MzI0NDUwMzI0.Dbybkg.R5xLGaWsCCySpL-zKOmKXsbCBUw")
