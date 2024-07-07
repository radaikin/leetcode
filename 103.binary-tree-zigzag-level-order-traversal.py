#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # res: List[List[int]] = []
        res: dict = {}

        def pushToRes(lvl: int, rt: Optional[TreeNode]):
            if not rt:
                return
            if lvl in res:
                if lvl % 2 == 0:
                    res[lvl].append(rt.val)
                else:
                    tmp: List[int] = [rt.val]
                    tmp.extend(res[lvl])
                    res[lvl] = tmp
            else:
                res[lvl] = [rt.val]
            lvl += 1
            pushToRes(lvl, rt.left)
            pushToRes(lvl, rt.right)
        pushToRes(0, root)
        return list(res.values())
        # @lc code=end

# debug
# root = TreeNode(3, left=TreeNode(9), right=TreeNode(
#     20, left=TreeNode(15), right=TreeNode(7)))
# Solution().zigzagLevelOrder(root)
