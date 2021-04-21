$ ry -3 -m pip install -u discord.py[voice]

import discord

# TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxx.yyyyyy.zzzzzzzzzzzzzzzzzzzzzzzzzzz'


discord.Object(id)

	a == '1'
	b == '2'
	c == '3'
	d == '4'
	e == '5'
	name == ''
	dam == ''

global_with_embed.py
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return

    GLOBAL_CH_NAME = "進行発言チャンネル" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client.get_all_channels()


        embed = discord.Embed(title="進行発言チャンネル",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 

        embed.set_footer(text=f"{name} / {a} / {dam}",
            
	 embed.set_footer(text=f"{name} / {b} / {dam}",

	embed.set_footer(text=f"{name} / {c} / {dam}",

	embed.set_footer(text=f"{name} / {d} / {dam}",

	embed.set_footer(text=f"{name} / {e} / {dam}",
           
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
	returm

client.run(token)


