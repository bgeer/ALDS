from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats

waysone = 0
waystwo = 0

#Schrijf hier je code voor opgave 4. We hebben al een beginnetje voor je gemaakt, met de base cases:
def ways2pay( amount, highest_coupon_number=13, coupons=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]):
    global waysone
    waysone = waysone + 1
    if(amount == 0): # hij komt precies uit, één manier gevonden
        return 1
    elif(amount < 0): # oeps, teveel afgetrokken, deze manier kon niet
        return 0
    elif(highest_coupon_number==1): #als er nog alleen 1-centjes over zijn kan het maar op 1 manier
        return 1
    return ways2pay(amount, highest_coupon_number-1, coupons) + ways2pay(amount-coupons[highest_coupon_number-1], highest_coupon_number, coupons)

def ways2pay2( amount, highest_coupon_number=13, coupons=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000], table=[]):
    global waystwo
    waystwo = waystwo + 1
    if not table:
        table = [[-1 for j in range(amount+1)] for i in range(highest_coupon_number+1)]
    if(amount == 0): # hij komt precies uit, één manier gevonden
        return 1
    elif(amount < 0): # oeps, teveel afgetrokken, deze manier kon niet
        return 0
    elif(highest_coupon_number==1): #als er nog alleen 1-centjes over zijn kan het maar op 1 manier
        return 1
    elif table[highest_coupon_number][amount] == -1:
        table[highest_coupon_number][amount] = ways2pay2(amount, highest_coupon_number-1, coupons, table) + ways2pay2(amount-coupons[highest_coupon_number-1], highest_coupon_number, coupons, table)
    return table[highest_coupon_number][amount]

mean_std_ways1=[]
stdev_std_ways1=[]
mean_my_ways2=[]
stdev_my_ways2=[]
mean_rec_ways1=[]
stdev_rec_ways1=[]
mean_rec2_ways2=[]
stdev_rec2_ways2=[]
meetpunten = list(range(1,71,1))
for i in meetpunten:
    std=[]
    my=[]
    rec=[]
    rec2=[]
    for j in range(1000):
        t1 = time.time()
        res = ways2pay(i)
        t2 = time.time()
        std.append(t2-t1)
        t1 = time.time()
        res = ways2pay2(i)
        t2 = time.time()
        my.append(t2-t1)
        rec.append(waysone)
        rec2.append(waystwo)
        waysone = 0
        waystwo= 0
    mean_std_ways1.append(stats.mean(std))
    stdev_std_ways1.append(stats.stdev(std))
    mean_my_ways2.append(stats.mean(my))
    stdev_my_ways2.append(stats.stdev(my))
    mean_rec_ways1.append(stats.mean(rec))
    stdev_rec_ways1.append(stats.stdev(rec))
    mean_rec2_ways2.append(stats.mean(rec2))
    stdev_rec2_ways2.append(stats.stdev(rec2))

#En dan de plot-code gemaakt met Matplotlib
#Zie bijvoorbeeld de tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(meetpunten, mean_std_ways1, 'b-')
plt.fill_between(meetpunten, np.array(mean_std_ways1)-np.array(stdev_std_ways1), np.array(mean_std_ways1)+np.array(stdev_std_ways1), color='b', alpha=0.3)
plt.plot(meetpunten, mean_my_ways2, 'r-')
plt.fill_between(meetpunten, np.array(mean_my_ways2)-np.array(stdev_my_ways2), np.array(mean_my_ways2)+np.array(stdev_my_ways2), color='r', alpha=0.3)
plt.xlabel("amount to try")
plt.ylabel("time (seconds)")
plt.legend(["ways2pay1", "ways2pay2"], loc='upper left')
plt.show()


#En dan de plot-code gemaakt met Matplotlib
#Zie bijvoorbeeld de tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(meetpunten, mean_rec_ways1, 'b-')
plt.fill_between(meetpunten, np.array(mean_rec_ways1)-np.array(stdev_rec_ways1), np.array(mean_rec_ways1)+np.array(stdev_rec_ways1), color='b', alpha=0.3)
plt.plot(meetpunten, mean_rec2_ways2, 'r-')
plt.fill_between(meetpunten, np.array(mean_rec2_ways2)-np.array(stdev_rec2_ways2), np.array(mean_rec2_ways2)+np.array(stdev_rec2_ways2), color='r', alpha=0.3)
plt.xlabel("amount to try")
plt.ylabel("recusions")
plt.legend(["ways2pay1", "ways2pay2"], loc='upper left')
plt.show()


# Zonder memosiatie heeft het algoritme een O(2^n) en met is deze O(1) omdat iets nooit 2 maal wordt berekend 
# doordat er gebruik wordt gemaakt van memoisatie. In de runtime is dit nog niet overduidelijk te zien omdat 
# de getallen dusdanig klein zijn waardoor dit niet veel moeite kost voor een computer. Bij het plotje van
# het aantal recursies is duidelijk te zien dat hoe groter de getallen worden des te minder er her berekent
# hoeft te worden door de look up tabel.