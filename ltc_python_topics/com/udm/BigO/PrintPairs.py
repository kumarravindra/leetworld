def printpairs(array):

    for i in array:
        for j in array:
            print(str(i)+","+str(j))

arr = [1,2,3,4]
print(printpairs(arr))

"""
Time Complexity for this example is O(n * n) = O(N*2)
"""