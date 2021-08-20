# coding:utf-8

'''
date: 2021/7/20
content:
给你两个非空 的链表，表示两个非负的整数。
它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        '''
        解法一
        思路：两个链表同时遍历
        时间复杂度：
        空间复杂度：
        '''

        '''第一次ac写法'''
        # point1, point2 = l1, l2
        # dummy_node = ListNode(-1)
        # head = dummy_node
        # offset = 0
        # while point1 is not None and point2 is not None:
        #     value1 = point1.val
        #     value2 = point2.val
        #     value_sum = value1 + value2 + offset
        #
        #     if value_sum >= 10:
        #         value_sum -= 10
        #         offset = 1
        #     else:
        #         offset = 0
        #
        #     tmp_node = ListNode(value_sum)
        #     head.next = tmp_node
        #     head = head.next
        #
        #     point1 = point1.next
        #     point2 = point2.next
        #
        # while point1 is not None:
        #     value1 = point1.val
        #     value_sum = value1 + offset
        #     if value_sum >= 10:
        #         value_sum -= 10
        #         offset = 1
        #     else:
        #         offset = 0
        #     tmp_node = ListNode(value_sum)
        #     head.next = tmp_node
        #     head = head.next
        #     point1 = point1.next
        #
        # while point2 is not None:
        #     value2 = point2.val
        #     value_sum = value2 + offset
        #     if value_sum >= 10:
        #         value_sum -= 10
        #         offset = 1
        #     else:
        #         offset = 0
        #     tmp_node = ListNode(value_sum)
        #     head.next = tmp_node
        #     head = head.next
        #     point2 = point2.next
        #
        # if offset:
        #     tmp_node = ListNode(offset)
        #     head.next = tmp_node
        #
        # return dummy_node.next


        '''改进后写法'''
        point1, point2 = l1, l2
        dummy_node = ListNode(-1)
        head = dummy_node
        offset = 0
        while (point1 is not None) or (point2 is not None):
            value1 = point1.val if point1 is not None else 0
            value2 = point2.val if point2 is not None else 0
            value_sum = value1 + value2 + offset

            if value_sum >= 10:
                value_sum -= 10
                offset = 1
            else:
                offset = 0

            tmp_node = ListNode(value_sum)
            head.next = tmp_node
            head = head.next

            if point1 is not None:
                point1 = point1.next
            if point2 is not None:
                point2 = point2.next

        if offset:  # 最后检测是否最前的进位
            tmp_node = ListNode(offset)
            head.next = tmp_node

        return dummy_node.next


if __name__ == '__main__':
    pass













