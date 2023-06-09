English | [繁體中文](https://github.com/cycleapple/ChatGPTBot/blob/main/README_zh.md)
# ChatGPT DiscordBot

ChatGPT DiscordBot is a Python-based Discord bot that uses OpenAI's GPT-3 language model to generate responses to user messages. The bot supports two slash commands: `/chat` and `/image`.

`/chat` allows users to chat with the GPT-3 model by sending a message and receiving a response from the bot. `/image` allows users to generate an image using the DALL-E API by sending a prompt to the bot.

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment for the project: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Unix-based systems) or `venv\Scripts\activate` (Windows)
4. Install the required modules: `pip install -r requirements.txt`

## Setting up Environment Variables

To use ChatGPT DiscordBot, you need to set the following environment variables:

- `DISCORD_BOT_TOKEN`: Discord bot token. You can obtain this token from the [Discord Developer Portal](https://discord.com/developers/applications).
- `OPENAI_API_KEY`: OpenAI API key. You can obtain this key from the OpenAI API Dashboard.
- `ENABLE_IMAGE_COMMAND`: (Optional) Set this variable to `true` to enable the `/image` command. Set it to `false` or leave it unset to disable the `/image` command.

To set these environment variables, create a file named `.env` in the root directory of the project and add the following lines:

````
DISCORD_BOT_TOKEN=<your_discord_bot_token_here>
OPENAI_API_KEY=<your_openai_api_key_here>
ENABLE_IMAGE_COMMAND=<true_or_false>
````

This project use `dotenv` package to load the environment variables from the `.env` file into your code.

## Usage

To run the bot, execute the following command in your terminal while in the root directory of the project:

````
python DiscordBot.py
````


Once the bot is running, you can interact with it by typing commands in your Discord server. The bot currently supports two slash commands:

- `/chat`: Have a chat with ChatGPT. Usage: `/chat [message]`
- `/image`: Generate an image using the DALL-E API. Usage: `/image [prompt]`

## OAuth2 URL Generation
To add the bot to your Disco
rd server, you need to generate an OAuth2 URL for the bot with the following scopes and permissions:

Scopes:
- bot
- applications.commands

Permissions:

- Read Messages/View Channels
- Send Message


To generate an OAuth2 URL for the bot, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your bot application.
2. Click on the `OAuth2` tab on the left-hand menu.
3. Under the `OAuth2 URL Generator` section, check the `bot` and `applications.commands` scopes.
4. Under the `Bot Permissions` section, check the `Read Messages/View Channels` and `Send Message` permissions.
5. Copy the generated URL and paste it into your web browser.
6. Select the Discord server you want to add the bot to and authorize the bot.
7. The bot should now be added to your server and ready to use.