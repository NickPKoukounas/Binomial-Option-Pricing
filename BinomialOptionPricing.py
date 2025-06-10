import numpy as np
import math

#American and European Call with Dividend = 0 are equivalent
def Euro_Call(r, D, volatility, S0, K, T, n): #Regular Binomial tree pricing
    dt = T/n
    u = np.exp(volatility*np.sqrt(dt))
    d = 1/u
    p = (np.exp((r-D)*dt) - d)/(u-d)
    q = 1-p
    Values = []

    for j in range(n+1):
        val = (math.comb(n, j)*(p**j)*(q**(n-j))) * max(S0*(u**j)*(d**(n-j)) - K, 0)
        Values.append(val)

    
    return np.exp(-(r)*n*dt) * sum(Values)


def Euro_Put(r, D, volatility, S0, K, T, n):
    dt = T/n
    u = np.exp(volatility*np.sqrt(dt))
    d = 1/u
    p = (np.exp((r-D)*dt) - d)/(u-d)
    q = 1-p
    Values = []
    
    for j in range(n+1):
        val = (math.comb(n, j)*(p**j)*(q**(n-j))) * max(K-S0*(u**j)*(d**(n-j)), 0)
        Values.append(val)
    
    return np.exp(-(r)*n*dt) * sum(Values)


def American_Put(r, D, volatility, S0, K, T, n):
    dt = T/n
    u = np.exp(volatility*np.sqrt(dt))
    d = 1 / u
    p = (np.exp((r-D)*dt)-d)/(u-d)
    discount = np.exp(-r*dt)

    prices = [S0*(u**j)*(d**(n-j)) for j in range(n + 1)]

    option_values = [max(K-price, 0) for price in prices]

    for i in range(n-1, -1, -1):
        for j in range(i+1):
            stock_price = S0*(u**j)*(d**(i-j))
            continuation = discount*(p*option_values[j + 1] + (1 - p)*option_values[j])
            exercise = max(K-stock_price, 0)
            option_values[j] = max(continuation, exercise)

    return option_values[0]


def American_Pall(r, D, volatility, S0, K, T, n):
    dt = T/n
    u = np.exp(volatility*np.sqrt(dt))
    d = 1 / u
    p = (np.exp((r-D)*dt)-d)/(u-d)
    discount = np.exp(-r*dt)

    prices = [S0*(u**j)*(d**(n-j)) for j in range(n+1)]

    option_values = [max(price-K, 0) for price in prices]

    for i in range(n-1, -1, -1):
        for j in range(i+1):
            stock_price = S0*(u**j)*(d**(i-j))
            continuation = discount*(p*option_values[j + 1] + (1 - p)*option_values[j])
            exercise = max(stock_price-K, 0)
            option_values[j] = max(continuation, exercise)

    return option_values[0]
