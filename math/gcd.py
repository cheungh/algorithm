def gcd(a, b):
    if a == 0:
        return b
    divisor = b % a
    return gcd(divisor, a)

if __name__ == '__main__':

    print(gcd(15, 25))
    # return 5
