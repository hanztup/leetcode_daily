# coding:utf-8

'''
date: 2022/01/12
content: https://leetcode-cn.com/problems/add-two-numbers/
'''


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def compute_remain(self, sum_val):
        '''
        计算进位值和当前位值
        '''
        if sum_val >= 10:
            remain = sum_val - 10
            forward = 1
        else:
            remain = sum_val
            forward = 0

        return remain, forward

    def create_new_node(self, ret, remain):
        '''
        建立新的节点及连接
        '''
        tmp_node = ListNode(remain)
        ret.next = tmp_node
        ret = ret.next
        return ret

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy_node = ListNode(-1)
        ret = dummy_node
        forward = 0  # 进位的值
        while l1 is not None and l2 is not None:
            sum_val = l1.val + l2.val + forward
            # 计算进位值和当前位值
            remain, forward = self.compute_remain(sum_val)

            # 建立节点及连接
            ret = self.create_new_node(ret, remain)

            # 移动指针
            l1 = l1.next
            l2 = l2.next

        # 补充判断l1或l2
        while l1 is not None:
            sum_val = l1.val + forward
            remain, forward = self.compute_remain(sum_val)
            ret = self.create_new_node(ret, remain)
            l1 = l1.next

        while l2 is not None:
            sum_val = l2.val + forward
            remain, forward = self.compute_remain(sum_val)
            ret = self.create_new_node(ret, remain)
            l2 = l2.next

        if forward != 0:
            ret = self.create_new_node(ret, forward)
        return dummy_node.next

    def addTwoNumbers_faster(self, l1, l2):
        '''
        写法二：这道题的更简洁地写法
        '''

        dummy_node = ListNode(-1)
        head = dummy_node
        offset = 0

        while (l1 is not None) or (l2 is not None):
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum_val = val1 + val2 + offset

            if sum_val >= 10:
                sum_val -= 10
                offset = 1
            else:
                offset = 0

            tmp_node = ListNode(sum_val)
            head.next = tmp_node
            head = head.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if offset != 0:
            tmp_node = ListNode(offset)
            head.next = tmp_node

        return dummy_node.next

