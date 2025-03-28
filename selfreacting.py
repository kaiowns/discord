import discord from discord.ext import commands import re

# DISCLAIMER: This is a self-bot, meaning it runs on a user account and it's against Discord TOS. Use at your own discretion.

TOKEN = "token"  # Replace this with your actual Discord account token.

# Intents

intents = discord.Intents.default() intents.messages = True

# Bot instance

client = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@client.event async def on_ready(): print(f"Logged in as {client.user}")  # Just a simple confirmation that the bot is running.

@client.event async def on_message(message): if message.author.id != client.user.id: return  # This ensures the bot only reacts to messages sent by YOU.

# Extract all emojis from the message (including custom server emojis and Unicode emojis).
emojis = re.findall(r"<a?:\w+:\d+>|[\U00010000-\U0010ffff]", message.content)

for emoji in emojis:
    try:
        await message.add_reaction(emoji)  # Adding the extracted emojis as reactions.
    except Exception as e:
        print(f"Failed to react with {emoji}: {e}")  # If something goes wrong, print the error.

# Running the self-bot.

client.run(TOKEN, bot=False)

