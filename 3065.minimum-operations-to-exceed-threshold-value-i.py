#
# @lc app=leetcode id=3065 lang=python3
#
# [3065] Minimum Operations to Exceed Threshold Value I
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        i, res = 0, 0
        for i, num in enumerate(nums):
            if num < k:
                res += 1
            i += 1
        return res
# @lc code=end
