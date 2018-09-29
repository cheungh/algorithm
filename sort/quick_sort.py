# randomized pivot to prevent O(n2)
from random import randint

# purpose of func
# select a pivot
# move smaller element to the left
# move larger element to the right
# return the pivot position
# run divide and conquer on
# 1. left of the pivot
# 2. right of the pivot
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

            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1] # swap the pivot with the last smaller index + 1, this is the pivot position
    # return the pivot position which is smaller index + 1
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

    """
    A = [20, 45, 93, 67, 10, 97, 52, 88, 33, 49]  # [6, 3, 17, 11, 4, 44, 76, 23, 12, 30]
    quick_sort(A, 0, len(A) - 1)

    print(A)
    """
    X = []
    end = 2000001
    for m in range(0, end):
        X.append(randint(1, 12023))
    import time
    start = time.time()
    quick_sort(X, 0, len(X)-1)
    done = time.time()
    elapsed = done - start
    print(elapsed)
    print(X[0])
    print(X[end - 2])
    print("finished")
"""
program output
43.372665882110596
1
12023
finished
"""
