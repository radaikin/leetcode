#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
from typing import List
# @lc code=start


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        res = []
        ch_set = set(words[0])

        for ch in ch_set:
            count = 100
            for word in words:
                temp = word.count(ch)
                count = temp if temp < count else count
            while count != 0:
                res.append(ch)
                count -= 1
        return res

# @lc code=end


# debug
# Solution().commonChars(["bella","label","roller"])
# Solution().commonChars(["cool","lock","cook"])
