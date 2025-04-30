import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats
import bisect
import time 
import pandas as pd

print("hello world")


zero_k = np.loadtxt('zero_k.csv', delimiter=',', skiprows=1)
ten_k = np.loadtxt('ten_k.csv', delimiter=',', skiprows=1)
twenty_k = np.loadtxt('twenty_k.csv', delimiter=',', skiprows=1)
thirty_k = np.loadtxt('thirty_k.csv', delimiter=',', skiprows=1)
hundred_k = np.loadtxt('hundred_k.csv', delimiter=',', skiprows=1)
five_hundred_k = np.loadtxt('five_hundred_k.csv', delimiter=',', skiprows=1)

zero_k_no_partial = np.loadtxt('zero_k_no_partial.csv', delimiter=',', skiprows=1)
ten_k_no_partial = np.loadtxt('ten_k_no_partial.csv', delimiter=',', skiprows=1)
twenty_k_no_partial = np.loadtxt('twenty_k_no_partial.csv', delimiter=',', skiprows=1)
thirty_k_no_partial = np.loadtxt('thirty_k_no_partial.csv', delimiter=',', skiprows=1)
hundred_k_no_partial = np.loadtxt('hundred_k_no_partial.csv', delimiter=',', skiprows=1)
five_hundred_k_no_partial = np.loadtxt('five_hundred_k_no_partial.csv', delimiter=',', skiprows=1)

print(np.mean(zero_k))
print(np.mean(ten_k))
print(np.mean(twenty_k))
print(np.mean(thirty_k))
print(np.mean(hundred_k))
print(np.mean(five_hundred_k))

y_axis = np.array([np.mean(zero_k), np.mean(ten_k), np.mean(twenty_k), np.mean(thirty_k), np.mean(hundred_k), np.mean(five_hundred_k)])
x_axis = np.array([0, 10000, 20000, 30000, 100000, 500000])

plt.plot(x_axis, y_axis,
        linestyle='-',     
        marker='o', 
        markersize=6,
        markerfacecolor='blue', 
        markeredgecolor='black',
        markeredgewidth=1)

plt.xlabel("Number of bills pre-removed", fontsize=16)
plt.ylabel("Expected # of Bills Drawn Before Match", fontsize=16) 
plt.title("C vs K", fontsize=20)
plt.grid()
plt.show()


plt.hist(zero_k, bins=50, alpha=0.5, label='0k')
plt.hist(ten_k, bins=50, alpha=0.5, label='10k')
# plt.hist(twenty_k, bins=50, alpha=0.5, label='20k')
plt.hist(thirty_k, bins=50, alpha=0.5, label='30k')
plt.hist(hundred_k, bins=50, alpha=0.5, label='100k')
plt.hist(five_hundred_k, bins=50, alpha=0.5, label='500k')
plt.xlabel("Number of Bills Drawn Before Match", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.title("C vs K Histogram", fontsize=20)
plt.legend()
plt.grid()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()


plt.hist(zero_k_no_partial, bins=50, alpha=0.5, label='0k')
plt.hist(ten_k_no_partial, bins=50, alpha=0.5, label='10k')
# plt.hist(twenty_k_no_partial, bins=50, alpha=0.5, label='20k')
plt.hist(thirty_k_no_partial, bins=50, alpha=0.5, label='30k')
plt.hist(hundred_k_no_partial, bins=50, alpha=0.5, label='100k')
plt.hist(five_hundred_k_no_partial, bins=50, alpha=0.5, label='500k')
plt.xlabel("Number of Bills Drawn Before Match", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.title("C vs K without partials Histogram", fontsize=20)
plt.legend()
plt.grid()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()