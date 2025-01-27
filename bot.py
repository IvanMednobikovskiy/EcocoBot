#Бот, рассказывающий о времени разложения бытовых предметов

import random
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

items = {
    'пластик': 450,
    'стекло': 1000,
    'бумага': 5,
    'банка': 100,
    'сигарета': 2,
    'стиропор': 500,
    'пакет': 20,
    'шина': 80,
    'подгузник': 500,
    'ткань': 5,
    'сталь': 50,
    'яблоко': 2,
    'банан': 5,
    'жвачка': 5,
    'дерево': 10,
    'картон': 2,
    'газета': 6,
    'коробка': 3,
    'соломинка': 200
}

@bot.command()
async def howlong(ctx, item):
    item = item.lower()
    if item in items.keys():
        await ctx.send(f'Вещь {item} разлагаеться {items[item]} лет')
    else:
        await ctx.send('Такой вещи нет в базе данных')

# бот, который дает советы по экологии
@bot.command()
async def eco(ctx):
    facts = [
        "Каждый год в океаны попадает около 8 миллионов тонн пластика.",
        "Леса покрывают около 30% поверхности земли и являются домом для 80% наземных видов животных и растений.",
        "Более миллиарда людей живут без доступа к чистой питьевой воде.",
        "Один рециклированный стеклянный бутыль экономит достаточно энергии, чтобы запитать лампу на 4 часа.",
        "Каждое сохраненное дерево может поглотить около 21 кг углекислого газа в год."
    ]
    await ctx.send(f'Рандомный факт: {random.choice(facts)}')

@bot.command()
async def joke(ctx):
    jokes = [
        "Почему электрические машины такие счастливые? Потому что они всегда заряжаются позитивом!",
        "Какое любимое дерево у экологов? Экстремально зеленое!",
        "Почему у компоста всегда хорошее настроение? Потому что он знает, что из него вырастет что-то прекрасное!",
        "Как называют супергероя, который спасает планету, сортируя мусор? Сортировщик-ман!",
        "Почему солнечные панели такие болтливые? Потому что у них всегда есть что сказать о светлых сторонах жизни!"
    ]
    await ctx.send(f'Шуточка: {random.choice(jokes)}')

bot.run('')