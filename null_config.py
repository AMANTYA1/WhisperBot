import os

#Why coder's say I am Null
# Config Vars
NULLAPI_HASH = "4af0dda44fd0209249bb9a482690506c"
NULLAPI_KEY = 9197144
NULLBOT_NAME = os.environ.get("BOT_NAME", None) # Your bot name, example: Null Bot
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Your bot username with (@), example: @WhisperNRobot
NULL_TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

# Config Text
START_TEXT = f"**Heya,there I am a {NULLBOT_NAME}!**\n\nType /help to see how to use me!\nType /repo to deploy your own bot like {NULLBOT_NAME}.\n Powered by [BotDuniya](https://t.me/BotDuniyaXD)"

HELP_TEXT = f"**• How to use {NULLBOT_NAME}:**\n\nClick the button below or\n\nType __{BOT_USERNAME} wspr <username> | <text>__\nExample: `{BOT_USERNAME} wspr @Shubhanshutya | Hello!`\nEssay sir"

REPO_TEXT = f"Click the button below to deploy bot like {NULLBOT_NAME} Thankyou"
