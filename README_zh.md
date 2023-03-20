[English](https://github.com/cycleapple/ChatGPTBot) | 繁體中文
## ChatGPT DiscordBot
ChatGPT DiscordBot 是一個使用 OpenAI 的 GPT-3 語言模型來產生使用者訊息回覆的 Python Discord 機器人。此機器人支援兩種斜線指令：`/chat` 與 `/image`。

`/chat` 允許使用者與 GPT-3 模型對話，並從機器人接收回覆。`/image` 允許使用者使用 DALL-E API 生成圖片，並透過向機器人發送提示來進行操作。

## 安裝
1. 複製此存儲庫到您的本機。
2. 為此專案建立一個虛擬環境：`python3 -m venv venv`
3. 啟用虛擬環境：`source venv/bin/activate`（Unix 系統）或 `venv\Scripts\activate`（Windows）
4. 安裝所需的模組：`pip install -r requirements.txt`

## 設置環境變數
要使用 ChatGPT DiscordBot，您需要設置以下環境變數：

- `DISCORD_BOT_TOKEN`：Discord 機器人Token。您可以從 [Discord Developer Portal](https://discord.com/developers/applications) 取得Token。
- `OPENAI_API_KEY`：OpenAI API 金鑰。您可以從 OpenAI API 儀表板獲取此金鑰。
- `ENABLE_IMAGE_COMMAND`：（可選）將此變數設置為 true 以啟用 /image 指令。將其設置為 false 或不設置以禁用 /image 指令。
要設置這些環境變數，請在專案的根目錄中創建一個名為 .env 的文件，並添加以下行：

````
DISCORD_BOT_TOKEN=<your_discord_bot_token_here>
OPENAI_API_KEY=<your_openai_api_key_here>
ENABLE_IMAGE_COMMAND=<true_or_false>
````
您可以使用 dotenv 包將環境變數從 .env 文件加載到您的代碼中。

## 使用方法
要運行機器人，在專案的根目錄中執行以下命令：

````
python DiscordBot.py
````

一旦機器人運行起來，您就可以在 Discord 伺服器中輸入指令與之交互了。目前，機器人支援兩種斜線指令：

- `/chat`：與 ChatGPT 對話。用法：/chat [message]
- `/image`：使用 DALL-E API 生成圖片。