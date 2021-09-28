from array import *


def searchElementInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Element doesnt exist in array"


arr = [1, 2, 3, 4, 5]
print(searchElementInArray(arr, 3))
