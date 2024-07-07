#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#
from typing import List
# @lc code=start


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res_zero: List[str] = []
        res_one: List[str] = []
        zero_seq: int = 0
        one_seq: int = 1
        for i, group_num in enumerate(groups):
            if group_num == zero_seq:
                res_zero.append(words[i])
                zero_seq = 0 if zero_seq == 1 else 1
            if group_num == one_seq:
                res_one.append(words[i])
                one_seq = 0 if one_seq == 1 else 1

        return res_zero if len(res_zero) >= len(res_one) else res_one

# @lc code=end
