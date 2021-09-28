#https://www.youtube.com/watch?v=U8XENwh8Oy8
# https://leetcode.com/tag/array/

def find_rotated_sorted_array_index(numbs, target):
    l, r = 0, len(numbs)-1

    while l <= r:
        mid = (l + r) // 2
        
        if target == numbs[mid]:
            return mid

        # l sorted position
        if numbs[l] <= numbs[mid]:
            if target > numbs[mid] or target < numbs[l]:
                l = mid + 1
            else:
                r = mid - 1
        # r sorted position
        else:
            if target < numbs[mid] or target > numbs[r]:
                r = mid - 1
            else:
                l = mid + 1
    return - 1


arr = [4,5,6,7,0,1,2]
trgt = 0
print(find_rotated_sorted_array_index(arr, trgt))
