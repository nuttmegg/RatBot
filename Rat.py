import discord
from discord import embeds
from discord.ext import commands
import random
import datetime
time = datetime.datetime.now()
import os

client = discord.Client
bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name =f"{bot.command_prefix}help"))
    print(discord.__version__)

#=========================================================
class Sussy(commands.Cog):
    def __init__(self):
        self.bot = bot
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(
        color=discord.Color.dark_red(), 
        title="**Rat Bot**",
        description="")
        embed.set_footer(
          text=f"requested by"
          )
        embed.set_thumbnail(
          url="https://cdn.discordapp.com/attachments/500716923319877632/874145182952587314/prof1.png"
          )
        for page in self.paginator.pages:
            embed.description=f"{page}"
        await destination.send(embed=embed)

bot.help_command = MyHelpCommand()
#=========================================================
@bot.command(aliases=["av"], description="Shows the avatar of the author")
async def avatar(ctx):
  embed=discord.Embed(
    title="**Avatar**",
    color=discord.Colour.dark_red())
  embed.set_author(
    name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  embed.set_footer(
    text=f"Requested by {ctx.author}")
  embed.set_image(
    url=ctx.author.avatar_url)
  await ctx.send(embed=embed)
  print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command(aliases=["pic", "ratpic"])
async def rat(ctx):
    picture = {
                1:('https://cdn.discordapp.com/attachments/500716923319877632/874133307208638474/9k.png'),
                2:('https://cdn.discordapp.com/attachments/500716923319877632/874133352989474846/2Q.png'),
                3:('https://cdn.discordapp.com/attachments/500716923319877632/874133378344050708/images.png'),
                4:('https://cdn.discordapp.com/attachments/500716923319877632/874133466399260702/images.png'),
                5:('https://cdn.discordapp.com/attachments/500716923319877632/874133531016716348/images.png'),
                6:('https://cdn.discordapp.com/attachments/500716923319877632/874133700353343528/images.png'),
                7:('https://cdn.discordapp.com/attachments/500716923319877632/874133766422024192/images.png'),
                8:('https://cdn.discordapp.com/attachments/500716923319877632/874133964443492433/images.png'),
                9:('https://cdn.discordapp.com/attachments/500716923319877632/874134012619284520/images.png'),
                10:('https://cdn.discordapp.com/attachments/500716923319877632/874134111218991154/images.png'),
                11:('https://cdn.discordapp.com/attachments/500716923319877632/874134684769091594/images.png'),
                12:('https://cdn.discordapp.com/attachments/500716923319877632/874134885617508392/images.png'),
                13:('https://cdn.discordapp.com/attachments/500716923319877632/874135067201515632/images.png'),
            }
    rand = random.randint(1, 13)
    embed = discord.Embed(
    title="**Here's a rat picture for you.**",
    description="",
    color=discord.Colour.dark_red())
    embed.set_footer(
        text=f"Requested by {ctx.author}")
    embed.set_image(
      url= (f'{picture[rand]}')
    )
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')

bot.run(os.environ['Token'])