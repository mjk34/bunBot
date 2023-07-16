import os, random, discord

from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext

from commands.cmd import ping, anime
from commands.gpt import gpt_string

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = int(os.getenv('GUILD_ID'))

CHANNEL = int(os.getenv('BOT_CMD'))

client = Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

"""Start up bot status message on boot"""
@client.event
async def on_ready(): await client.change_presence(activity=discord.Game('/uwu for fortune!'))

"""Filter message based on author and occasionally 'uwuify' read message"""
@client.event
async def on_message(message):
    if message.author == client.user: return                # checks if professor

    if message.channel.id == CHANNEL:
        content = message.content
        temp_msg = ['Typing...', 'Ummm...', 'Hmmm...', 'Thinking...']
        msg = random.randint(0, 3)

        ping = '<@1128015416837558372>'
        token = 'hey bunbot'
        if ping in content:
                # add in prompt detection

                # this is the else if no prompts are detected
                reply = await message.reply(f'{temp_msg[msg]}')
                gpt_str = await gpt_string('', content[len(token):])
                await reply.edit(content=gpt_str)
                return
        
        if token in content.lower():
            reply = await message.reply(f'{temp_msg[msg]}')
            gpt_str = await gpt_string('', content[len(token):])
            await reply.edit(content=gpt_str)
            return
        
        try:
            m_id = message.reference.message_id
            m_cid = message.reference.channel_id
            r_message = await client.get_channel(m_cid).fetch_message(m_id)

            m_aname = r_message.author.name
            m_context = r_message.content

            if m_aname == 'BunBot':
                reply = await message.reply(f'{temp_msg[msg]}')
                gpt_str = await gpt_string(m_context, content)
                await reply.edit(content=gpt_str)
                return
        except:
            return

"""Non-Blockchain dependent commands"""
@slash.slash(name='ping', description="Ping BunBot", guild_ids=[GUILD_ID])
async def _(ctx:SlashContext): await ping(ctx)

@slash.slash(name='anime', description="Check AniList for Simulcast shows", guild_ids=[GUILD_ID])
async def _(ctx:SlashContext): await anime(ctx)

client.run(TOKEN)