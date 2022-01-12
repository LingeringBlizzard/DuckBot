#Duck Bot
import discord
import os
from discord.utils import get
from duckbottoken import duckbot
from discord.ext import commands
bot = commands.Bot(command_prefix="$")
file = ""
client = discord.Client()
@bot.command(brief='This command will mute people', help='This command will mute people for you')
async def mute(ctx, member: discord.Member):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		role = discord.utils.get(member.server.roles, name='Muted')
		await bot.add_roles(member, role)
		embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
		await bot.say(embed=embed)
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
    else:
    	await ctx.send("Sorry You entered this command incorrectly please use $help (command) to get the usage of this command")

					
bot.run(duckbot)