#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        d: dict = {}
        for i in hand:
            d[i] = d.get(i, 0) + 1
        i = hand[0]

        s_k = sorted(d.keys())
        for key in s_k:
            if d[key] > 0:
                step_count = d[key]
                for i in range(key, key + groupSize):
                    if i in d:
                        if d[i] < step_count:
                            return False
                        d[i] -= step_count
                    else:
                        return False
        return True

# @lc code=end


# debug
# Solution().isNStraightHand( hand = [1,1,2,2,3,3], groupSize = 2)
# Solution().isNStraightHand( hand = [1,2,3], groupSize = 1)
