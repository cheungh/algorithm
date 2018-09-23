from random import randint
import time

def merge_sort(A):
    # base case of recursion : return A
    if len(A) < 2:
        return A
    # divide array into 2 arrays, left and right
    left = A[:len(A) / 2]
    right = A[len(A) / 2:]
    # divide to smaller part via recursion
    left = merge_sort(left)
    right = merge_sort(right)

    # return merge result
    combined = merge(left, right)
    return combined

def merge(left, right):
    combined_array = []
    # let left_counter be the tracker for # of element left placed into combined
    # let right_counter be the tracker for # of element right placed into combined

    left_counter = 0
    right_counter = 0

    # while loop if there are element in both left and right array
    while left_counter < len(left) and right_counter < len(right):
        if left[left_counter] < right[right_counter]:
            combined_array.append(left[left_counter])
            left_counter += 1
        else:
            combined_array.append(right[right_counter])
            right_counter += 1

    while left_counter < len(left):
        combined_array.append(left[left_counter])
        left_counter += 1

    while right_counter < len(right):
        combined_array.append(right[right_counter])
        right_counter += 1
    return combined_array

X = []
end = 2000001
for m in xrange(1, end):
    X.append(randint(1, 12023))
start = time.time()
Y = merge_sort(X)
done = time.time()
elapsed = done - start
print(elapsed)
print Y[0]
print Y[len(Y)-1]
print "finished"

# program output
"""
using 2 cores cpu MHz: 3407.994 VM Centos7 4GB memory
sorting 2M randomized integer from 1 to 12023
The result is 100% faster than quicksort
quicksort takes 26 seconds.
11.950414896
183
9212
finished
"""
