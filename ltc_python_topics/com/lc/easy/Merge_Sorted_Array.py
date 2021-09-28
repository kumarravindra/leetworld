#https://www.youtube.com/watch?v=P1Ic85RarKY
def merge_sorted_arr(num1, m, num2, n):
    # last index of num1
    last = m + n - 1

    # merge in reverse order
    while m > 0 and n > 0:
        if num1[m-1] > num2[n-1]:
            num1[last] = num1[m - 1]
            m -= 1
        else:
            num1[last] = num2[n-1]
            n -= 1
        last -= 1
    # fill num1 with leftover num2 elements

    while n > 0:
        num1[last] = num2[n - 1]
        n, last = n-1, last-1

    return num1

n1 = [2,2,3,0,0,0, 0, 0]
m = 3
n2 =[1,2, 3, 5,6]
n = 5
print(merge_sorted_arr(n1, m, n2,  n))


def merge_it(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

    return nums1

n1 = [2,2,3,0,0,0, 0, 0]
m = 3
n2 =[1,2, 3, 5,6]
n = 5
print(merge_it(n1, m, n2,  n))

def most_efficient_merge(nums1, m, nums2, n):
    # two get pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    # set pointer for nums1
    last = m + n - 1

    # while there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[last] = nums2[p2]
            p2 -= 1
        else:
            nums1[last] = nums1[p1]
            p1 -= 1
        last -= 1

    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]
    return nums1

n11 = [2,2,3,0,0,0, 0, 0]
m1 = 3
n22 =[1, 2, 3, 5,6]
n1 = 5
print(most_efficient_merge(n11, m1, n22,  n1))




