def sumOfDigits(n):
    assert n >=0 and int(n) == n , 'Please use positive integer number'
    if n == 0:
        return n
    return int(n%10) + sumOfDigits(int(n//10))

print(sumOfDigits(123456))
