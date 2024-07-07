#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        n_s, n_t = len(s), len(t)
        while j < n_s and i < n_t:
            if t[i] == s[j]:
                i += 1
            j += 1
        return n_t - i
# @lc code=end
