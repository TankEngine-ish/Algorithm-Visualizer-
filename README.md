# Sorting Algorithm Visualizer

For my very first project in Python I decided to go for an
algorithm visualizer. 

It was all done in an an Anaconda environment along with Jupyter and IPyWidgets for the plotting charts inside VSCode.
In the first part of the project I created some simple .png files with the unsorted and then sorted arrays.
Then, in the second part of the project I animated the sorting process but also added the number of times the arrays were accessed.

The number of elements in the arrays can be easily changed inside the python code by swapping the value of 'N'
with any anumber. I chose 30 elements. In the future I might add more popular algorithms to this project.
You can check the results below.



## Insertion Sort

The first algorithm that was implemented was insertion sort.
It is one of the simplest and most commonly used sorting algorithms. 
It involves the sorted list created based on an iterative comparison of each element in the list with its adjacent element.

An index pointing at the current element indicates the position of the sort. At the beginning of the sort (index=0), the current value is compared to the adjacent value to the left. If the value is greater than the current value, no modifications are made to the list; this is also the case if the adjacent value and the current value are the same numbers. 

However, if the adjacent value to the left of the current value is lesser, then the adjacent value position is moved to the left, and only stops moving to the left if the value to the left of it is lesser. Despite its simplicity, Insertion sort is quite inefficient compared to quicksort, merge sort etc.


![Alt text](<Images/Screenshot from 2023-12-16 00-03-51.png>)


## Quick Sort

The second algorithm I implemented was quick sort.
It's a recursive, divide-and-conquer algorithm that is ranked as fastest in its class. 
It has an average time complexity of O (n log n ), which compared to its peers is pretty fast. 
Quick sort creates two empty arrays to hold elements less than the pivot value and elements greater than the pivot value, and then recursively sort the sub arrays. There are two basic operations in the algorithm, swapping items in place and partitioning a section of the array.

You can also see the time it took to sort (0.1 ms) with the help
of the python's time library.


![Alt text](<Images/Screenshot from 2023-12-23 22-12-33.png>)


This is the second part of the project where I actualy animated the sorting process.
You can see how much faster quicksort is than insertion.

![quicksort](./Images/quicksort.gif =250x250)