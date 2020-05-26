def permute(a, start, end):
    # print the string when it has reached the last char
    # the program increment the start index 
    if start == end:
        print(''.join(a))
        
    for i in range(start, end + 1):
        # swap from the first char
        a[start], a[i] = a[i], a[start]
        # the program increment the start index and continue to swap char 
        # until the start == end
        permute(a, start + 1, end)
        # swap back to original pattern
        a[start], a[i] = a[i], a[start]


# Test
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)
