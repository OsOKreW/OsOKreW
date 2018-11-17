#OsOKreW by Giovy52845

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='#')
client = discord.Client()

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)


@bot.command(pass_context=True)
async def comandi(ctx):
    embed = discord.Embed(name="{}'s comandi".format(ctx.message.server.name), color=0x58aae2)
    embed.add_field(name="#regole", value="**Con questo comando puoi vedere tutte le regole.**",  inline=False)
    embed.add_field(name="#info", value="**Con questo comando puoi vedere tutte le info riguardanti una persona.**", inline=False)
    embed.add_field(name="#serverinfo", value="**Con questo comando puoi vedere tutte le info riguardanti il server.**", inline=False)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def regole(ctx):
    await bot.say("**1)** Rispetta gli amministratori e i membri!\n**2)** Non copiare i nickname. Ad esempio: Nickname1, Nickname2 ecc.\n**3)** Questo elenco non copre tutte le regole; ma solo quelle di base. Se un amministratore trova un         **comportamento inadeguato**, lo modera di conseguenza.\n**4)** Non inviare link a siti web di truffa, pornografici, phishing o qualsiasi cosa che possa danneggiare          il computer dell'utente o considerati inappropriati in quanto vogliamo che gli utenti siano al sicuro durante il         loro utilizzo.\n**5)** Non linkare siti web esterni o immagini che includono contenuti sessuali, violenti o inappropriati.\n**6)** Non inviare link di altri server discord.\n**7)** Sono proibite le critiche alle sanzioni ricevute e ai richiami ricevuti da parte di un amministratore o         moderatore. Qualsiasi osservazione o obiezione in merito va fatta esclusivamente in privato.\n**8)** È vietato entrare sul server con doppi e tripli account che riconducano alla stessa persona.\n\n__**Nota bene:**__\nLa violazione delle regole 4, 5, 6 e 8 del Regolamento generale è punibile con il **ban immediato e permanente dal server** senza preavviso. La violazione delle altre regole sono punibili inizialmente o con un’ammonizione.")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Ecco quello che ho trovato.", color=0x58aae2)
    embed.add_field(name="Nome:", value=user.name, inline=True)
    embed.add_field(name="ID: ", value=user.id, inline=True)
    embed.add_field(name="Stato:", value=user.status, inline=True)
    embed.add_field(name="Ruolo più alto:", value=user.top_role)
    embed.add_field(name="Entrato il: ", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), color=0x58aae2)
    embed.add_field(name="Nome:", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Ruoli:", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Membri:", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

client.run(str(os.environ.get('BOT_TOKEN')))
