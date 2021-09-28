def missing_positive(nums):

    length = len(nums)
    if 1 not in nums:
        return 1

    # nums = [1]
    if length == 1:
        return 2
    for i in range(length):
        if nums[i] <= 0 or nums[i] > length:
            nums[i] =length + 1

    for num in nums:
            num = abs(num)
            if num <= length and nums[num -1] >= 0:
                nums[num -1] *= -1

    for i in range(length):
        if nums[i] > 0:
            return i + 1
    return length + 1

number = [1,2,3,6,7]
print(missing_positive(number))
