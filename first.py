import discord
import random
import json
import asyncio
import os
from discord.ext import commands
from config import settings
from help import information
import json

bot = commands.Bot(command_prefix = settings['prefix'], help_command=None)
bot.remove_command('help')

@bot.command() 
async def hello(ctx, arg): 
    author = ctx.message.author 

    await ctx.send(f'Привет, {author.mention}!')

@bot.command()
async def say(ctx, *, arg):
	await ctx.message.delete()
	await ctx.send(arg)
	
@bot.command()
async def r(ctx):
	author = ctx.message.author
	g=random.randint(0, 1)
	if (g==0):
		await ctx.send(f'Да, {author.mention}.')
	else:
		await ctx.send(f'Нет, {author.mention}.')

@bot.command()
async def funny(ctx):
	await ctx.message.delete()
	await ctx.send('АХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХАХААХААХХАХАХААХАХАХААХАХ')

@bot.command()
async def roll(ctx, arg):
	author = ctx.message.author
	B=int(arg)
	A=0
	g=int(random.uniform(A, B))
	await ctx.send(f'Кубик кинут... {author.mention}')
	await ctx.send('```Ваше число:```')
	await ctx.send(g)

@bot.command()
async def help(ctx):
	embed = discord.Embed(color = 0xff0000, title = 'Команды', description='Префикс бота - !? \nroll - кинуть кубик \nr - ответ на вопрос (Да/Нет) \nfunny - :) \nsay - скажет за Вас всё что угодно! \nsayemb Шрифт(Жирный/Тонкий) текст - текст в ембед')
	await ctx.send(embed = embed)
        
@bot.command()
async def spam(ctx, aor=None, *, arg = None):
	a = ctx.message.author
	if aor == 'bесконечна':
		await ctx.message.delete()
		await ctx.send(f'Нехороший же ты человек, {a.mention}!')
		b=0
		print(f'{a.mention} запустил спам!')
		while b <= 59:
			await ctx.send(arg)
			b = b + 1
			print('Спам в процессе:', b, '/ 60!')
	else:
		await ctx.send("Гуляй)")
		print(f'{a.mention} попытался запустить спам!')
		

@bot.command()
async def sayemb(ctx, name, *, arg):
	author = ctx.message.author
	await ctx.message.delete()
	if name == 'Жирный':
		embed = discord.Embed(color = 0xff0000, title = arg, description="")
		await ctx.send(embed = embed)
	elif name == 'Тонкий':
		embed = discord.Embed(color = 0xff0000, title = "", description=arg)
		await ctx.send(embed = embed)
	else:
		await ctx.send(f'{author.mention}, выберите шрифт.')
	
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
