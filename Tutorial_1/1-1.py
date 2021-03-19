from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats

def random_int_array(length):
    array = np.random.randint(0, high=100, size=length, dtype='l') #een array'tje met ints tussen de 0 en de 100 (exclusief)
    return array

def max2(int_array):
    l = len(int_array)
    for i in range(l - 1):
        maxFound = True
        for j in range(l - 1):
            if int_array[j] > int_array[i]:
                maxFound = False
                break
        if maxFound:
            return int_array[i]

mean_std_max=[]
stdev_std_max=[]
mean_my_max=[]
stdev_my_max=[]
meetpunten = list(range(5,2501,50))
for i in meetpunten:
    std =[]
    my = []
    for j in range(50): #vijftig metingen per datapunt
        arr = random_int_array(i)
        t1 = time.time()
        res = max(arr)
        t2 = time.time()
        std.append(t2-t1)
        t1 = time.time()
        res = max2(arr)
        t2 = time.time()
        my.append(t2-t1)
    mean_std_max.append(stats.mean(std))
    stdev_std_max.append(stats.stdev(std))
    mean_my_max.append(stats.mean(my))
    stdev_my_max.append(stats.stdev(my))
    
#En dan de plot-code gemaakt met Matplotlib
#Zie bijvoorbeeld de tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(meetpunten, mean_std_max, 'b-')
plt.fill_between(meetpunten, np.array(mean_std_max)-np.array(stdev_std_max), np.array(mean_std_max)+np.array(stdev_std_max), color='b', alpha=0.3)
plt.plot(meetpunten, mean_my_max, 'r-')
plt.fill_between(meetpunten, np.array(mean_my_max)-np.array(stdev_my_max), np.array(mean_my_max)+np.array(stdev_my_max), color='r', alpha=0.3)
plt.xlabel("number of array elements")
plt.ylabel("time (seconds)")
plt.legend(["standard max (python)", "max2 (my_max)"], loc='upper left')
plt.show()

# Vraag
# Ja ik had verwacht dat de max2 nog steeds langzamer zo zijn dan de standaard max. Omdat het in worst case meer vergelijkingen moet uitvoeren.