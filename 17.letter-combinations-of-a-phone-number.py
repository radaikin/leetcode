#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping: dict[str, str] = {"2": "abc",
                                   "3": "def",
                                   "4": "ghi",
                                   "5": "jkl",
                                   "6": "mno",
                                   "7": "pqrs",
                                   "8": "tuv",
                                   "9": "wxyz"}

        result: List[str] = []

        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                result.append(currStr)
                return
            for ch in mapping[digits[i]]:
                backtrack(i+1, currStr + ch)
        if digits:
            backtrack(0, "")

        return result

# @lc code=end
