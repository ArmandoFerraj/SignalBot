# from CoinbaseFunctions import initialize_coinbase, get_unit, get_current_holdings, coinbase_buy, coinbase_sell
# initialize_coinbase()

STATE_BUY = "BUY"
STATE_SELL = "SELL"

class FSM:
    def __init__(self):
        self.state = STATE_BUY #initialize in the BUY state because we are looking for an entry
    
    def run(self, signal): 
        
        if self.state == STATE_SELL:
            # this is where our exit strategy logic should be  #if no profit do nothing  #if too much loss or if we have profit => sell
            self.exit_position(signal)

        elif self.state == STATE_BUY: 

            if signal == {} or signal.status_code ==  204:
                return
            
            else:
                self.enter_position(signal) 
                
        
    def enter_position(self, signal): 
        """
        - This function takes in the the trading signal dictionary as input and enters the trade 


        
        - run get_unit() -- determines how much we put down on the trade
        - pass the signal and the unit into coinbase_buy -- enters the trade
        - conbase_buy should return something like successful purchase or an error
        - if that return is a succesful purchase then we switch state

        # unit = get_unit(initialize_coinbase())
        # coinbase_buy(signal, unit) 
        """
        
        print(f"Buy: {signal.content.decode('utf-8')}")
        self.state = STATE_SELL 

    def exit_position(self, signal): 
        """
        - takes in the trading signal as input. 
        - run get_current_holdings
        - pass the trading and holdings into coinbase_sell() to liquidate position
        - if succesful then switch state
        - if not succesful we have a problem and we need to think about how to handle. we do not want to be stuck in an open position indefinitely and we dont want to switch back to buy if it is stil open.

        # holdings = get_current_holdings(initialize_coinbase(), signal)
        # coinbase_sell(signal, holdings)
        # signal = None
        #should return successful or not 
        #if success then signal = None
        """
        
        print(f"Sell: {signal.content.decode('utf-8')}")
        self.state = STATE_BUY 

            
    






