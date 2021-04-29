# dbotpy v0.1

## Installation

You can install released versions of TrinityD from the Python Package Index with pip or a similar tool:

**Stable Release:** `pip install dbotpy`<br>
<br>**Originally Tested with: Python 3.8.6**
## Something Important 
Please **Turn ON** Server Member Intents of your bot 
from the <font color="violet">Discord Developer Portal<br>
<br></font>
<img align="center" alt="Turn on Member Intent" width="280px" src="https://raw.githubusercontent.com/Datavorous/datavorous.github.io/main/IMG_20210428_120207.jpg" />


## Example Usage
```python
# import the module
from dbotpy import instant_bot

# initiate the object
my_bot = instant_bot(prefix="!",no_help=False,token="token_here") 
#if you pass no_help with True,the default Help Command won't work
#but it's recommended to use a custom help command of your own, because the default one is not good


# start the bot instantly!!
my_bot.start_bot()

```

## Use any specific cog with your discord bot
```python
# import the cogs
from dbotpy import Utility,Fun2, Lyrics,Error
import discord
from discord.ext import commands

#as simple as that
client = commands.Bot(command_prefix='!')

client.load_extension("Utility")
client.load_extension("Fun2")
client.load_extension("Lyrics")
client.load_extension("Error")
#done loading cogs!
@client.command()
async def ping(ctx):
    await ctx.send('pong')
#any extra commands of your choice(make a new help command pls)
client.run('token_here')
#run your bot!!
```

<br>
<br><b>
Visit:<br></b><a href = "https://youtube.com/channel/UCzQ0-MHhoUdItckrw6DvQIA">
[YouTube]</a>
<br>
<a href="https://discord.gg/V4BtrGxMAt">
[Discord]
</a>
