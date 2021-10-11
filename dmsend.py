import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다(24시간 온라인).")
    game = discord.Game('~하는 중')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 656447086455291925:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="사운즈")
                        embed.add_field(name="name", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/cxBFZqU2xc")
                        await i.send(embed=embed)
                except:
                    pass


client.run('ODk1MjIzOTQzNDYyNTM5MjY1.YV1cRA.bkz9Is-PYLYdgjrkHu95rZJbmMQ')