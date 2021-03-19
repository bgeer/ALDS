from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats
import random


class priorityQueue:
    def __init__(self):
        self.queue = []

    def Queue( self, data, priority ):      #O(1)
        self.queue.append([data,priority])

    def Dequeue(self):                      #O(n)
        maximum = [0,0]
        for i in range(len(self.queue)):
            if maximum[1] < self.queue[i][1]:
                maximum = self.queue[i]
        self.queue.remove(maximum)
        return maximum[0]

    def Contains(self, data):               #O(n)
        for i in range(len(self.queue)):
            if data == self.queue[i][0]:
                return True
        return False

    def Remove(self, data):                 #O(n) = O(n) + O(n) = 2 * O(n)
        memo =[]
        for i in range(len(self.queue)):
            if data == self.queue[i][0]:
                memo.append(self.queue[i])
        for j in range(len(memo)):
            self.queue.remove(memo[j])

    def __repr__(self):                     #O(1)
        return str(self.queue)



class priorityQueue2:
    def __init__(self):             
        self.dict = {}
    
    def Queue( self, data, priority ):      #O(1)
        if priority in self.dict:
            self.dict[priority].append(data)
        else:
            self.dict[priority] = [data]
            
    def Dequeue(self):                      #O(1)
        highest_priority = max(self.dict)
        if self.dict[highest_priority] == []:
            del self.dict[highest_priority]
            highest_priority = max(self.dict)
        value = self.dict[highest_priority].pop(0)
        if self.dict[highest_priority] == []: #for the last empty to delete else it would result in a empty priority.
            del self.dict[highest_priority]
            return value
        return value
    
    def Contains(self, data):               #O(n)
        for l in self.dict.values():
            if data in l:
                return True
        else:
            return False
    
    def Remove(self, data):                 #O(n)
        for l in self.dict.values():
            if data in l:
                l.remove(data)
        
        
    
    def __repr__(self):                     #O(1)
        return str(self.dict)

        
def singleTestPriorityQueue1():
    print("Testing priorityQeue 1 based on a list")
    t1 = time.time()     
    a = priorityQueue()
    t2 = time.time()
    print("Creating a queue took: " + str((t2 - t1) * 1000) + " milliseconds")
    t1 = time.time()
    a.Queue(1, 6)
    t2 = time.time()
    print("Queueing a value took: " + str((t2 - t1) * 1000) + " milliseconds")
    a.Queue(4, 1)
    a.Queue(7, 2)
    a.Queue(7, 4)
    print(a.Dequeue())
    print(a)
    print(a.Contains(4))
    print(a.Contains(3))
    a.Remove(7)
    a.Remove(8)
    print(a)
    print("End of testing priorityQeue 1 based on a list")           



def singleTestPriorityQueue2():
    print("Testing priorityQeue 2 based on a dictonary")           
    a = priorityQueue2()

    a.Queue(1, 6)
    a.Queue(4, 1)
    a.Queue(7, 2)
    a.Queue(7, 4)
    print(a)
    print(a.Dequeue())
    print(a)
    print(a.Contains(4))
    print(a.Contains(3))
    a.Remove(7)
    a.Remove(8)
    print(a)
    print("End of testing priorityQeue 2 based on a dict")   

# singleTestPriorityQueue1()
# singleTestPriorityQueue2()


#Average test function with max priority of 10 
def averageTestPriorityQueue(classType, amountOfValues, maxRandomValue):
    if classType == 1:
        a = priorityQueue()
    elif classType == 2:
        a = priorityQueue2()
    else:
        print("Please specify which class to test...")
        return
    randomValues = []
    queueTimes = []
    containsTimes = []
    dequeueTimes = []
    removeTimes = []

    # Creating list with random ints
    for i in range(amountOfValues):
        random.seed(time.time())
        randomValues.append(random.randint(1, maxRandomValue))
    
    # print(randomValues)

    # Measuring Queue Times
    for i in range(amountOfValues):
        random.seed(time.time()) #Using time as seed so it will be always as random as possible because time keeps going.
        randomPriority = random.randint(1,10) # Max priority from 1 tot 10 not done in function because it also takes some time
        t1 = time.time()
        a.Queue(randomValues[i], randomPriority) # Only variables because function calls as parameters will also take time.
        t2 = time.time()
        queueTimes.append(t2-t1)
        # print(a)
    
    # print(queueTimes)

    # Measuring Contains times
    for j in range(int(amountOfValues-1)): # Search for half of the values in the list
        random.seed(time.time())
        randomSearchValue = random.randint(1, max(randomValues)- 1) #idk if this is the best way because what is the chance this value is in the list ;/
        # print(randomSearchValue)
        t1 = time.time()
        a.Contains(randomSearchValue)
        t2 = time.time()
        containsTimes.append(t2-t1)
    # print(containsTimes)

    # Measuring Dequeue Times
    for k in range(amountOfValues):
        # print("Before:")
        # print(a)
        t1 = time.time()
        a.Dequeue()
        t2 = time.time()
        dequeueTimes.append(t2-t1)
        # print("After:")
        # print(a)

    # Measuring Remove Times
    for l in range(amountOfValues): #Fill a queue first else it will be hard to remove value's, same way as before without measuring the time.
        random.seed(time.time()) 
        randomPriority = random.randint(1,10) 
        a.Queue(randomValues[i], randomPriority)
        

averageTestPriorityQueue(2, 10, 100)