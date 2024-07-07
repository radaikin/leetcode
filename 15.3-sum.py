#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List
# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        i = 0
        n = len(nums)
        nums.sort()
        while i < n - 2 and nums[i] <= 0:
            j = i + 1
            k = n - 1
            while j != k:
                check_sum = nums[i] + nums[j] + nums[k]
                if check_sum > 0:
                    k -= 1
                elif check_sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j != k and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < n - 2 and nums[i] <= 0 and nums[i] == nums[i - 1]:
                i += 1
        return res
# @lc code=end
