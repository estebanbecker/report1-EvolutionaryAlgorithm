import random
import time
import matplotlib.pyplot as plt 
import numpy as np
import scikit_posthocs as sp
from scipy import stats

random.seed(time.time())

def unfair_coin_flip(p):
    coin_list = []
    for i in range(30):
        coin=0
        for j in range(50):
            if random.random() < p:
                coin += 1
        coin_list.append(coin/50)
    return coin_list

#Flip a coin
coin1 = unfair_coin_flip(p=0.5)

#Flip unfair coins
coin2 = unfair_coin_flip(p=0.75)
coin3 = unfair_coin_flip(p=0.9)
coin4 = unfair_coin_flip(p=0.55)
coin5 = unfair_coin_flip(p=0.48)

fig1 = plt.figure()
fig1.suptitle('Fair Coin Flip')
plt.boxplot(coin1)
plt.show()

fig2 = plt.figure()
fig2.suptitle('Unfair Coin Flip (75/25)')
plt.boxplot(coin2)
plt.show()

fig3 = plt.figure()
fig3.suptitle('Unfair Coin Flip (55/45)')
plt.boxplot(coin4)
plt.show()

print(sp.posthoc_dunn([coin1, coin2, coin3, coin4, coin5], p_adjust='holm'))