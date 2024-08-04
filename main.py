from StateMachine import FSM
import requests

url = 'http://localhost:8000/getmessage/'
SIGNALBOT = FSM()

while True:

    if SIGNALBOT.state == "BUY":
        signal = requests.get(url) #grabs signal from the server 

    SIGNALBOT.run(signal) 
    
        
   
