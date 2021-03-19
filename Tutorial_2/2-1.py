from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats

class myStack():

    def __init__(self, maxCapicity, t):
        self.maxCapicity = maxCapicity
        self.currentCapicity = 0
        self.type = t
        self.array = np.array([], dtype=self.type)
        

    def push(self, item):
        if self.currentCapicity != self.maxCapicity:
            self.array = np.append(self.array, np.array(item, dtype=self.type)) #need to add this way else the dtype would be changed by default.
            self.currentCapicity += 1
            print(self.array)
            print(self.currentCapicity)
            return True
        else:
            print("Stack reached max capicity")
            return False

    def pop(self):
        if self.currentCapicity != 0:
            self.array = np.delete(self.array, -1)
            self.currentCapicity -= 1
            return True
        else:
            print("Trying to pop empty stack...")
            return False

    def isEmpty(self):
        if self.currentCapicity == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.currentCapicity == self.maxCapicity:
            return True
        else:
            return False

    def doubleCapicity(self):
        self.maxCapicity *= 2

stack = myStack(1, 'uint8')
print(stack.isEmpty())
print(stack.isFull())
stack.pop()
print(stack.isEmpty())
stack.pop()