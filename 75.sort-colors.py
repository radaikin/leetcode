#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = g = 0
        for i in nums:
            if i == 0:
                r += 1
            elif i == 1:
                g += 1

        i: int = 0
        while i < len(nums):
            if i < r:
                nums[i] = 0
            elif i < r + g:
                nums[i] = 1
            else:
                nums[i] = 2
            i += 1


# @lc code=end

# debug
# Solution().sortColors([2, 0, 1])
# Solution().sortColors([2, 0, 2, 1, 1, 0])
