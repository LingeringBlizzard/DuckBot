#Duck Bot
import discord
import os
from discord.utils import get
from duckbottoken import duckbot
from discord.ext import commands
bot = commands.Bot(command_prefix="$")
file = ""
client = discord.Client()
@bot.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		await member.edit(nick=nick)
		await ctx.send(f'Nickname was changed for {member.mention} ')
@bot.command()
async def remove(ctx, arg1):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		await ctx.message.delete()
		await ctx.channel.purge(limit=int(arg1))
@bot.command()
async def invite(ctx):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		await ctx.message.delete()
		#creating invite link
		invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
	    #dming it to the person
		await ctx.author.send(invitelink)
@bot.command()
async def recruitme(ctx, member: discord.Member):
	if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.id == 592430350630912004:
		user = ctx.message.author
		role = discord.utils.get(user.guild.roles, name="Private Sector")
		await member.add_roles(role)
					
bot.run(duckbot)