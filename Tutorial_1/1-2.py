from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats

def random_int_array(length):
    array = np.random.randint(0, high=100, size=length, dtype='l') #een array'tje met ints tussen de 0 en de 100 (exclusief)
    return array


def std_find(x, array):
    lst = list(array)
    try: 
        i=lst.index(x)
    except:
        i=-1
    return i

std_find(9, np.array([1,3,4]))

assert std_find(9, np.array([1,3,4])) == -1, "Nee, die zit er niet in..."
assert std_find(4, np.array([1,3,4])) == 2, "Nee, die zit er juist wel in..."

def my_find(x, array):
    index = -1
    l = len(array)
    for i in range(l):
        if array[i] == x:
            index = i
            break
    return index

mean_std_find=[]
stdev_std_find=[]
mean_std_find0=[]
stdev_std_find0=[]
meetpunten = list(range(5,10001,50))
for i in meetpunten:
    find =[]
    find0 =[]
    for j in range(50): #vijftig metingen per datapunt
        arr = random_int_array(i)
        t1 = time.time()
        res = my_find(57 ,arr)
        t2 = time.time()
        find.append(t2-t1)
        t1 = time.time()
        res = my_find(101 ,arr)
        t2 = time.time()
        find0.append(t2-t1)
    mean_std_find.append(stats.mean(find))
    stdev_std_find.append(stats.stdev(find))
    mean_std_find0.append(stats.mean(find0))
    stdev_std_find0.append(stats.stdev(find0))
    
#En dan de plot-code gemaakt met Matplotlib
#Zie bijvoorbeeld de tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(meetpunten, mean_std_find, 'b-')
plt.fill_between(meetpunten, np.array(mean_std_find)-np.array(stdev_std_find), np.array(mean_std_find)+np.array(stdev_std_find), color='b', alpha=0.3)
plt.plot(meetpunten, mean_std_find0, 'r-')
plt.fill_between(meetpunten, np.array(mean_std_find0)-np.array(stdev_std_find0), np.array(mean_std_find0)+np.array(stdev_std_find0), color='r', alpha=0.3)
plt.xlabel("number of array elements")
plt.ylabel("time (seconds)")
plt.legend(["find (find)", "find0 (find0)"], loc='upper left')
plt.show()


# Vragen
# De time complexity is O(n) omdat de runtime van het algoritme lineair stijgt met de grote van het array.
# Als je zoekt naar de worstcase dan moet het hele array doorgelopen worden, daardoor duur het langer voor dat het algoritme daar mee klaar is. 
# Ook worden de uitschieters telkes groter. 
# Terwijl het in een normale situatie een meer reele runtime heeft die niet zoveel groter wordt door de grote van de array.
