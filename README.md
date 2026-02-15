# Telegram Spam Detection Bot

This bot detects whether a given text (e.g., from email) is spam.
**Setup Instructions**
1. Create a bot in Telegram
  - Talk to @BotFather and create a new bot.
2. Copy the API token.
3. Add API token
4. Open bot/API.txt and paste your API token there.
5.Train the model
  - Run the training script:
    `python3 model/train_model.py`
  - Wait approximately 1 minute for the training to complete.
6. Run the bot GUI
  - Start the bot interface with:
    `python3 bot/bot_gui.py`
