def print_unordered_pairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(str(array[i]) + "," + str(array[j]))

arr = [1,2,3,4]
print(print_unordered_pairs(arr))

"""
Time omplexity for this in order of n sqaure
"""