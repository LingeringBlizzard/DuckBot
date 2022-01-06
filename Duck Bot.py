#Duck Bot
import discord
import os
from discord.utils import get
from duckbottoken import duckbot
client = discord.Client()
file = ""

def check(reaction, user):
	if  user != client.user and str(reaction.emoji) == '🇺🇸':
		return True
	elif user != client.user and  str(reaction.emoji) == '🇺🇲':
		return True
	elif  user != client.user and str(reaction.emoji) == '🇮🇳':
		return True
	elif  user != client.user and str(reaction.emoji) == '🇬🇧':
		return True
	elif  user != client.user and str(reaction.emoji) == '🇦🇺':
		return True
	elif  user != client.user and str(reaction.emoji) == '🇨🇳':
		return True
	else:
		return False
def check1(reaction, user):
	if  user != client.user and str(reaction.emoji) != '🇺🇸':
		return False
	elif user != client.user and  str(reaction.emoji) != '🇺🇲':
		return False
	elif  user != client.user and str(reaction.emoji) != '🇮🇳':
		return False
	elif  user != client.user and str(reaction.emoji) != '🇬🇧':
		return False
	elif  user != client.user and str(reaction.emoji) != '🇦🇺':
		return False
	elif  user != client.user and str(reaction.emoji) != '🇨🇳':
		return False
	else:
		return True
def checkrandom(reaction, user):
	if  user != client.user and str(reaction.emoji) == '🦆':
		return True
	elif user != client.user and  str(reaction.emoji) == '🎮':
		return True
	elif  user != client.user and str(reaction.emoji) == '📣':
		return True
	else:
		return False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_raw_reaction_add(payload):
	user = payload.member
	if payload.message_id == 928522305909424169:
		if str(payload.emoji) == '🇺🇸':
			role = get(user.guild.roles, name="USA")
			await payload.member.add_roles(role)
		elif str(payload.emoji) == '🇺🇲':
			role = get(user.guild.roles, name="USA_West")
			await payload.member.add_roles(role)
		elif str(payload.emoji) == '🇮🇳':
			role = get(user.guild.roles, name="India")
			await payload.member.add_roles(role)
		elif str(payload.emoji) == '🇬🇧':
			role = get(user.guild.roles, name="Europe")
			await payload.member.add_roles(role)
		elif str(payload.emoji) == '🇦🇺':
			role = get(user.guild.roles, name="Australia")
			await payload.member.add_roles(role)
		elif str(payload.emoji) == '🇨🇳':
			role = get(user.guild.roles, name="Asia")
			await payload.member.add_roles(role)
		channel = client.get_channel(payload.channel_id)
		message = await channel.fetch_message(payload.message_id)
		await message.remove_reaction(payload.emoji, payload.member)

		
	if payload.message_id == 928522319259893780:
		reaction = payload.emoji
		user = payload.member
		if str(reaction) == '📣':
			role = get(user.guild.roles, name="Announcements")
			await user.add_roles(role)
		elif str(reaction) == '🎮':
			role = get(user.guild.roles, name="Game Night")
			await user.add_roles(role)
		elif str(reaction) == '🦆':
			role = get(user.guild.roles, name="interested in joining")
			await user.add_roles(role)
		channel = client.get_channel(payload.channel_id)
		message = await channel.fetch_message(payload.message_id)
		await message.remove_reaction(payload.emoji, payload.member)


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.author.guild_permissions.administrator == True:
		if message.content.startswith('$purge'):
			await message.channel.purge(limit=100)
		if message.content.startswith('$roles'):
			run = True
			await message.delete()
			channel = message.channel
			msg = await channel.send('Server region\n🇺🇸 - USA\n🇺🇲 - USA_West\n🇮🇳 - India\n🇬🇧 - Europe\n🇦🇺 - Australia\n🇨🇳 - Asia')
			await msg.add_reaction('🇺🇸')
			await msg.add_reaction('🇺🇲')
			await msg.add_reaction('🇮🇳')			
			await msg.add_reaction('🇬🇧')
			await msg.add_reaction('🇦🇺')
			await msg.add_reaction('🇨🇳')
			global file
			file = msg.id

			# while run == True:
			# 	try:
			# 		reaction, user = await client.wait_for('reaction_add', check=check)
			# 	except:
			# 		channel.send("NOOO what did you do?")
			# 	else:
			# 		if str(reaction.emoji) == '🇺🇸':
			# 			role = get(user.guild.roles, name="USA")
			# 			await user.add_roles(role)
			# 		elif str(reaction.emoji) == '🇺🇲':
			# 			role = get(user.guild.roles, name="USA_West")
			# 			await user.add_roles(role)
			# 		elif str(reaction.emoji) == '🇮🇳':
			# 			role = get(user.guild.roles, name="India")
			# 			await user.add_roles(role)
			# 		elif str(reaction.emoji) == '🇬🇧':
			# 			role = get(user.guild.roles, name="Europe")
			# 			await user.add_roles(role)
			# 		elif str(reaction.emoji) == '🇦🇺':
			# 			role = get(user.guild.roles, name="Australia")
			# 			await user.add_roles(role)
			# 		elif str(reaction.emoji) == '🇨🇳':
			# 			role = get(user.guild.roles, name="Asia")
			# 			await user.add_roles(role)
			# 	finally:
			# 		await reaction.remove(user)
		if message.content.startswith("$randomroles"):
			run = True
			await message.delete()
			channel = message.channel
			msg = await channel.send('Random Roles\n🦆 Interested in Joining\n🎮 game night ping\n📣 announcements')
			await msg.add_reaction('🦆')
			await msg.add_reaction('🎮')
			await msg.add_reaction('📣')
			global file2
			file2 = msg.id


			# try:
			# 	reaction, user = await client.wait_for('reaction_add', check=check)
			# except:
			# 	channel.send("NOOO what did you do?")
			# else:
			# 	if str(reaction.emoji) == '📣':
			# 		role = get(user.guild.roles, name="Announcements")
			# 		await user.add_roles(role)
			# 	elif str(reaction.emoji) == '🎮':
			# 		role = get(user.guild.roles, name="Game Night")
			# 		await user.add_roles(role)
			# 	elif str(reaction.emoji) == '🦆':
			# 		role = get(user.guild.roles, name="interested in joining")
			# 		await user.add_roles(role)
			# finally:
			# 	await reaction.remove(user)




					

client.run(duckbot)