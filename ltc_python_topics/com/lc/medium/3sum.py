"""https://leetcode.com/problems/3sum/"""
'''https://www.youtube.com/watch?v=n2_HLNY8e_Q&ab_channel=SaiAnishMalla'''

def find_3sum(nums):
    nums.sort()
    output = []

    length = len(nums)

    for x in range(0, length-2):
        if x != 0 and nums[x] == nums[x-1]:
            continue
        lower = x+1
        higher = length-1
        target = 0 - nums[x]

        while higher > lower:
            total = nums[lower] + nums[higher]

            if total == target:
                output.append([nums[x], nums[lower], nums[higher]])
                while higher > lower and nums[lower] == nums[lower + 1]:
                    lower += 1
                while higher > lower and nums[higher] == nums[higher - 1]:
                    higher -= 1

                lower += 1
                higher -= 1
            elif total > target:
                higher -= 1
            elif total < target:
                lower += 1

    return output

# Driver program
bar_height = [-1,0,1,2,-1,-4]

print("The output is ",
      find_3sum(bar_height))

