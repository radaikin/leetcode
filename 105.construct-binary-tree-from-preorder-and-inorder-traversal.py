#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        inoder_root_index = inorder.index(preorder[0])

        root.left = self.buildTree(
            preorder[1:1 + len(inorder[: inoder_root_index])],
            inorder[: inoder_root_index]
        )
        root.right = self.buildTree(
            preorder[1 + len(inorder[: inoder_root_index]):],
            inorder[inoder_root_index + 1:]
        )
        return root


# @lc code=end

# debug
# Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
# Solution().buildTree(preorder = [3,9,10,20,15,11,7], inorder = [10,9,3,11,15,20,7])
# Solution().buildTree(preorder = [1,2,4,6,5,3,7,8,9,10], inorder = [4,2,5,6,1,3,8,9,7,10])
# Solution().buildTree(preorder = [4,5,3,17,2,6,7,1,9,8,10,11,13,14,15,20,19], \
#                       inorder = [3,2,6,17,1,7,5,9,8,4,10,14,13,11,20,15,19])
