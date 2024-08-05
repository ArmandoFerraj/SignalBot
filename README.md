dependent libraries:
- discord.py
- httpx
- fastapi
- uvicorn

project architecture:
- DiscordBot.py listens to messages in a specific discord channel and POST those messages to the server using FAST API
- server.py takes the incoming message, proccesses it into a trading signal, and then stores the signal in a list
- main.py sends GET requests to the server for trading signals, then inputs the signal into the trading bot
