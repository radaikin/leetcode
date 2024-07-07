#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res: List = []
        candidates.sort()

        def backtrack(startIndex: int, currCombination: List[int], currTarget: int):
            if currTarget == 0:
                res.append(currCombination)
                return
            if currTarget < 0:
                return
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > currTarget:
                    break
                backtrack(
                    i + 1,
                    currCombination + [candidates[i]],
                    currTarget - candidates[i]
                )

        backtrack(0, [], target)
        return res
# @lc code=end

# debug
# Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
