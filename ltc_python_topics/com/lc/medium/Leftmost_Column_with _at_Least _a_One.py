# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# facebook most asked
#https://leetcode.com/problems/container-with-most-water/
#https://www.youtube.com/watch?v=_xRnjwnIh8k
#https://www.youtube.com/watch?v=l-4l1HXG8eQ
# https://www.youtube.com/watch?v=AS3Hcla3Hm0

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        rows, cols = binaryMatrix.dimensions()
        curr_row = 0
        curr_col = cols - 1

        while curr_row < rows and curr_col >= 0:
            if binaryMatrix.get(curr_row, curr_col) == 0:
                curr_row += 1
            else:
                curr_col -= 1

        if curr_col != cols - 1:
            return curr_col + 1
        else:
            return -1



lft = Solution()
mtx = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
[[0,0,0,1],[0,0,0,0],[0,1,1,1]]
[[0,0,0,0],[0,0,0,0],[0,0,0,1]]
# Driver program

print(lft.leftMostColumnWithOne(mtx))