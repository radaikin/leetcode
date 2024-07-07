#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
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

        dummy: ListNode = ListNode(-1, head)

        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = dummy

        while curr:
            next_node: Optional[ListNode] = curr.next
            while next_node and curr.val == next_node.val:
                next_node = next_node.next
            if curr.next != next_node:
                prev.next = next_node
            else:
                prev = curr
            curr = next_node
        return dummy.next


# @lc code=end

# debug
# Solution().deleteDuplicates(head=ListNode(
    # 1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))))
# Solution().deleteDuplicates(head=ListNode(
    # 1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
