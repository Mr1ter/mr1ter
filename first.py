import discord
import random
import json
import asyncio
import os
from discord.ext import commands
from config import settings
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix = '!?', help_command=None)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(title="У-упс...", description='Упомяните пользователя.', color=0xff0000))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="У-упс...", description='У Вас нет прав на использование данной команды.', color=0xff0000))
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=discord.Embed(title="У-упс...", description='Данной команды не существует. \nДля того, чтобы узнать, какие у меня команды, пропишите ``!?help``.', color=0xff0000))

# Приветствие
@bot.command() 
async def hello(ctx, member: member.Discord):
	await ctx.send(f'Привет, {member.mention}!')

# Говорилка (доступно только создателю бота)
@bot.command()
async def say(ctx, *, arg=None):
	if (ctx.author.id==426699376090677258 or ctx.author.id==715160316425797722):
		await ctx.message.delete()
		await ctx.send(arg)
	else:
		print("")
	
# Да/Нет
@bot.command()
async def r(ctx):
	author = ctx.message.author
	g=random.randint(0, 1)
	if (g==0):
		await ctx.send(f'Да, {author.mention}.')
	else:
		await ctx.send(f'Нет, {author.mention}.')
#Кубик
@bot.command()
async def roll(ctx, arg=None):
	if arg==None:
		await ctx.send(embed= discord.Embed(color = 0xff0000, title = 'У-упс...', description='Введите число.'))
	else:
		author = ctx.message.author
		B=int(arg)
		A=0
		g=int(random.uniform(A, B))
		await ctx.send(embed = discord.Embed(color = 0xff0000, title = 'Кубик кинут!', description=f'Выпало число: {g}'))
#Помощь
@bot.command()
async def help(ctx):
	embed = discord.Embed(color = 0xff0000, title = 'Команды', description='Префикс бота - !? \nroll - кинуть кубик \nr - ответ на вопрос (Да/Нет) \nban - забанить участника \nkick - кикнуть участника \npoll - голсование \ninvite - ссылка приглашение бота на свой сервер! \ninfo - инфо о боте')
	await ctx.send(embed = embed)
# Сказать в емб (доступна только создателю бота)
@bot.command()
async def sayemb(ctx, name, *, arg=None):
	if (ctx.author.id==426699376090677258 or ctx.author.id==715160316425797722):
		author = ctx.message.author
		if name == 'Жирный':
			await ctx.message.delete()
			embed = discord.Embed(color = 0xff0000, title = arg, description="")
			await ctx.send(embed = embed)
		elif name == 'Тонкий':
			await ctx.message.delete()
			embed = discord.Embed(color = 0xff0000, title = "", description=arg)
			await ctx.send(embed = embed)
		else:
			await ctx.send(f'{author.mention}, выберите шрифт.')
	else:
		print("")
# Инвайт
@bot.command()
async def invite(ctx):
	embed = discord.Embed(color = 0xff0000, title = 'Ссылка-приглашение бота на личный сервер', description='https://discordapp.com/oauth2/authorize?&client_id=815741276984967238&scope=bot&permissions=2081422591')
	await ctx.send(embed = embed)
# Информация
@bot.command()
async def info(ctx):
	embed = discord.Embed(color = 0xff0000, title = 'Информация', description='Создатель: 𝕄𝕣𝕚𝕥𝕖𝕣.ink#5540 \nКодер: Mäster#3004, dead.ink#2796 \nСсылка на официальный сервер бота: https://discord.gg/rHMzm33DDD')
	await ctx.send(embed = embed)
# Бан
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	e=discord.Embed(color=0xff0000, title=None, description=f'{member.mention} забанен! Причина: {reason}.')
	await ctx.send(embed=e)
	await member.ban(reason=reason)
# Кик
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	e=discord.Embed(color=0xff0000, title=None, description=f'{member.mention} кикнут! Причина: {reason}.')
	await ctx.send(embed=e)
	await member.kick(reason=reason)
# Голосование
@bot.command()
async def poll(ctx, *, arg=None):
    author = ctx.message.author
    await ctx.message.delete()
    emb = discord.Embed(title=f'Голосование от {author.name}!', description=f'{arg}', color=0xff0000)
    message = await ctx.send(embed=emb)
    await message.add_reaction('✅')
    await message.add_reaction('❌')
	
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
