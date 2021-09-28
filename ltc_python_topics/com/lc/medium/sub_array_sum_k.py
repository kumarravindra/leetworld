def sub_array_sum_k(nums, k):
    dict = {0: 1}
    count = 0
    sum = 0
    for num in nums:
        sum += num
        if sum - k in dict:
            count += dict[sum - k]
        if sum in dict:
            dict[sum] += 1
        else:
            dict[sum] = 1
    return count



nu = [1,4,5,6,8,2,3]
ki = 5
print(sub_array_sum_k(nu, ki))