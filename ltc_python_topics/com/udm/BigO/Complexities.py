"""
Algorithm run time complexities

Complexity      Name        Sample
O(1)           Constant     Accessing a specific element in array
O(N)           Linear       Loop through array elements
O(LogN)        Logarithmic  Find an element in sorted array
O(N2)         Quadratic     Looking at a every index in the array twice
O(2 power N) Exponential    Double recursion in Fibonacci
"""
def runit(n):

    for index in range (0, len(n),3):
        print(n[index])


arr = [1, 2, 3, 4, 5, 6]
print(runit(arr))

"""
Space Complexity is important too
Drop constants and non dominant terms like O(2N) = O(N)

"""