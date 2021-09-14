import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)
dash = '-' * 40
@client.event
async def on_ready():
    
    bot_channel = client.get_channel(781144966705053698) #Bot Channel
    await bot_channel.send(dash)
    await bot_channel.send("**Dango Bot Online!**")

@client.command()
async def Ah(ctx):
    await ctx.channel.send("Chu!")

@client.command()
async def scramble(ctx):
    channel = client.get_channel(615779508724826123)                    #Elite Lounge
    members = channel.members                                           #getting a list of all members in channel
    '''
    await ctx.channel.send("**The following are in Elite Lounge: **")
    for x in members:                                                   
        await ctx.channel.send(x)
    '''
    random.shuffle(members)                #randomizes the list of members

    # Creates a Team 1 and Team 2 list of members' names (T1 consisting of first half of random list; T2 second half)
    t1 = "".join([":blue_circle: " + "\t" + member.name + '\n' for member in members[:len(members)//2]])
    t2 = "".join([":red_circle: " + "\t" + member.name + '\n' for member in members[len(members)//2:]])

    # Creates final string where the BOT will send all teams in one Discord message
    final_str = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(dash, "**              TEAM 1** (Left Side)", dash, t1, dash, "**              TEAM 2** (Right Side)", dash, t2)
    await ctx.channel.send(final_str)


client.run("NzgxMTM4MDMxNDU3NDY4NDE2.X75Rew.I2Q8Y6FWJUitp2onL6J3lQYc_9U")