#
# @lc app=leetcode id=2729 lang=python3
#
# [2729] Check if The Number is Fascinating
#

# @lc code=start
class Solution:
    def isFascinating(self, n: int) -> bool:
        concat: str = str(n) + str(n * 2) + str(n * 3)
        if '0' in concat:
            return False
        for i in range(1, 10):
            if concat.count(str(i)) != 1:
                return False
        return True
# @lc code=end
