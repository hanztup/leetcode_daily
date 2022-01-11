# coding:utf-8

'''
date: 2022/01/05
content: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return

        dummy_node = ListNode(-1)
        dummy_node.next = head
        prev = dummy_node

        while head is not None:
            loop_flag = False
            while head.next and head.val == head.next.val:
                head.next = head.next.next
                loop_flag = True

            if not loop_flag:
                # means no duplicates
                head = head.next
                prev = prev.next
            else:
                # means duplicates
                head = head.next
                prev.next = head

        return dummy_node.next