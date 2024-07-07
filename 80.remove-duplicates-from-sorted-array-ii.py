#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from typing import List
# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        j = 2
        while i < len(nums):
            if nums[j - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1
            elif nums[j - 2] != nums[i]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

# @lc code=end
