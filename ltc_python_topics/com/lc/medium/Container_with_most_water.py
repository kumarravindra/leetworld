def mostWater(height):
    left, right = 0, len(height)-1
    max_water = 0
    while left < right:
        max_water = max(max_water,(right-left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


hgt = [1,8,6,2,5,4,8,3,7]
print(mostWater(hgt))

