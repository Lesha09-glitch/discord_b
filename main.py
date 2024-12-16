import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

token = "MTMxMDU4MTYwNTgxMDgzMTQzMA.GL33zO.3V3b4Lw2JPS2yvAQ2n5fVbxlnzYL0CxUhqBD0M"
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
url_hook = "https://discord.com/api/webhooks/1315654589680189440/gWENhA0qKdfrhOGmAZtGPpq-sF0OsxdYGNW3-sUViVGWgwHZaUzbGkxfnlnEsdpuqyDD"

text_message = "!!!Самая крутая новость!!!"

embed = DiscordEmbed(title = "!Новости!", description = "Вышла новая игра!!!", url = "https://www.youtube.com", color = "8B0000")

hook = DiscordWebhook(url=url_hook, content=text_message, username="WebHook")
hook.add_embed(embed)
hook.execute()


@bot.event
async def on_ready():
    print("Я готов!")

@bot.command()
async def help2(hel, *, word=None):
    await hel.send("Добро пожаловать на сервер")
    if word is not None:
        if "пушкин" in word.lower():
            await hel.send("Вот список книг Пушкина->")

@bot.event
async def on_message(mes):
    if mes.author.bot:
        print(mes.author.bot)
        return
    if "привет" in mes.content.lower():
        await mes.channel.send(f"Привет {mes.author}")
    await mes.channel.send("Что хотите сделать?")





    














bot.run(token)