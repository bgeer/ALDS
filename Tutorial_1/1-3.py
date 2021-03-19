from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats

fib1 = 0
fib2 = 0
def recfib1(n):
    global fib1 
    fib1 = fib1 + 1
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return recfib1(n-2) + recfib1(n-1)

def recfib2(n, answers = []):
    global fib2 
    fib2 = fib2 + 1
    if not answers:
        answers =[0,1]
        for i in range(n-1):
            answers.append(-1)
    if answers[n] == -1:
        answers[n] = recfib2(n-2, answers) + recfib2(n-1, answers)
    return answers[n]

mean_std_max=[]
stdev_std_max=[]
mean_my_max=[]
stdev_my_max=[]
mean_rec_max=[]
stdev_rec_max=[]
mean_rec2_max=[]
stdev_rec2_max=[]
meetpunten = list(range(1,20,1))
for i in meetpunten:
    std=[]
    my=[]
    rec=[]
    rec2=[]
    for j in range(1000):
        t1 = time.time()
        res = recfib1(i)
        t2 = time.time()
        std.append(t2-t1)
        t1 = time.time()
        res = recfib2(i)
        t2 = time.time()
        my.append(t2-t1)
        rec.append(fib1)
        rec2.append(fib2)
        fib1 = 0
        fib2 = 0
    mean_std_max.append(stats.mean(std))
    stdev_std_max.append(stats.stdev(std))
    mean_my_max.append(stats.mean(my))
    stdev_my_max.append(stats.stdev(my))
    mean_rec_max.append(stats.mean(rec))
    stdev_rec_max.append(stats.stdev(rec))
    mean_rec2_max.append(stats.mean(rec2))
    stdev_rec2_max.append(stats.stdev(rec2))

#En dan de plot-code gemaakt met Matplotlib
#Zie bijvoorbeeld de tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(meetpunten, mean_std_max, 'b-')
plt.fill_between(meetpunten, np.array(mean_std_max)-np.array(stdev_std_max), np.array(mean_std_max)+np.array(stdev_std_max), color='b', alpha=0.3)
plt.plot(meetpunten, mean_my_max, 'r-')
plt.fill_between(meetpunten, np.array(mean_my_max)-np.array(stdev_my_max), np.array(mean_my_max)+np.array(stdev_my_max), color='r', alpha=0.3)
plt.xlabel("number fibonacci")
plt.ylabel("time (seconds)")
plt.legend(["recfib1", "recfib2"], loc='upper left')
plt.show()


#En dan de plot-code gemaakt met Matplotlib
#Zie bijvoorbeeld de tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot(meetpunten, mean_rec_max, 'b-')
plt.fill_between(meetpunten, np.array(mean_rec_max)-np.array(stdev_rec_max), np.array(mean_rec_max)+np.array(stdev_rec_max), color='b', alpha=0.3)
plt.plot(meetpunten, mean_rec2_max, 'r-')
plt.fill_between(meetpunten, np.array(mean_rec2_max)-np.array(stdev_rec2_max), np.array(mean_rec2_max)+np.array(stdev_rec2_max), color='r', alpha=0.3)
plt.xlabel("number fibonacci")
plt.ylabel("recusions")
plt.legend(["rec1", "rec2"], loc='upper left')
plt.show()