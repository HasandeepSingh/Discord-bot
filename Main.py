import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="Your Prefix Here", intents=discord.Intents.all)

Token = "Your Token Here"

@bot.event
async def on_ready():
  print("Bot is Online and all commands are working properly")

@bot.command()
async def hello(ctx):
  await ctx.send("Hello")

bot.run(Token)
