#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List
# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# @lc code=end
