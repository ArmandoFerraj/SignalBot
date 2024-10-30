
dependent libraries:
- discord.py
- httpx
- fastapi
- uvicorn

project architecture:
- DiscordBot sends messages to the server using FAST API
- the server processes the message and stores the signal
- main sends requests to the server and runs the trading bot
