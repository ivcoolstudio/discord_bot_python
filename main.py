import os
import discord, random
from discord.ext import commands
import json
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.command()
async def орелилирешка(ctx):
    await ctx.send(random.choice(['орел 🌕', 'решка 🌑']))

@client.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))
    
@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запросhttps://notF.ivancool.repl.co
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 1)))

@client.command(pass_context=False)
async def пинг(ctx):
  # Вывод задержки в чат с помощью команды .пинг
  await ctx.send('Пинг: {0}'.format(client.latency))
@client.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
@client.command()
async def help_me(ctx):
    await ctx.send(f"/fox - отправляет случайную картинку лисы \n /rand - отправляет случайное число от 1 до 100 \n /hello - поздороваться с ботом \n /ping - получить ответ и узнать информацию о пинге бота \n /help me - узнать основные команды бота \n /орелилирешка сыграть в орел или решку \n ")  #перенос строки осуществляется добавлением: \n без кнопки Enter!
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='real life', url='https://www.twitch.tv/playthislist'))
    print("Bot is connected to all of the available servers in the bots mainframe.")
@client.command()
async def tetris(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на сайт с тетрисом",
        url='https://ivcoolstudio.github.io/myprojacts/',
    )
    await ctx.send(embed=embed)

client.run('MTA1MTUwMDkyODIzNjI2OTU4OA.GeaXQY.OPqXa8SWZ8ejVABTRs2Ipy0S3jnAghiLmM0oeo')
