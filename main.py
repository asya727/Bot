import discord
from discord.ext import commands
import os, random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Ayrışma süreleri sözlüğü
ayrışma_süreleri = {
    'plastik şişe': '450 yıl',
    'kağıt': '2-6 hafta',
    'cam şişe': '1 milyon yıl',
    'alüminyum kutu': '200 yıl',
    'lastik': '50-80 yıl'
}

@bot.command(name='ayrışma_süresi')
async def ayrışma_süresi(ctx, *, eşya: str):
    süre = ayrışma_süreleri.get(eşya.lower())
    if süre:
        await ctx.send(f"{eşya.title()} yaklaşık olarak {süre} sürede ayrışır.")
    else:
        await ctx.send(f"Üzgünüm, {eşya} hakkında bilgi bulamadım. Lütfen başka bir eşya deneyin.")

# Botu çalıştır
bot.run('Buraya Token EklenmeLİ')
