"""
https://leetcode.com/problems/move-zeroes/submissions/


"""

def move_all_zeros(nums):
    prev_idx = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            hold = nums[prev_idx]
            nums[prev_idx] = nums[i]
            nums[i] = hold
            prev_idx += 1
    return nums


num = [0,1,0,3,12]
print(move_all_zeros(num))