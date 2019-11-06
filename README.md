<h1 align="center">@Sticker2PictureBot</h1>
<p align="center">
  <a href="http://t.me/sticker2picturebot"><em>http://t.me/sticker2picturebot</em></a>
</p>
<br>

## About

Ever wanted to send Telegram stickers as pictures to other chats? Now you can!

This is a Telegram Bot based on python-telegram-bot. You send it a sticker and it will reply you with the sticker converted into a PNG. How handy?!


## Setup and Deployment

- Clone the repo.
- Create Python VirtualEnv.
```bash
python3 -m venv .env
source .env/bin/activate
```
- Install required dependencies.
```bash
pip install -r requirements.txt
```
- Create a `config.py` in `/src/`.
```python
# Telegram Bot API Token
tg_bot_token = "YOUR-TG-BOT-API-TOKEN-HERE"
```
- Run it!
```bash
# Run locally...
python bot.py

# Run in prod...
./run_prod.sh
```