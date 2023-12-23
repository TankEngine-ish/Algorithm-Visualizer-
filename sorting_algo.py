#%%
import time 
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16

N = 30
arr = np.round(np.linspace(0,1000,N), 0)
np.random.seed(0)
np.random.shuffle(arr) 

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)


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
####### Quick Sort #######
##############################

sorter = "Quick"


def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, hi)
        quicksort(A, p+1, hi)


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
##############################