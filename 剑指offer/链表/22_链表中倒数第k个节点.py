# coding:utf-8

'''
date: 2021/5/12
content:
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        '''
        解法1
        思路：倒数第k个，转换为正数第n-k+1个
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        # if head is None:
        #     return None
        #
        # visit_length = 0
        # store_head = head
        #
        # # 先统计链表长度
        # while head is not None:
        #     head = head.next
        #     visit_length += 1
        #
        # # 再找到正数第n-k+1个节点
        # steps = visit_length - k
        # if steps < 0:
        #     return None
        # while store_head is not None:
        #     steps -= 1
        #     if steps < 0:
        #         break
        #     store_head = store_head.next
        #
        # return store_head


        '''
        解法二
        思路：双指针，可以避免使用循环求链表长度
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former is not None:
            former, latter = former.next, latter.next
        return latter


























