#
# @lc app=leetcode id=2980 lang=python3
#
# [2980] Check if Bitwise OR Has Trailing Zeros
#

# @lc code=start
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        res: int = 0
        for i in nums:
            if i % 2 == 0:
                res += 1
            if res == 2:
                return True
        return False
# @lc code=end
