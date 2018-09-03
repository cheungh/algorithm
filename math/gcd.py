
def gcd(a, b):
    # base case return result
    if a % b == 0:
        return b
    else:
        # recursive call
        return gcd(a, (a % b))


if __name__ == '__main__':

    print(gcd(15, 25))
    # return 5
