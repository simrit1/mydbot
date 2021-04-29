import discord
import Utility,Lyrics,Fun2,Error
import asyncio,ModCog,FunCog
from discord.ext import commands


class instant_bot:
  def __init__(self,prefix,no_help:bool,token):
    self.prefix = prefix
    self.no_help = no_help
    self.token = token
  def start_bot(self):
    intents = discord.Intents.default() 
    intents.members = True  
    bot = commands.Bot(command_prefix=self.prefix,intents=intents)
    if self.no_help:
      bot.remove_command('help')
    
    bot.load_extension("sbutilcog")
    bot.load_extension("ModCog")
    bot.load_extension("FunCog")
    bot.load_extension("Lyrics")
    bot.load_extension("sbfuncog")
    bot.load_extension("Error")
    
    bot.run(self.token)



  
