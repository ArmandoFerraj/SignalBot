import random

balance = 1000 # total account balance
steps = 365 # number of trades
win_rate = .85 # probability of winning the trade
unit = 1 #percentage of ur balance you are gambling with


def random_step(win_rate):
    if random.random() < win_rate:
        result = 3 # how much profit to take
    else:
        result = -20 # stop loss 
    return result

def trading_sim(num_trades, win_rate, balance, risk):
     for i in range(num_trades):
        roi = ((random_step(win_rate) / 100)) # roi ----> ie how much money you won off of the trade or how much you loss off the trade as a percentage
        balance = balance + balance*roi*risk # add or subtract the roi to the current balance
        i = i + 1
        # print(balance)
     return balance

"""
the code below will run the strategy 10000 times and return the average
"""

simulations = 10000
results = []
for z in range(simulations):
    results.append(trading_sim(num_trades=steps, win_rate=win_rate, balance=balance, risk=unit))

avg_sim = sum(results)/len(results)
print(avg_sim)

