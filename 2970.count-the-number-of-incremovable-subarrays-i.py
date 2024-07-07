#
# @lc app=leetcode id=2970 lang=python3
#
# [2970] Count the Number of Incremovable Subarrays I
#

# @lc code=start
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res, n = 0, len(nums)

        def isStrictlyIncreasing(arr: list[int]) -> bool:
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True

        for i in range(n):
            for j in range(i, n):
                temp_arr = nums[: i] + nums[j+1:]
                if isStrictlyIncreasing(temp_arr):
                    res += 1
        return res
# @lc code=end
