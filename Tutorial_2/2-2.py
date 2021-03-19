from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats


# Schrijf hier de code voor opgave 2
def random_int_array(length):
    array = np.random.randint(-128, high=127, size=length,
                              dtype=np.int8)  # een array'tje met ints tussen de 0 en de 100 (exclusief)
    return array


def quicksort(array, low, high):
    counter = 0
    if low >= high:
        return array, counter
    p, p_counter = partition(array, low, high)
    array, counter1 = quicksort(array, low, p - 1)
    array, counter2 = quicksort(array, p + 1, high)
    counter += p_counter + counter1 + counter2
    return array, counter


def partition(array, low, high):
    counter = 0
    pivot = array[high]
    i = low
    for j in range(low, high, 1):
        if array[j] <= pivot:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
        counter += 1
    temp = array[i]
    array[i] = array[high]
    array[high] = temp
    return i, counter


def quicksort_low(array, low, high):
    counter = 0
    if low >= high:
        return array, counter
    p, p_counter = partition_low(array, low, high)
    array, counter1 = quicksort_low(array, low, p - 1)
    array, counter2 = quicksort_low(array, p + 1, high)
    counter += p_counter + counter1 + counter2
    return array, counter


def partition_low(array, low, high):
    counter = 0
    pivot = min(array[low:high + 1])
    i = array.tolist().index(pivot)
    array[high], array[i] = array[i], array[high]
    i = low
    for j in range(low, high):
        counter += 1
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i, counter


def quicksort_med(array, low, high):
    counter = 0
    if low >= high:
        return array, counter
    p, p_counter = partition_med(array, low, high)
    array, counter1 = quicksort_med(array, low, p - 1)
    array, counter2 = quicksort_med(array, p + 1, high)
    counter += p_counter + counter1 + counter2
    return array, counter


def partition_med(array, low, high):
    counter = 0
    pivot = int(stats.median_high(array[low:high + 1]))
    i = array.tolist().index(pivot)
    array[high], array[i] = array[i], array[high]
    i = low
    for j in range(low, high):
        counter += 1
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i, counter


mean_std_max = []
stdev_std_max = []
mean_my_max = []
stdev_my_max = []
mean_my_med = []
stdev_my_med = []
mean_std_max_time = []
stdev_std_max_time = []
mean_my_max_time = []
stdev_my_max_time = []
mean_my_med_time = []
stdev_my_med_time = []
meetpunten = list(range(5, 201, 5))
for i in meetpunten:
    quick1 = []
    quick1_time = []
    quick2 = []
    quick2_time = []
    quick3 = []
    quick3_time = []
    for j in range(50):  # vijftig metingen per datapunt
        array = random_int_array(i)
        t1 = time.time()
        res, compared1 = quicksort(array, 0, len(array) - 1)
        t2 = time.time()
        quick1_time.append(t2 - t1)
        quick1.append(compared1)
        t1 = time.time()
        res, compared2 = quicksort_low(array, 0, len(array) - 1)
        t2 = time.time()
        quick2_time.append(t2 - t1)
        quick2.append(compared2)
        t1 = time.time()
        res, compared3 = quicksort_med(array, 0, len(array) - 1)
        t2 = time.time()
        quick3_time.append(t2 - t1)
        quick3.append(compared3)
    mean_std_max.append(stats.mean(quick1))
    stdev_std_max.append(stats.stdev(quick1))
    mean_my_max.append(stats.mean(quick2))
    stdev_my_max.append(stats.stdev(quick2))
    mean_my_med.append(stats.mean(quick3))
    stdev_my_med.append(stats.stdev(quick3))
    mean_std_max_time.append(stats.mean(quick1_time))
    stdev_std_max_time.append(stats.stdev(quick1_time))
    mean_my_max_time.append(stats.mean(quick2_time))
    stdev_my_max_time.append(stats.stdev(quick2_time))
    mean_my_med_time.append(stats.mean(quick3_time))
    stdev_my_med_time.append(stats.stdev(quick3_time))

plt.plot(meetpunten, mean_std_max, 'b-')
plt.fill_between(meetpunten, np.array(mean_std_max) - np.array(stdev_std_max),
                 np.array(mean_std_max) + np.array(stdev_std_max), color='b', alpha=0.3)
plt.plot(meetpunten, mean_my_max, 'r-')
plt.fill_between(meetpunten, np.array(mean_my_max) - np.array(stdev_my_max),
                 np.array(mean_my_max) + np.array(stdev_my_max), color='r', alpha=0.3)
plt.plot(meetpunten, mean_my_med, 'y-')
plt.fill_between(meetpunten, np.array(mean_my_med) - np.array(stdev_my_med),
                 np.array(mean_my_med) + np.array(stdev_my_med), color='y', alpha=0.3)
plt.xlabel("number of array elements")
plt.ylabel("Comparisons")
plt.legend(["Quicksort1(Normal)", "Quicksort2(Minimum)", "Quicksort3(Median)"], loc='upper left')
plt.show()

plt.plot(meetpunten, mean_std_max_time, 'b-')
plt.fill_between(meetpunten, np.array(mean_std_max_time) - np.array(stdev_std_max_time),
                 np.array(mean_std_max_time) + np.array(stdev_std_max_time), color='b', alpha=0.3)
plt.plot(meetpunten, mean_my_max_time, 'r-')
plt.fill_between(meetpunten, np.array(mean_my_max_time) - np.array(stdev_my_max_time),
                 np.array(mean_my_max_time) + np.array(stdev_my_max_time), color='r', alpha=0.3)
plt.plot(meetpunten, mean_my_med_time, 'y-')
plt.fill_between(meetpunten, np.array(mean_my_med_time) - np.array(stdev_my_med_time),
                 np.array(mean_my_med_time) + np.array(stdev_my_med_time), color='y', alpha=0.3)
plt.xlabel("number of array elements")
plt.ylabel("Time")
plt.legend(["Quicksort1(Normal)", "Quicksort2(Minimum)", "Quicksort3(Median)"], loc='upper left')
plt.show()

