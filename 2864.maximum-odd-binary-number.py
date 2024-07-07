#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        res: str = ''
        count: int = 0
        for j in s:
            if j == '1':
                count = count + 1
        i: int = 0
        while i < count - 1:
            res = '1' + res
            i = i + 1
        i = 0
        while i < len(s) - count:
            res = res + '0'
            i = i + 1
        return res + '1'
# @lc code=end
