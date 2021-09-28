def unorderedpairtwoarray(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i])+ "," + str(arrayB[j]))

arr1 = [1,2,3]
arr2 = [5,6,7]
print(unorderedpairtwoarray(arr1,arr2))