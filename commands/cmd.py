import random, discord
from commands.helper import fetchContentList, fetchContent

"""Checks uwuBot's response to see if it is available"""
async def ping(ctx):
    images = fetchContentList('pong.txt')
    num = random.randint(0, len(images)-1)
    embed = discord.Embed(
        title = f'Pong!',
        color = 16251130
    ).set_image(url= images[num])
    embed.set_footer(text='@~ powered by UwUntu')
    
    await ctx.send(embed=embed)

"""Requests for a link to Anichart to see the in season running anime"""
async def anime(ctx):
    content, f = fetchContent('anichart.txt')
    embed = discord.Embed(
        title = f'Current Anime',
        url = 'https://anilist.co/search/anime/this-season',
        description = content,
        color = 6943230
    ).set_thumbnail(url = 'https://pbs.twimg.com/profile_images/1236103622636834816/5TFL-AFz_400x400.png')
    embed.set_footer(text='@~ powered by UwUntu')

    await ctx.send(embed=embed)
    f.close()

async def faq(ctx):
    desc = 'Q: Hey Bun! Maybe Someone, You and I can collab...?\n```A: BunBun only collabs with people she is very comfortable with.```\n\n'
    desc += 'Q: Bunbun! We should play this [game] together on stream!\n```A: Bunun doesn\'t really do gaming much and she much rather do just chatting with her chat and have fun that way.```\n\n'
    desc += 'Q: Hey Bunbun, can you raid [me or another streamer] because it\'s [my/their] birthday?\n```A: Happy Birthday! But Bunbun doesn\'t want to!^^```\n\n'
    desc += 'Q: Bunbun, can I talk to you through DMs?\n```A: Please Don\'t- Bunbun don\'t want to and you should respect that. If it\'s something serious, then ping her and her mod to organize a private channel to address any issues.```\n\n'
    desc += 'Q: Hey Bun! Can I ask you a question?\n```A: You just did! JK, you can ask Bunbun a question in the service area or ask the mods!```\n\n'
    desc += 'Q: Bunbun, is there a place where I can put my [music/stream/content]?\n```Yes!, There\'s a special promotion channel where you can promote yourself as a streamer, youtuber, artist, etc.```\n\n'

    embed = discord.Embed(
        title = f'Facts and Questions',
        description = desc,
        color = 6943230
    )
    embed.set_footer(text='@~ powered by UwUntu')
    await ctx.author.send(embed=embed)
    await ctx.reply(f'<@{ctx.author.id}> I\'ve forwarded the detes to your DM')