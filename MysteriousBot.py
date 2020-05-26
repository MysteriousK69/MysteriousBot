import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
import asyncio
from discord.utils import find,get
import json
import requests as rq
import os
import random
import time
import datetime



bot = commands.Bot(command_prefix='!')

bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!help for a list of commands!"))

@bot.event
async def on_member_join(user):
    role=find(lambda m:m.name == 'Member',user.server.roles)
    await bot.add_roles(user,role)

@bot.command()
async def ping(ctx, name="ping", description="Shows the Bot Latency m/s", hidden=False):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Latency is {:.2f}ms'.format(duration))
    await ctx.message.delete()



#@bot.command(pass_context=True)
#@commands.has_role("Admin")
#async def get_role(ctx,role:discord.Role,member: discord.Member,content,name="get-role"):
#    try:
#        await bot.add_roles(role)
#        await ctx.send("Role added")
#        await ctx.message.delete()
#    except:
#        await ctx.send("Bot could not add that role")
#        await ctx.message.delete()


@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, content):
    try:
        await member.ban()
        await member.send(f"You were banned for {content}")
        await ctx.send("I have successfully banned them")
        await ctx.message.delete()
    except:
        await ctx.send("Error: You either dont have perms to perform this action or you did not mention a valid user!")

@bot.command()
@commands.has_role("staff")
async def warn(ctx, member : discord.Member, content):
    try:
        await member.send(f"You were warned for {content}")
        await ctx.send("I have warned them")
        await ctx.message.delete()
    except:
        await ctx.send("Error: You either dont have perms to perform this action or you did not mention a valid user!")
    
@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, member : discord.Member):
    try:
        await member.kick()
        await member.send(f"You were banned for {content}")
        await ctx.send("Member kicked sucessfully!")
        await ctx.message.delete()
    except:
        await ctx.send("Error: You either dont have perms to perform this action or you did not mention a valid user!")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def unban(ctx, member : discord.Member):
    try:
        await member.unban()
        await ctx.send("I hope they will join soon :D")
        await ctx.message.delete()
    except:
        await ctx.send("Error: You either dont have perms to perform this action or you did not mention a valid user!")
    
@bot.command(name="coin-flip")
async def coin_flip(ctx):
    coin_flip = [
        "Heads!",
        "Tails!"
    ]
    response = random.choice(coin_flip)
    embed = discord.Embed(title="Coin FLip", color=0xeee657)
    embed.add_field(name="Result for Coin Flip", value=response)

    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def shop(ctx):
    await ctx.message.delete()
    await ctx.send("https://shoppy.gg/@MysteriousK")

@bot.command(name="roll-dice")
async def roll_dice(ctx):
    roll_dice = [
        "1!",
        "2!",
        "3!",
        "4!",
        "5!",
        "6!"
    ]
    response = random.choice(roll_dice)

    embed=discord.Embed(title="Dice Roll",color=0xeee657)
    embed.add_field(name="Result for dice roll", value=response)

    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command(pass_context=True)
@commands.has_role("staff")
async def dmall(ctx, message):
    for members in bot.get_all_members():
        try:

                embed = discord.Embed(title="Announcement", description=message, color=ctx.message.author.top_role.colour)

                y=0
                x = y
                y = x + 1
                await members.send(embed=embed)
                await ctx.message.delete()
        except:
            continue

@bot.command()
async def addition(ctx, a: int, b: int):
    try:
        await ctx.send(a+b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers!")

@bot.command()
async def multiplication(ctx, a: int, b: int):
    try:
        await ctx.send(a*b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers!")

@bot.command()
async def greet(ctx):
    await ctx.send(":wave: Hello, there!")
    await ctx.message.delete()

@bot.command()
async def division(ctx, a: int, b:int):
    try:
        await ctx.send(a/b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers or you tried to divide by 0!")

@bot.command()
async def subtraction(ctx, a: int, b: int):
    try:
        await ctx.send(a-b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers!")

@bot.command()
async def add(ctx, a: int, b: int):
    try:
        await ctx.send(a+b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers!")

@bot.command()
async def multiply(ctx, a: int, b: int):
    try:
        await ctx.send(a*b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers!")

@bot.command()
async def divide(ctx, a: int, b:int):
    try:
        await ctx.send(a/b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers or you tried to divide by 0!")


@bot.command()
async def subtract(ctx, a: int, b: int):
    try:
        await ctx.send(a-b)
        await ctx.message.delete()
    except:
        await ctx.send("You did not send 2 valid integers!")

@bot.command()
async def square(ctx,a:int):
    try:
        await ctx.send(a*a)
    except:
        await ctx.send("You did not send a valid interger!")

@bot.command(name="minecraft-account")
async def minecraft_account(ctx):
    await ctx.send("https://shoppy.gg/@MysteriousK")
    await ctx.message.delete()


@bot.command()
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")
    await ctx.message.delete()

@bot.command()
async def tableflip(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")
    await ctx.message.delete()

@bot.command()
async def unflip(ctx):
    await ctx.send("┬─┬ ノ( ゜-゜ノ)")
    await ctx.message.delete()

@bot.command()
async def invite(ctx):
    await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=671365110832431115&permissions=8&scope=bot")
    await ctx.message.delete()

@bot.command(name="8ball")
async def eight_ball(ctx):
    eight_ball = [
        "This is a resounding no!",
        "Too hard to tell!",
        "Definitely!",
        "It is not looking likely!",
        "It is not quite possible!",
        "It is possible!",
        "Thats definitely a NO!"
    ]
    response = random.choice(eight_ball)

    embed = discord.Embed(title="Eight Ball", description="Result for 8 Ball", color=ctx.message.author.top_role.colour)

    embed.add_field(name="8 Ball", value=response)

    await ctx.send(embed=embed)

    await ctx.message.delete()


@bot.command()
async def pp(ctx):
    pp = [
        "8D",
        "8=D",
        "8==D",
        "8===D",
        "8====D",
        "8=====D",
        "8======D",
        "8=======D",
        "8========D",
        "8=========D",
        "8==========D",
        "8===========D",
        "8============D",
        "8=============D",
        "8==============D"
        
    ]
    response = random.choice(pp)

    embed = discord.Embed(title="PP measuring machine", description="Measure your PP", color=0xeee657)

    embed.add_field(name="Your PP", value=response)

    await ctx.send(embed=embed)

    await ctx.message.delete()

@bot.command()
async def status(ctx):
    embed = discord.Embed(title="Bot Status!", color=0xeee657)

    embed.add_field(name="Current status", value="Online!", inline=False)

    await ctx.send(embed=embed)

    await ctx.message.delete()

@bot.command()
async def say(ctx, *, content):
    await ctx.send(content)
    await ctx.message.delete()

@bot.command(pass_context=True)
@commands.has_role("staff")
async def channel(ctx, content):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel(content)

@bot.command()
async def hi(ctx):
    await ctx.send("Hello!")

@bot.command(name="help-all")
async def help_all(ctx):
    embed = discord.Embed(title="Help", description="A list of all commands", color=0xeee657)

    embed.add_field(name="!add X Y", value="Gives the addition of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!multiply X Y", value="Gives the multiplication of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!divide X Y", value="Gives the division of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!subtract X Y", value="Gives the subtraction of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!square X", value="Gives the square of **X** (replace X with any integer)", inline=False)
    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!info", value="Gives some info about the bot and developer", inline=False)
    embed.add_field(name="!help-all", value="Gives this message", inline=False)
    embed.add_field(name="!shop", value="Sends a link to the developers shop (helps in keeping the bot up :smile:", inline=False)
    embed.add_field(name="!invite", value="Sends a link to invite the bot to your server", inline=False)
    embed.add_field(name="!8ball", value="Ask any question nd get the real answer", inline=False)
    embed.add_field(name="!ping", value="Check the bot's ping!", inline=False)
    embed.add_field(name="!tableflip", value="(╯°□°）╯︵ ┻━┻)", inline=False)
    embed.add_field(name="!unflip", value="┬─┬ ノ( ゜-゜ノ)", inline=False)
    embed.add_field(name="!shrug", value="¯\_(ツ)_/¯", inline=False)
    embed.add_field(name="!minecraft-account", value="Get a minecraft account!", inline=False)
    embed.add_field(name="!dmall", value="DM every member of the server (use only for announcements)", inline=False)
    embed.add_field(name="!roll-dice", value="Roll a dice!", inline=False)
    embed.add_field(name="!coin-flip", value="Flip a coin!", inline=False)
    embed.add_field(name="!kick", value="kick any member from the server", inline=False)
    embed.add_field(name="!ban", value="Ban any member from the server!", inline=False)
    embed.add_field(name="!unban", value="Unban a member... he hates u tho", inline=False)
    embed.add_field(name="!status", value="Check the online status of the bot")
    embed.add_field(name="!channel", value="!channel \"name\"(creates a channel)", inline=False)
    embed.add_field(name="!pp", value="Measure your PP!")
    embed.add_field(name="!say", value="!say ok boomer (bot will send any message in the chat!)", inline=False)


    await ctx.message.delete()

    await ctx.send(embed=embed)

@bot.command(name="info")
async def info(ctx):
    embed = discord.Embed(title="MysteriousBot", description="The official MysteirousBot!", color=ctx.message.author.top_role.colour)

    embed.add_field(name="Author", value="[MK]Mysterious K#2510]")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=671365110832431115&permissions=8&scope=bot")
    embed.add_field(name="Shop", value="https://shoppy.gg/@MysteriousK")

    await ctx.message.delete()
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="A list of categories:", color=0xeee657)

    embed.add_field(name="Admin", value="A list of admin commands (\"!help-admin\" for more info)", inline=False)
    embed.add_field(name="Fun", value="A list of fun commands (\"!help-fun\" for more info)", inline=False)
    embed.add_field(name="Info", value="A list of info commands (\"!help-info\" for more info)", inline=False)
    embed.add_field(name="All", value="All the commands for the bot (\"!help-all\" for more info)", inline=False)
    embed.add_field(name="Calculator", value="A list of calculator commands (\"!help-calculator\" for more info)", inline=False)

    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command(name="help-calculator")
async def help_calculator(ctx):
    embed = discord.Embed(title="Help", description="A list of calculator commands", color=0xeee657)

    embed.add_field(name="!add X Y", value="Gives the addition of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!multiply X Y", value="Gives the multiplication of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!divide X Y", value="Gives the division of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!subtract X Y", value="Gives the subtraction of **X** and **Y** (replace X and Y with any integer)", inline=False)
    embed.add_field(name="!square X", value="Gives the square of **X** (replace X with any integer)", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command(name="help-info")
async def help_info(ctx):
    embed = discord.Embed(title="Help", description="A list of info commands", color=0xeee657)
    
    embed.add_field(name="!shop", value="Sends a link to the developers shop (helps in keeping the bot up :smile:", inline=False)
    embed.add_field(name="!invite", value="Sends a link to invite the bot to your server", inline=False)
    embed.add_field(name="!info", value="Gives some info about the bot and developer", inline=False)
    embed.add_field(name="!status", value="Tells the online status of the bot")

    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command(name="help-fun")
async def help_fun(ctx):
    embed = discord.Embed(title="Help", description="A list of fun commands", color=0xeee657)

    embed.add_field(name="!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!8ball", value="Ask any question nd get the real answer", inline=False)
    embed.add_field(name="!ping", value="Check the bot's ping!", inline=False)
    embed.add_field(name="!tableflip", value="(╯°□°）╯︵ ┻━┻)", inline=False)
    embed.add_field(name="!unflip", value="┬─┬ ノ( ゜-゜ノ)", inline=False)
    embed.add_field(name="!shrug", value="¯\_(ツ)_/¯", inline=False)
    embed.add_field(name="!minecraft-account", value="Get a minecraft account!", inline=False)
    embed.add_field(name="!roll-dice", value="Roll a dice!", inline=False)
    embed.add_field(name="!coin-flip", value="Flip a coin!", inline=False)
    embed.add_field(name="!pp", value="Measure your PP!")
    embed.add_field(name="!say", value="!say ok boomer (bot will send any message in the chat!", inline=False)

    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command(name="help-admin")
async def help_admin(ctx):
    embed = discord.Embed(title="Help", description="A list of admin commands", color=0xeee657)

    embed.add_field(name="!kick", value="kick any member from the server!", inline=False)
    embed.add_field(name="!ban", value="Ban any member from the server!", inline=False)
    embed.add_field(name="!unban", value="Unban a member... he hates u tho!", inline=False)
    embed.add_field(name="!channel", value="!channel \"name\"(creates a channel)", inline=False)
    embed.add_field(name="!dmall", value="DM every member of the server (use only for announcements)", inline=False)


    await ctx.send(embed=embed)
    await ctx.message.delete()








bot.run("NjcxMzY1MTEwODMyNDMxMTE1.XmO9HQ.wgEyHBxv--VsquC1ZsIr6mzweKo")