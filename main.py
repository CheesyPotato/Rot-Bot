import string
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
def make_rot_n(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: str.translate(s, trans)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def rot1(x):
    await bot.say(make_rot_n(1)(x))
@bot.command()
async def rot2(x):
    await bot.say(make_rot_n(2)(x))
@bot.command()
async def rot3(x):
    await bot.say(make_rot_n(3)(x))
@bot.command()
async def rot4(x):
    await bot.say(make_rot_n(4)(x))
@bot.command()
async def rot5(x):
    await bot.say(make_rot_n(5)(x))
@bot.command()
async def rot6(x):
    await bot.say(make_rot_n(6)(x))
@bot.command()
async def rot7(x):
    await bot.say(make_rot_n(7)(x))
@bot.command()
async def rot8(x):
    await bot.say(make_rot_n(8)(x))
@bot.command()
async def rot9(x):
    await bot.say(make_rot_n(9)(x))
@bot.command()
async def rot10(x):
    await bot.say(make_rot_n(10)(x))
@bot.command()
async def rot11(x):
    await bot.say(make_rot_n(11)(x))
@bot.command()
async def rot12(x):
    await bot.say(make_rot_n(12)(x))
@bot.command()
async def rot13(x):
    await bot.say(make_rot_n(13)(x))
@bot.command()
async def rot14(x):
    await bot.say(make_rot_n(14)(x))
@bot.command()
async def rot15(x):
    await bot.say(make_rot_n(15)(x))
@bot.command()
async def rot16(x):
    await bot.say(make_rot_n(16)(x))
@bot.command()
async def rot17(x):
    await bot.say(make_rot_n(17)(x))
@bot.command()
async def rot18(x):
    await bot.say(make_rot_n(18)(x))
@bot.command()
async def rot19(x):
    await bot.say(make_rot_n(19)(x))
@bot.command()
async def rot20(x):
    await bot.say(make_rot_n(20)(x))
@bot.command()
async def rot21(x):
    await bot.say(make_rot_n(21)(x))
@bot.command()
async def rot22(x):
    await bot.say(make_rot_n(22)(x))
@bot.command()
async def rot23(x):
    await bot.say(make_rot_n(23)(x))
@bot.command()
async def rot24(x):
    await bot.say(make_rot_n(24)(x))
@bot.command()
async def rot25(x):
    await bot.say(make_rot_n(25)(x))
bot.run('TOKEN')
