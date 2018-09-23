# randomized pivot to prevent O(n2)
from random import randint

def QuickSort(A, start, end):
    # base case
    # print "run qs [%s] [%s]" % (start, end)
    if end > start:
        pivot = partition(A, start, end)
        QuickSort(A, start, pivot - 1)
        QuickSort(A, pivot + 1, end)

def partition(A, start, end):
    # print "run partition [%s] [%s]" % (start, end)
    # print "A is  [%s]" % A
    # pivot = end
    # pivot = randint(start, end)
    # pivot = start
    pivot = ((end - start) / 2) + start
    # print "pivot is %s" % pivot
    A[pivot], A[end] = A[end], A[pivot]
    i = start - 1
    for j in xrange(start, end):
        if A[j] <= A[end]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    # print "p %s : A is [%s]" % (i + 1, A)
    return i + 1



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
