"Given an array of integers nums and an integer target, return indices of the two numbers such that"
"they add up to target."

'''
https://leetcode.com/problems/two-sum/
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def twoSum(nums, target):
    nSet = {}
    for nIndex, num in enumerate(nums):
        if target-num in nSet:
            return [nSet[target-num], nIndex]
        nSet[num] = nIndex

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))