#%%
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 16


N = 30
arr = np.round(np.linspace(0,1000,N), 0)
np.random.shuffle(arr) 

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)


##############################
####### Insertion Sort #######
##############################

sorter = "Insertion"

i = 1
while (i < len(arr)):
    j = i
    while ((j > 0) and (arr[j-1] > arr[j])):
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = temp
        j -= 1
    i += 1

##############################
    
fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1),arr, align="edge", width=0.8)






















##############################
####### Quick Sort #######
##############################
