#%%
import time 
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class TrackedArray():
    
    def _init_(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []  # whether it's 'get' or 'set' 
        self.full_copies = []

    def _getitem_(self, key):
        self.track(key, "get")
        return self.arr._getitem_(key)
    
    def _setitem_(self, key, value):
        self.arr._setitem_(key, value)
        self.track(key, "set")

    def _len_(self):
        return self.arr._len_()
    



                        

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16

N = 30
arr = np.round(np.linspace(0,1000,N), 0)
np.random.seed(0)
np.random.shuffle(arr) 

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value", title = "Unsorted array")


##############################
####### Insertion Sort #######
##############################

sorter = "Insertion"
t0 = time.perf_counter()

i = 1
while (i < len(arr)):
    j = i
    while ((j > 0) and (arr[j-1] > arr[j])):
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = temp
        j -= 1
    i += 1

dt = time.perf_counter() - t0

##############################

print(f"---------- {sorter} Sort ----------")
print(f"Array Sorted in {dt*1E3:.1f} ms")
    
fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)


##############################
######### Quick Sort #########
##############################

sorter = "Quick"

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)


def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
    temp = A[i]
    A[i] = A[hi]
    A[hi] = temp
    return i

t0 = time.perf_counter()
quicksort(arr, 0, len(arr)-1)
dt = time.perf_counter() - t0

##############################


print(f"---------- {sorter} Sort ----------")
print(f"Array Sorted in {dt*1E3:.1f} ms")
    
fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value", title = f"{sorter} sort")