#
# @lc app=leetcode id=2717 lang=python3
#
# [2717] Semi-Ordered Permutation
#

# @lc code=start
from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        index_one: int = nums.index(1)
        nums_len = len(nums)
        index_last: int = nums.index(nums_len)
        swaps: int = (index_one) + (-1 if index_last <
                                    index_one else 0) + ((nums_len - 1) - index_last)
        return swaps
# @lc code=end
