import string
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
def make_rot_n(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: str.translate(s, trans)
xrot1 = make_rot_n(1)
xrot2 = make_rot_n(2)
xrot3 = make_rot_n(3)
xrot4 = make_rot_n(4)
xrot5 = make_rot_n(5)
xrot6 = make_rot_n(6)
xrot7 = make_rot_n(7)
xrot8 = make_rot_n(8)
xrot9 = make_rot_n(9)
xrot10 = make_rot_n(10)
xrot11 = make_rot_n(11)
xrot12 = make_rot_n(12)
xrot13 = make_rot_n(13)
xrot14 = make_rot_n(14)
xrot15 = make_rot_n(15)
xrot16 = make_rot_n(16)
xrot17 = make_rot_n(17)
xrot18 = make_rot_n(18)
xrot19 = make_rot_n(19)
xrot20 = make_rot_n(20)
xrot21 = make_rot_n(21)
xrot22 = make_rot_n(22)
xrot23 = make_rot_n(23)
xrot24 = make_rot_n(24)
xrot25 = make_rot_n(25)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def rot1(x):
    await bot.say(xrot1(x))
@bot.command()
async def rot2(x):
    await bot.say(xrot2(x))
@bot.command()
async def rot3(x):
    await bot.say(xrot3(x))
@bot.command()
async def rot4(x):
    await bot.say(xrot4(x))
@bot.command()
async def rot5(x):
    await bot.say(xrot5(x))
@bot.command()
async def rot6(x):
    await bot.say(xrot6(x))
@bot.command()
async def rot7(x):
    await bot.say(xrot7(x))
@bot.command()
async def rot8(x):
    await bot.say(xrot8(x))
@bot.command()
async def rot9(x):
    await bot.say(xrot9(x))
@bot.command()
async def rot10(x):
    await bot.say(xrot10(x))
@bot.command()
async def rot11(x):
    await bot.say(xrot11(x))
@bot.command()
async def rot12(x):
    await bot.say(xrot12(x))
@bot.command()
async def rot13(x):
    await bot.say(xrot13(x))
@bot.command()
async def rot14(x):
    await bot.say(xrot14(x))
@bot.command()
async def rot15(x):
    await bot.say(xrot15(x))
@bot.command()
async def rot16(x):
    await bot.say(xrot16(x))
@bot.command()
async def rot17(x):
    await bot.say(xrot17(x))
@bot.command()
async def rot18(x):
    await bot.say(xrot18(x))
@bot.command()
async def rot19(x):
    await bot.say(xrot19(x))
@bot.command()
async def rot20(x):
    await bot.say(xrot20(x))
@bot.command()
async def rot21(x):
    await bot.say(xrot21(x))
@bot.command()
async def rot22(x):
    await bot.say(xrot22(x))
@bot.command()
async def rot23(x):
    await bot.say(xrot23(x))
@bot.command()
async def rot24(x):
    await bot.say(xrot24(x))
@bot.command()
async def rot25(x):
    await bot.say(xrot25(x))
bot.run('TOKEN')
