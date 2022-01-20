#Duck Bot
import discord
import os
from discord.utils import get
from duckbottoken import duckbot
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="$", intents=intents)
file = ""
client = discord.Client()
@bot.command(pass_context=True,brief='This command will mute people', help='This command will mute people for you')
async def mute(ctx, member: discord.Member):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

		await member.add_roles(mutedRole)
		await member.send(f" you have muted from: - {ctx.guild.name}")
		embed = discord.Embed(title="mute", description=f" muted-{member.mention}",colour=discord.Colour.light_gray())
		await ctx.send(embed=embed)
@bot.command()
async def unmute(ctx, member: discord.Member):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:

		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

		await member.remove_roles(mutedRole)
		await member.send(f" you have unmutedd from: - {ctx.guild.name}")
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
        await ctx.send("Sorry that is not a valid command please use $help to get a list off all the vaild commands")
@bot.command()
async def squadron(ctx, squadron):
	separator = ", "
	run = False
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		squadronname = squadron + " Squadron Information"
		embed= discord.Embed(title=squadronname.upper(), description="Information about " + squadron + " Squadron")
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
			user = await bot.fetch_user(804739629483032587)
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
@bot.command()
async def join(ctx):
	await ctx.message.delete()
	await ctx.send('https://cdn.discordapp.com/attachments/931223718632521768/933446508362231868/Duck_Requirements.png')
@bot.command()
async def duck(ctx):
	await ctx.send('https://stats.warbrokers.io/squads/Duck')
					
bot.run(duckbot)