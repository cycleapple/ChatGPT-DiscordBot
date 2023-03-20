import os
import discord
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')
enable_image_command = os.getenv('ENABLE_IMAGE_COMMAND', '').lower() == 'true'

openai.api_key = openai_api_key


def generate_image(prompt):
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai_api_key}",
        },
        json={
            "model": "image-alpha-001",
            "prompt": prompt,
            "num_images": 1,
            "size": "1024x1024",
            "response_format": "url",
        },
    )
    if response.status_code == 200:
        return response.json()["data"][0]["url"]
    else:
        return None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


async def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2560,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


@bot.slash_command(name='chat', description="Have a chat with ChatGPT")
async def gpt_command(ctx, *, message):
    author = ctx.author.id
    await ctx.defer()  # defer the interaction to acknowledge it
    response_text = await generate_response(message)
    await ctx.followup.send(
        f'> **{message}** - <@{str(author)}> {response_text}')  # send the follow-up message to the channel


if enable_image_command:
    @bot.slash_command(name='image', description="Generate an image using DALL-E API")
    async def generate_image_command(ctx, *, prompt):
        author = ctx.author.id
        await ctx.defer()  # defer the interaction to acknowledge it
        image_url = generate_image(prompt)
        if image_url:
            await ctx.followup.send(f'> **{prompt}** - <@{str(author)}>\n{image_url}')
        else:
            await ctx.followup.send(f'> **{prompt}** - <@{str(author)}> Unable to generate an image.')

if __name__ == '__main__':
    bot.run(discord_bot_token)