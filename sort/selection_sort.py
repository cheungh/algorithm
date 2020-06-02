def selection_sort(a, n):
    """
    how selection sort works:
    start from left most element of array 
    -> find smallest ele and swap with current ele 
    -> continue until loop has reached right most element
    -> loop end and array is sorted
    
    - loop array idx from left to right
    - find smallest and swip with the loop element idx
    for 0 to n-1:
        current_value <= a[i]
        for current_idx to n-1:
            find smallest item and store its index
        if not equal to current idx
            swap smallest with current_idx
        else:
            do nothing, since current is smallest
    """
    for i in range(0, n):
        smallest_value = a[i]
        smallest_index = i
        for j in range(i + 1, n):
            if a[j] < smallest_value:
                smallest_value = a[j]
                smallest_index = j
        if smallest_index != i:
            a[i], a[smallest_index] = a[smallest_index], a[i]
    pass

a = [9, 7, 2, 3, 1]
selection_sort(a, len(a))
print(a)

a = [101, 45, 9, 17, 2, 3, 1]
selection_sort(a, len(a))
print(a)

a = [1, 3, 5, 7, 9]
selection_sort(a, len(a))
print(a)
