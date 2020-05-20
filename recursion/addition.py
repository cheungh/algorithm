def addition(m, n):
    """
 formula: addition(m, n - 1) + m
  3 * 4
  9 + 3 = 12
 addition(3, 3) 9
 addition(3, 2) 6
 addition(3, 1) 3
 addition(3, 0) 0
    """
    if n == 0:
        return 0
    # also work with n == 1 then return m
    min_addition = addition(m, n - 1)
    return m + min_addition

print(addition(3, 4))
print(addition(9, 7))
