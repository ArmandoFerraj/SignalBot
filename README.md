dependent libraries:
- discord.py
- httpx
- fastapi
- uvicorn

The project uses a micro services architecture:
- DiscordBot.py uses the discord library to listen to messages from a specific channel and POST those messages to our server using FAST API
- server.py takes the incoming message, proccesses it, and then stores the trading signal in a list
- main.py sends GET requests to the server looking for trading signals, then feeds the signal into our state machine ie the trading bot
