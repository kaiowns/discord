import discord from discord.ext import commands import asyncio

# DISCLAIMER: This is a self-bot, using one is against Discord TOS. Use at your own risk.

TOKEN = "your-token-here"  # Replace with your Discord account token. DELETE_DELAY = 10  # Time in seconds before messages are deleted.

intents = discord.Intents.default() intents.messages = True client = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@client.event async def on_ready(): print(f"Logged in as {client.user}")  # Confirmation that the bot is active.

@client.event async def on_message(message): if message.author.id != client.user.id: return  # Ignore messages from other users.

try:
    await asyncio.sleep(DELETE_DELAY)  # Wait for the specified delay.
    await message.delete()  # Delete the message.
    print(f"Deleted message: {message.content}")
except Exception as e:
    print(f"Failed to delete message: {e}")  # Error handling.

client.run(TOKEN, bot=False)  # Running the self-bot

