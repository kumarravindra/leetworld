"""
 How to convert a number from decimal to the binary
 example : 13 to binary
 Division by      Quotient    Remainder
 13/2               6           1
 6/2                3           0
 3/2                1           1
 1/2                0           1

 So, 13 is 1101 as binary number
 Steps:
 1- Divide the number by 2
 2- Get the integer quotient for the next iteration
 3- Get the remainder for the binary digit
 4- Repeat the steps until the quotient is equal to 0

 :param n:
 :return:

 but how to write a recurssion function for this
 seems if we multiply bottom 1 by 10, and add next digit and then multiply by 10 and add another digit
 1 * 10 = 10 +1, = 11 * 10 = 110 * 10 = 1100 + 1 = 1101
 so function will be f(n) = n mod 2 + 10 * f(n/2)
 """


def decimaltobinary(n):
    assert int(n) == n, 'Number must be integer only!'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimaltobinary(int(n / 2))


print(decimaltobinary(13))
