STATE_BUY = "BUY"
STATE_SELL = "SELL"

class FSM:
    def __init__(self):
        self.state = STATE_BUY #initialize in the BUY state because we are looking for an entry
    
    def run(self, signal): 
        
        if self.state == STATE_SELL:
            # this is where our exit strategy logic should be  #if no profit do nothing and wait  #if if we have profit => sell #if we loss too much => sell
            self.exit_position(signal)

        elif self.state == STATE_BUY: 

            if signal.status_code ==  204: #the message is empty so return
                return
            
            else:
                self.enter_position(signal) 
                
        
    def enter_position(self, signal): 
        
        #use functions from coinbase API to enter position (need a signal to buy)
        
        print(f"Buy: {signal.content.decode('utf-8')}")
        self.state = STATE_SELL 

    def exit_position(self, signal): 

        #use functions from coinbase API to liquidate position (use the signal to make sure we sell the right asset)
       
        print(f"Sell: {signal.content.decode('utf-8')}")
        self.state = STATE_BUY 

            
    






