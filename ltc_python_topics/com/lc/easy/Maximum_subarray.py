def find_maximum_sub_array(nums):
    length = len(nums)
    cur_sum = max_sum = nums[0]


    for i in range(1, length):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum



number = [-2,1,-3,4,-1,2,1,-5,4]
print(find_maximum_sub_array(number))
