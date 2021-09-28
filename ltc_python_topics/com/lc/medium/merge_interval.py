#https://leetcode.com/problems/merge-intervals/
from typing import List
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        updated_merged = []
        for i in sorted(intervals):
            if updated_merged and i[0] <= updated_merged[-1][1]:
                updated_merged[-1][1] = max(updated_merged[-1][1], i[1])
            else:
                updated_merged += i,
        return updated_merged

a = Solution()
arr = [[1,3],[2,6],[8,10],[15,18]]
print(a.merge(arr))

# i[0] is i.start and i[1] is i.end same way updated_merged[-1][1] is updated_merged[-1].end 

