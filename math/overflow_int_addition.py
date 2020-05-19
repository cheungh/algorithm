def int_overflow_addition(a, b):
    """
    perform addition on strings for integer overflow
    :param a: string a
    :param b: string b
    :return:
    """
    # 1. reverse the string
    # start with the right digit
    a = a[::-1]
    b = b[::-1]

    len_a = len(a)
    len_b = len(b)

    # 2. set max_l as max loop condition
    max_l = max(len_b, len_a)

    # use sum_arr to store the sum of each digit for the 2 numbers
    sum_arr = []

    for i in range(max_l):
        if i < len_a and i < len_b:
            sum_arr.append(int(b[i]) + int(a[i]))
        else:
            if i < len_a:
                sum_arr.append(int(a[i]))
            else:
                sum_arr.append(int(b[i]))
    # shift the overflow of 10 base to the next digit
    for i in range(len(sum_arr)):
        if sum_arr[i] > 9:
            sum_arr[i] -= 10
            if i + 1 == len(sum_arr):
                sum_arr.append(1)
            else:
                sum_arr[i + 1] += 1
    # reverse loop and append the char into return result string.
    result = ""
    for i in range(len(sum_arr) - 1, -1, -1):
        result += str(sum_arr[i])
    return result


print(int_overflow_addition("156", "78"))

print(int_overflow_addition("1234", "9876"))

print(int_overflow_addition("19999999999999999999999999999999999999999", "5"))

"""
program output:
234
11110
20000000000000000000000000000000000000004
"""
