#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        i = len(nums) - 1
        j = len(nums)
        while i >= 0:
            if nums[i] == val:
                nums[i] = nums[j - 1]
                nums[j - 1] = val
                j -= 1
            i -= 1
        return j
# @lc code=end
