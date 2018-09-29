# randomized pivot to prevent O(n2)
from random import randint

from random import randint

def partition(arr, low, high):
    # 1. select a pivot algorithm
    # print(arr)
    pivot_value = arr[high]
    # let i be smaller index, initialize with low - 1
    i = low - 1
    # for j from 0 to high - 1
    for j in range(low, high):
        # if arr[j] <= pivot
        #   then
        #   1. increment the small index
        #   thus shifting the pivot point
        #   2. swap arr[i] with arr[j], the current and smaller index
        if arr[j] <= pivot_value:
            # swap the pivot with the last smaller index + 1
            # this is the pivot position
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # return the pivot position which is smaller index + 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    # print(arr)
    return i + 1


def quick_sort(arr, low, high):

    # base case
    if low < high: # otherwise finish
        pivot = partition(arr, low, high)

        # divide conquer the left
        quick_sort(arr, low, pivot - 1)

        # divide conquer the right
        quick_sort(arr, pivot + 1, high)

if __name__ == '__main__':
    
# X = [4, 13, 8, 3, 1, 2]
X = []
end = 2000001
for m in xrange(1, end):
    X.append(randint(1, 12023))
import time
start = time.time()
QuickSort(X, 0, len(X)-1)
done = time.time()
elapsed = done - start
print(elapsed)
print X[0]
print X[end - 2]
print "finished"
"""
using 2 cores cpu MHz: 3407.994 VM Centos7 4GB memory
sorting 2M randomized integer from 1 to 12023
quicksort is 100% slower than mergesort
see my merge sort program
program output
27.1561751366
1
12023
finished
"""
