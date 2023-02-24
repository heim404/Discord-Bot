import discord
from discord.ext import commands
import datetime
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("BOT ONLINE")

@bot.command()
async def ola(ctx):
    username=ctx.message.author.mention
    await ctx.send("OLA" + username)


@bot.command()
@commands.has_any_role("Admin")
async def ban(ctx, member:discord.Member, *, reason="None"):
    if reason == None:
        reason = "Este nelo foi banido pelo boi " + ctx.message.author.name
    await member.ban(reason=reason)    

#kick user do server
@bot.command()
async def kick(ctx, member:discord.Member, *, reason="None"):
    kicker=ctx.message.author.mention
    if ctx.author.guild_permissions.kick_members:
        await member.kick()
        await ctx.send(f'{member.display_name} foi kikado pelo ' + kicker)
    else:
        await ctx.send(kicker + f' tentou dar kick ao {member.display_name} mas falhou que nem um bot')

#disconect user do canal
@bot.command()
async def boot(ctx, member: discord.Member):
    kicker=ctx.message.author.mention
    if ctx.author.guild_permissions.move_members:
        if member.voice:
            await member.move_to(None)
            await ctx.send(f'{member.display_name} levou um pontape do canal, quem deu o pontape '+ kicker)
        else:
            await ctx.send(f'{member.display_name} esse prototipo de pessoa nao se encontra no servidor')
    else:
        await ctx.send(kicker + f' tentou dar disconnect ao {member.display_name} so que nao capacidades para tanto')

#mute user por x tempo segundos ou minutos
@bot.command()
@commands.has_any_role("Admin")
async def mute(ctx, member:discord.Member, timelimit):
    if "s" in timelimit or "S" in timelimit:
       gettime = timelimit.strip("s")
       if int(gettime) > 2419000:
           await ctx.send("O tempo nao pode ser maior que 28 dias")
       else:
        newtime = datetime.timedelta(seconds=int(gettime))
        await member.edit(timed_out_until=discord.utils.utcnow()+ newtime)
    elif "m" in timelimit:
          gettime = timelimit.strip("m")
          if int(gettime) > 40320:
            await ctx.send("O tempo nao pode ser maior que 28 dias")
          else:
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow()+ newtime)








bot.run("")
