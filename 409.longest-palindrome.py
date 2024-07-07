#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] not in s[:i]:
                temp = 0
                for j in range(i, len(s)):
                    if s[i] == s[j]:
                        temp += 1
                res += temp - (temp % 2)
        return res if res == len(s) else res + 1
# @lc code=end


# debug
# Solution().longestPalindrome("abcecccdd")
# Solution().longestPalindrome("abccccdd")
# Solution().longestPalindrome("a")
# Solution().longestPalindrome("abcccd")
