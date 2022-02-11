#Duck Bot
import asyncio

import discord
import time
import urllib.request
from bs4 import BeautifulSoup
import os
from discord.utils import get
from duckbottoken import duckbot
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)
file = ""
client = discord.Client()
def getsquadnames():
	content = urllib.request.urlopen('https://stats.warbrokers.io/squads/Duck')
	read_content = content.read()
	soup = BeautifulSoup(read_content,'html.parser')
	squadmemberlinks = []
	squadmembernames = []
	for squadmembers in soup.find_all("div", class_="squad-player-header"):
		squadmembers = squadmembers.find('a')
		squadmember = squadmembers.get_text()
		squadmembernames.append(squadmember)
		squadmemberlink = squadmembers.get("href")
		squadmemberlinks.append(squadmemberlink)
	# for squadmembers in soup.fine_all("div", class_="squad-player-number-box-header"):
	# 	squadmembers = squadmembers.find('div')
	# 	print(squadmembers)
	return squadmemberlinks, squadmembernames
@bot.command()
async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		roleobject = discord.utils.get(ctx.guild.roles, name="Muted")
		if roleobject in user.roles:
			await ctx.send(f"Sorry, I cannot mute {user}, they are already muted")
			return
		await user.add_roles(roleobject)
		if (duration == 0 and unit == None):
			duration = ":infinity:"
			unit = ""
			await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
			return
		await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")


		if unit == "s":
			wait = 1 * duration
			await asyncio.sleep(wait)
		elif unit == "m":
			wait = 60 * duration
			await asyncio.sleep(wait)
		elif unit == "h":
			wait = 6600 * duration
			await asyncio.sleep(wait)
		elif unit == None:
			wait = wait = 6600 * duration
			await asyncio.sleep(wait)
		if (user.guild.roles == roleobject):
			await user.remove_roles(roleobject)
			await ctx.send(f":white_check_mark: {user} was unmuted")
@bot.command()
async def unmute(ctx, member: discord.Member):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:

		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

		await member.remove_roles(mutedRole)
		await member.send(f" you have been unmuted from: - {ctx.guild.name}")
		embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
		await ctx.send(embed=embed)
@bot.command(pass_context=True, brief='This will change a users nickname', help='This command will change the nickname of a user')
async def nick(ctx, member: discord.Member, nick):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		await member.edit(nick=nick)
		await ctx.send(f'Nickname was changed for {member.mention} ')
@bot.command(breif='This will remove the amount of messages you specify')
async def remove(ctx, number):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		await ctx.message.delete()
		await ctx.channel.purge(limit=int(number))
@bot.command(brief='This creates a invite link')
async def invite(ctx):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		await ctx.message.delete()
		#creating invite link
		invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
	    #dming it to the person
		await ctx.author.send(invitelink)
@bot.command(brief='Gives the role Private Sector')
async def accept(ctx, member: discord.Member):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		user = ctx.message.author
		role = discord.utils.get(user.guild.roles, name="Private Sector")
		await member.add_roles(role)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, that is not a valid command. Please use $help to get a list of all the vaild commands")
@bot.command()
async def squadron(ctx, squadron):
	separator = ", "
	run = False
	squadronname = squadron + " Squadron Information"
	embed= discord.Embed(title=squadronname.upper(), description="Information about " + squadron + " Squadron")
	try:
		if str(squadron).lower() == "black":
			link = 'https://cdn.discordapp.com/attachments/931223718632521768/933463212245024778/unknown.png'
			guild = ctx.guild.get_role(911352519517700148)
			user = await bot.fetch_user(667431741245358096)
			usernames = [m.name for m in guild.members]
			run = True
		elif str(squadron).lower() == "gold":
			link = 'https://cdn.discordapp.com/attachments/931223718632521768/933489928774508595/goldsquadronreqs.png'
			guild = ctx.guild.get_role(911352074200043552)
			user = await bot.fetch_user(814177227688247296)
			usernames = [m.name for m in guild.members]
			run = True
		elif str(squadron).lower() == "red":
			link = 'https://cdn.discordapp.com/attachments/931223718632521768/933490419105398804/redsquadronreqs.png'
			guild = ctx.guild.get_role(911349152829566997)
			user = None
			usernames = [m.name for m in guild.members]
			run = True
		elif str(squadron).lower() == "gray":
			guild = ctx.guild.get_role(911352664472821760)
			link = 'https://media.discordapp.net/attachments/931223718632521768/933499430450135092/graysquadronreqs.png'
			user = None
			usernames = [m.name for m in guild.members]
			run = True
		elif str(squadron).lower() == "green":
			guild = ctx.guild.get_role(911352765006102539)
			link = 'https://cdn.discordapp.com/attachments/931223718632521768/933500137693655050/unknown.png'
			user = None
			usernames = [m.name for m in guild.members]
			run = True
		else:
			await ctx.send("That is not a valid Squadron")
		if run is True:
			if user == None:
				embed.set_image(url=link)
				embed.add_field(name="Members Of Squadron", value=separator.join(usernames))
				await ctx.send(embed=embed)
			else:
				embed.add_field(name="Squadron Leader", value=user.display_name, inline=False)
				embed.set_thumbnail(url=user.avatar_url)
				embed.set_image(url=link)
				embed.add_field(name="Members Of Squadron", value=separator.join(usernames))
				await ctx.send(embed=embed)
	except:
		await ctx.send("Sorry, this command did not work properly. Please try again. If this issue continues, please contact LingeringBlizzard")

@bot.command()
async def join(ctx):
	await ctx.message.delete()
	await ctx.send('https://cdn.discordapp.com/attachments/931223718632521768/933446508362231868/Duck_Requirements.png')
@bot.command()
async def duck(ctx):
	number = 0
	embed = discord.Embed(title="Duck Squadron", description="[Click here to see full stats of Duck](https://stats.warbrokers.io/squads/Duck)")
	message = await ctx.send("Please wait, I am getting the data")
	try:
		squadmemberlink, squadmembernames = getsquadnames()
		for squadmembers in squadmemberlink:
			squadmembers = 'https://stats.warbrokers.io'+squadmembers
			embed.add_field(name='\u200b', value=" ["+squadmembernames[number]+"]"+"("+squadmembers+")")
			number = number + 1
		await message.delete()
		await ctx.send(embed=embed)
	except:
		await ctx.send("Sorry, there was a error")
					
bot.run(duckbot)
