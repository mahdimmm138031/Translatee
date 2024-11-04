import googletrans
import discord
import os
import webserver

Discord_token = os.environ['discordkey']

def translate_text(input_text, target_language='en'):
    translator = googletrans.Translator()
    translated = translator.translate(input_text, dest=target_language)
    return translated.text

# Get user input
class Client(discord.Client):

    async def on_message(self, message):
        if message.content.startswith('-en'):
            target_lang = 'en' 
            user_input = message.content[4:]
            translated_text = translate_text(user_input, target_lang)
            await message.channel.send(translated_text, reference=message)
        elif message.content.startswith('-ch'):
            target_lang = 'zh-cn' 
            user_input = message.content[4:]
            translated_text = translate_text(user_input, target_lang)
            await message.channel.send(translated_text, reference=message)

intents = discord.Intents.default()
intents.message_content = True

webserver.keep_alive()

client = Client(intents=intents)
client.run(Discord_token)
