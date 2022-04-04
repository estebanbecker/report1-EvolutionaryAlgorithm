import random
import time
import matplotlib.pyplot as plt 
import numpy as np 

random.seed(time.time())

def unfair_coin_flip(p):
    coin_list = []
    for i in range(30):
        coin=0
        for j in range(50):
            if random.random() < p:
                coin += 1
        coin_list.append(coin)
    return coin_list

#Flip 30 times a coin
coin1 = unfair_coin_flip(p=0.5)

#Flip 30 times an unfair coins (25/75),(10/90),(45/55),(52/48)
coin2 = unfair_coin_flip(p=0.75)
coin3 = unfair_coin_flip(p=0.9)
coin4 = unfair_coin_flip(p=0.55)
coin5 = unfair_coin_flip(p=0.48)

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
