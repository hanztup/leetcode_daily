# coding:utf-8


'''
date: 2022/01/07
content: https://leetcode-cn.com/problems/partition-list/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None:
            return

        dummy_node = ListNode(-1)
        dummy_node.next = head
        left = dummy_node
        right = dummy_node

        while right is not None and right.next is not None:
            # (1) right.next.val >= x
            if right.next.val >= x:
                right = right.next
                continue
            # (2) right.next.val < x
            if left is not right:
                tmp = right.next
                right.next = right.next.next
                tmp.next = left.next
                left.next = tmp
                left = left.next
            else:
                left = left.next
                right = right.next

        return dummy_node.next




