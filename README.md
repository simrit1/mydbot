# mydbot v0.1
[![Downloads](https://static.pepy.tech/personalized-badge/mydbot?period=total&units=international_system&left_color=green&right_color=red&left_text=Downloads)](https://pepy.tech/project/mydbot)
[![Downloads/Month](https://static.pepy.tech/personalized-badge/mydbot?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads/Month)](https://pepy.tech/project/mydbot)
## Installation

You can install released versions of mydbot from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install mydbot==0.1`<br>
<br>**Originally Tested with: Python 3.8.6**
## Something Important 
Please **Turn ON** Server Member Intents of your bot 
from the Discord Developer Portal<br>
<br>
<img align="center" alt="Turn on Member Intent" width="280px" src="https://raw.githubusercontent.com/Datavorous/datavorous.github.io/main/IMG_20210428_120207.jpg" />


## Example Usage
```python
# import the module
from mydbot import instant_bot

# initiate the object
my_bot = instant_bot(prefix="!",no_help=False,token="token_here") 
#if you pass no_help with True,the default Help Command won't work
#but it's recommended to use a custom help command of your own, because the default one is not good


# start the bot instantly!!
my_bot.start_bot()

```


<br><b>ATTENTION!</b><br>
This package depends upon four main cogs ,you can use those specifically too:<br>
<b>Install the cogs<b>

```python
pip install sbutilcog #handle utility stuffs
pip install sbfuncog #funny isn't it?
pip install sblycog #get lyrics of songs!
pip install sberrorcog #simple error handler
```
Use them: 
```python
import discord, sbutilcog, sbfuncog
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

bot.load_extension("sbutilcog")
bot.load_extension("sbfuncog")
#and just like that
@bot.command()
async def lol(ctx):
  await ctx.send("LOL")

bot.run('token')
```

<br>
<br><b>
Visit:<br></b><a href = "https://youtube.com/channel/UCzQ0-MHhoUdItckrw6DvQIA">
[YouTube]</a>
<br>
<a href="https://discord.gg/V4BtrGxMAt">
[Discord]
</a>
