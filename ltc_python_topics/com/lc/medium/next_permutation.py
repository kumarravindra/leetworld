#https://www.youtube.com/watch?v=4wlBBRo4tYY&ab_channel=SaiAnishMalla
#https://leetcode.com/problems/next-permutation/

def find_next_permutation(nums):
    length = len(nums)
    if length <= 2:
        return nums.reverse()

    # lets start from second last point and pass there as pointer
    pointer = length - 2
    while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
        pointer -= 1
        # at end of the number in left side
    if pointer == -1:
        return nums.reverse()

    for x in range(length - 1, pointer, -1):
        if nums[pointer] < nums[x]:
            nums[pointer], nums[x] = nums[x], nums[pointer]
            break

    nums[pointer + 1:] = reversed(nums[pointer + 1:])
    return nums

# Driver program
bar_height = [8,2,7,3,5,6,9]
#[1,2,3]

print("Maximum water that can be accumulated is ",
      find_next_permutation(bar_height))




