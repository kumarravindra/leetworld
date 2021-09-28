def runtimeofpandsum(array):
    sum = 0
    product = 1

    for i in array:
        sum += i

    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

arr = [1,2,3,4]
print(runtimeofpandsum(arr))

"""
Time complexity of this example is O(N) for first for loop and O(N) for second loop
so, its O(2N) = O(N)
"""