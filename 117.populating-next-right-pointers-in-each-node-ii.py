#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start

# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q: deque = deque([root])
        while q:
            lvl_size: int = len(q)
            for i in range(lvl_size):
                node: Node = q.popleft()
                if i < lvl_size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
# @lc code=end


# debug

# root = Node(1, left=Node(2, left=Node(4), right=Node(5)),
#             right=Node(3, left=Node(6), right=Node(7)))
# Solution().connect(root)
