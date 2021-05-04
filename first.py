import discord
import random
import json
import asyncio
import os
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions, CheckFailure, Bot

bot = commands.Bot(command_prefix = '!?', help_command=None)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=discord.Embed(title="У-упс...", description='Упомяните пользователя.', color=0xff0000))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="У-упс...", description='У Вас нет прав на использование данной команды.', color=0xff0000))
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=discord.Embed(title="У-упс...", description='Данной команды не существует. \nДля того, чтобы узнать, какие у меня команды, пропишите ``!?help``.', color=0xff0000))

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Вас и ждёт Ваших указаний."))
        await asyncio.sleep(10)
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "на команды"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="помощь: !?help"))
        await asyncio.sleep(10)

# Текст от имени бота
@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, arg=None):
	await ctx.message.delete()
	await ctx.send(arg)
	
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
	embed = discord.Embed(color = 0xff0000, title = 'Команды', description='Префикс бота - !? \n[] - данные скобки писать не надо. Они нужны, чтобы обозначить функцию. \n \nКоманды модерирования: \nban [@пинг] [Причина] - забанить участника (нужно право на бан) \nunban [ID] - разбанить участника (нужно право на бан) \nkick [@пинг] [Причина] - кикнуть участника (нужно право на кик) \npurge [число] - очистить канал от сообщений (нужно право на управление сообщениями) \nnick [@пинг] [ник] - изменить ник участнику (нужны права на изменение никнеймов) \n \nРП-команды: \nanon - надеть маску анонимуса \nhead [@пинг] - кивнуть кому-то головой \ncrazy - психануть \ngoaway [@пинг] - послать обидчика \nkill [@пинг] - убить кого-то \nhyp [@пинг] - загипнотизировать кого-то \nreadrap - зачитать рэп :sunglasses: \nsteal [@пинг] - стянуть с кого-то маску \npat [@пинг] - погладить кого-то \n \nРазвлекательные команды: \nroll [число] - кинуть кубик \nr [Вопрос] - ответ на вопрос \npoll [Текст] - голсование \nsay [Текст] - сказать что-то от имени бота (нужны права администратора) \nsayemb [Жирный/Тонкий] [Текст] - сказать в ембед оформлении (нужны права администратора) \n \nРазное:  \ninvite - ссылка приглашение бота на свой сервер! \ninfo - инфо о боте')
	await ctx.send(embed = embed)

# Сказать в емб 
@bot.command()
@commands.has_permissions(administrator=True)
async def sayemb(ctx, name, *, arg=None):
		if name == 'Жирный':
			await ctx.message.delete()
			embed = discord.Embed(color = 0xff0000, title = arg, description="")
			await ctx.send(embed = embed)
		elif name == 'Тонкий':
			await ctx.message.delete()
			embed = discord.Embed(color = 0xff0000, title = "", description=arg)
			await ctx.send(embed = embed)
		else:
			await ctx.send(embed=discord.Embed(color=0xff0000, title="У-упс...", description="Выберите шрифт."))
# Инвайт
@bot.command()
async def invite(ctx):
	embed = discord.Embed(color = 0xff0000, title = 'Ссылка-приглашение бота на свой сервер', description='https://discordapp.com/oauth2/authorize?&client_id=815741276984967238&scope=bot&permissions=1916267615')
	await ctx.send(embed = embed)
# Информация
@bot.command()
async def info(ctx):
	embed = discord.Embed(color = 0xff0000, title = 'Информация', description='Ссылка на официальный сервер бота: https://discord.gg/rHMzm33DDD \nРазработка бота временно приостановлена.')
	await ctx.send(embed = embed)

# Бан
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	if reason==None:
		e=discord.Embed(color=0xff0000, description=f'{member.mention} забанен!')
		await ctx.send(embed=e)
		await member.ban(reason=reason)
	else:
		e=discord.Embed(color=0xff0000, description=f'{member.mention} забанен! Причина: {reason}.')
		await ctx.send(embed=e)
		await member.ban(reason=reason)
# Кик
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	if reason==None:
		e=discord.Embed(color=0xff0000, description=f'{member.mention} кикнут!')
		await ctx.send(embed=e)
		await member.kick(reason=reason)
	else:
		e=discord.Embed(color=0xff0000, description=f'{member.mention} кикнут! Причина: {reason}.')
		await ctx.send(embed=e)
		await member.kick(reason=reason)

# Голосование
@bot.command()
async def poll(ctx, *, arg=None):
	if arg==None:
		embed = discord.Embed(color = 0xff0000, title = 'У-упс...', description='Для голосования должен быть хотя бы введён один символ.')
		await ctx.send(embed=embed)
	else:
		author = ctx.message.author
		await ctx.message.delete()
		emb = discord.Embed(title=f'Голосование от {author.name}!', description=f'{arg}', color=0xff0000)
		message = await ctx.send(embed=emb)
		await message.add_reaction('✅')
		await message.add_reaction('❌')

# Очистка сообщений
@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, arg=None):	
	if arg==None:		
		embed = discord.Embed(color=0xff0000, title = 'У-упс...', description='Введите число.')
		await ctx.send(embed=embed)	
	else:		
		await ctx.message.delete()		
		await ctx.channel.purge(limit=int(arg))		
		e = discord.Embed(color=0xff0000, description=f'Очищено сообщений: {arg}')		
		msg = await ctx.send(embed = e)
		await asyncio.sleep(10)
		await msg.delete()

#Разбан
@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, id: int = None):
    if id == None:
        await ctx.send(embed = discord.Embed(title = "У-упс...", description = 'Введите ID пользователя, которого Вы хотите разбанить.', color = 0xff0000))
    else:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(embed = discord.Embed(color = 0xff0000, title = None, description = f'Пользователь с ID {id} разбанен.'))

@bot.command()
async def anon(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} надел маску анонимуса.')
    embed.set_image(url = "https://media1.tenor.com/images/7f93abaaad9c81a5259d9e23ff1f7387/tenor.gif?itemid=21086303")
    await ctx.send(embed = embed)
		
@bot.command()
async def crazy(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} психанул.')
    embed.set_image(url = "https://media.tenor.com/images/01c5ae075fded0333a19a47327f7d34e/tenor.gif")
    await ctx.send(embed = embed)

@bot.command()
async def head(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} кивнул головой {member.mention}')
    embed.set_image(url = "https://media1.tenor.com/images/6dcf202b55e975d31dc53b3472939ec7/tenor.gif?itemid=21086444")
    await ctx.send(embed = embed)

@bot.command()
async def goaway(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} послал к чёрту {member.mention}')
    embed.set_image(url = "https://media1.tenor.com/images/0199532a38dabaf2a172fc01983779ba/tenor.gif?itemid=21086433")
    await ctx.send(embed = embed)

@bot.command()
async def kill(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} убил {member.mention}')
    embed.set_image(url = "https://media1.tenor.com/images/8b7ce78b6a6322bc9756787078f6edb7/tenor.gif?itemid=21086360")
    await ctx.send(embed = embed)

@bot.command()
async def hyp(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} загипнотизировал {member.mention}')
    embed.set_image(url = "https://media.tenor.com/images/1e59b308fd24980cea8363122c8c0d30/tenor.gif")
    await ctx.send(embed = embed)

@bot.command()
async def readrap(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention}  анонимно зачитал рэп. :sunglasses:')
    embed.set_image(url = "https://media.tenor.com/images/7312df4d5106d173949fe7099aee1c6a/tenor.gif")
    await ctx.send(embed = embed)

@bot.command()
async def steal(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} стянул маску анонимуса с {member.mention}')
    embed.set_image(url = "https://media.tenor.com/images/d5ae5f2d8f12528c9e126ef7c9a411c9/tenor.gif")
    await ctx.send(embed = embed)

@bot.command()
async def pat(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, description = f'{author.mention} погладил {member.mention}')
    embed.set_image(url = "https://media1.tenor.com/images/45a2ab1d40f7b1006e3871654828bbe8/tenor.gif?itemid=21086521")
    await ctx.send(embed = embed)
	
@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, *, nickname=None):
  if nickname==None:
    embed = discord.Embed(color = 0xff0000, title = "У-упс...", description="Введите новый никнейм для пользователя.")
    await ctx.send(embed=embed)
  else:
    await member.edit(nick=nickname)
    embed = discord.Embed(color=0xff0000, title="Done!", description=f'Ник пользователя {member.name} изменён на {nickname}')
    await ctx.send(embed=embed)

	
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
