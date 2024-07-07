#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # def count_nodes(node: TreeNode):
        #     if node is None:
        #         return 0
        #     return count_nodes(node.left) + count_nodes(node.right) + 1
        # return count_nodes(root)

        def calc_height(node: TreeNode) -> int:
            if not node:
                return -1
            h = 0
            while node.left:
                node = node.left
                h += 1
            return h

        h = calc_height(root)
        nodes_count = 0
        while root:
            if calc_height(root.right) == h - 1:
                nodes_count += pow(2, h)
                root = root.right
            else:
                nodes_count += pow(2, h - 1)
                root = root.left
            h -= 1
        return nodes_count

# @lc code=end
