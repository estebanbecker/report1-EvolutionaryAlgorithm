import random
import time
import matplotlib.pyplot as plt 
import numpy as np 

random.seed(time.time())

def unfair_coin_flip(n, p):
    coin = []
    for i in range(n):
        if random.random() < p:
            coin.append(0)
        else:
            coin.append(1)
    return coin

#Flip 30 times a coin
coin1 = [random.randint(0,1) for i in range(30)]

#Flip 30 times an unfair coins (25/75),(10/90),(45/55),(52/48)
coin2 = unfair_coin_flip(30, p=0.75)
coin3 = unfair_coin_flip(30, p=0.9)
coin4 = unfair_coin_flip(30, p=0.55)
coin5 = unfair_coin_flip(30, p=0.48)

fig1 = plt.figure()
fig1.suptitle('Fair Coin Flip')
plt.boxplot(coin1)
plt.show()

fig2 = plt.figure()
fig2.suptitle('Unfair Coin Flip (25/75)')
plt.boxplot(coin2)
plt.show()

fig3 = plt.figure()
fig3.suptitle('Unfair Coin Flip (45/55)')
plt.boxplot(coin4)
plt.show()
