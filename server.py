import uvicorn
from fastapi import FastAPI, HTTPException, Request
from typing import List
from helper import process_message

app = FastAPI()
signal_list: List[dict] = []

@app.post("/postmessage/")
async def from_discord(request: Request):
    message = await request.body()
    message = message.decode('utf-8') # Read the request body as a raw string
    signal = process_message(message)   # turn the string message into a trading signal 
    signal_list.append(signal)
    print(signal_list)


@app.get("/getmessage/")
async def to_signalbot():
    if len(signal_list) == 0:
        raise HTTPException(status_code=204, detail="No trading signals")
    else:
        current_message = signal_list.pop(0) #send the first signal in the list to the trading bot
        return current_message

def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    start_server()