# coding:utf-8

'''
date: 2022/01/05
content: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
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

        # 写法一
        while head is not None:
            tmp = head.next
            if tmp is None:
                break
            if tmp.val == head.val:
                # delete op
                head.next = tmp.next
                tmp.next = None
            else:
                head = tmp

        # 写法二: 更加简洁
        while head is not None:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next

        return dummy_node.next

