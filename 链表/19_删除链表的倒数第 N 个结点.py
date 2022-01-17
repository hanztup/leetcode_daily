# coding:utf-8

'''
date: 2022/01/17
content:
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        '''
        思路：快慢指针。快指针先走n个节点，当快指针走到最后一个节点时，慢指针恰好走到要删除节点的上一个节点
        '''

        if head is None:
            return

        slow, fast = head, head
        # fast指针先走n步
        while n > 0:
            fast = fast.next
            n -= 1

        if fast is None:
            head = head.next
            return head

        # fast和slow同时走，当fast为最后一个节点时退出
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # 此时删除slow的下一个节点
        slow.next = slow.next.next
        return head

