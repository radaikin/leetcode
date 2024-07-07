#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x: int = 0
        y: int = len(matrix) - 1
        while x <= y:
            mid: int = (x + y)//2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][0] > target:
                y = mid - 1
            else:
                x = mid + 1
        row = (x + y)//2
        x: int = 0
        y: int = len(matrix[row]) - 1
        while x <= y:
            mid: int = (x + y)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                y = mid - 1
            else:
                x = mid + 1
        return False
# @lc code=end
