dependent libraries:
- discord.py
- httpx
- fastapi
- uvicorn

project architecture:
- DiscordBot.py listens to messages in a discord channel and posts them to the server using FAST API
- server.py takes the incoming message, proccesses it, and then stores the signal in a list
- main.py sends requests to the server for trading signals, then inputs the signal into the trading bot
