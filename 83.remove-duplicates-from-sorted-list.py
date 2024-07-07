#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        while current:
            next_node: Optional[ListNode] = current.next
            while next_node and current.val == next_node.val:
                next_node = next_node.next
            current.next = next_node
            current = current.next
        return head

# @lc code=end

# debug
# Solution().deleteDuplicates(head=ListNode(1, ListNode(1, ListNode(2))))
# Solution().deleteDuplicates(head=ListNode(
#     1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
# Solution().deleteDuplicates(head=ListNode(
#     1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
