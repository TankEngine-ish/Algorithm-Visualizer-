# Sorting Algorithm Visualizer

For my very first project in Python I decided to go for an
algorithm visualizer. 

It was all done in an an Anaconda environment along with Jupyter for the plotting charts inside VSCode.

## Insertion Sort

The first algorithm that was implemented was insertion sort.
It is one of the simplest and most commonly used sorting algorithms. 
It involves the sorted list created based on an iterative comparison of each element in the list with its adjacent element.

An index pointing at the current element indicates the position of the sort. At the beginning of the sort (index=0), the current value is compared to the adjacent value to the left. If the value is greater than the current value, no modifications are made to the list; this is also the case if the adjacent value and the current value are the same numbers. 

However, if the adjacent value to the left of the current value is lesser, then the adjacent value position is moved to the left, and only stops moving to the left if the value to the left of it is lesser.Despite its simplicity, Insertion sort is quite inefficient compared to quicksort, merge sort etc.


![Alt text](<Images/Screenshot from 2023-12-16 00-03-51.png>)


## Quick Sort

The second algorithm I implemented was quick sort.
It's a recursive, divide-and-conquer algorithm that is ranked as fastest in its class. 
It has an average time complexity of O (n log n ), which compared to its peers is pretty fast. 

You can also see the time it took to sort (0.1 ms) with the help
of the python's time library.


![Alt text](<Images/Screenshot from 2023-12-23 22-12-33.png>)