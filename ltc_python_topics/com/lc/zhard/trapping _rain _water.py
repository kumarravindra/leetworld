# https://www.geeksforgeeks.org/trapping-rain-water/
#https://leetcode.com/problems/trapping-rain-water/solution/
# Space Complexity : O(1) and time complexity : O(n)

def findWater(bar_height):
    # initialize output and maximum element on left and right
    result = 0
    l_max = 0
    r_max = 0
    # indices to traverse the array
    left = 0
    right = len(bar_height) - 1

    while (left <= right):

        if (bar_height[left] < bar_height[right]):

            if (bar_height[left] > l_max):

                # update max in left
                l_max = bar_height[left]
            else:
                # water on curr element = max - curr
                result += l_max - bar_height[left]
            left += 1

        else:

            if (bar_height[right] > r_max):
                # update right maximum
                r_max = bar_height[right]
            else:
                result += r_max - bar_height[right]
            right -= 1

    return result

# Driver program
bar_height = [4, 2, 0, 3, 0, 2, 5]

print("Maximum water that can be accumulated is ",
      findWater(bar_height))





