def two_sum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in dict:
            dict[num] = i
        else:
            return [dict[n], i]

def main():
    print(two_sum([3,2,4], 6))

main()
