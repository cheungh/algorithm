def insertion_sort(a, n):
    """ 
    insertion sort algorithm
    # outer loop from left to right start from 1
    # inner loop from right to left end to right counter eq 0
    1. compare 2 elements 
    2. and swap 
    3. and decrement right counter
    # let l be left_cnf
    # let r be right_cnt
    """
    for l in range(1, n):
        r = l
        while a[r-1] > a[r] and r > 0:
            a[r], a[r - 1] = a[r-1], a[r]
            r -= 1
    return a


def reversed_insertion_sort(a, n):
    for i in range(1, n):
        idx = i
        while a[idx] > a[idx - 1] and idx > 0:
            # swap
            a[idx], a[idx - 1] = a[idx - 1], a[idx]
            idx -= 1
    return a


print(insertion_sort([101, 45, 9, 17, 2, 3, 1], 7))

print(insertion_sort([1, 2, 3, 4, 5, 6, 9], 7))

print(reversed_insertion_sort([101, 45, 9, 17, 2, 3, 1], 7))
