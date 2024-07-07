#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        r = l = 0
        n = len(s)
        ch: set = set()
        while r < n:
            if s[r] not in ch:
                ch.add(s[r])
                res = max(res, r - l + 1)
            else:
                while s[r] in ch:
                    ch.remove(s[l])
                    l += 1
                ch.add(s[r])
            r += 1
        return res


# @lc code=end

# debug
# Solution().lengthOfLongestSubstring("abcabcbb")
# Solution().lengthOfLongestSubstring("pwwkew")
# Solution().lengthOfLongestSubstring("bbbb")
