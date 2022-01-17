# coding:utf-8

'''
date: 2022/01/16
content:
Given two numbers represented by two linked lists, write a function that returns sum list.
The sum list is linked list representation of addition of two input numbers.

Example

Input:
  First  List: 5->6->3  // represents number 563
  Second List: 8->4->2  // represents number 842
Output:
  Resultant list: 1->4->0->5  // represents number 1405

Challenge
Not allowed to modify the lists.
Not allowed to use explicit extra space.
'''

class LinkList(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def compute_length(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    def reverse(self, head):
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

    def solution_1(self, l1, l2):
        '''
        思路：
        为了满足：
        1."Not allowed to modify the lists."  -- 不能直接对l1或l2反转
        2."Not allowed to use explicit extra space." -- 不能使用列表先保存每个节点的值
        因此，方法如下：
        1. 先统计出长度（差）
        2. 按位求和，创建节点与联系
        3. 反转链表 -- 将大于10的节点拆开，构建新的节点及关联 -- 再反转链表
        '''

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        '''统计长度（差）'''
        l1_len, l2_len = l1, l2
        l1_length = self.compute_length(l1_len)
        l2_length = self.compute_length(l2_len)

        '''按位求和，创建节点和连接'''
        dummy_node = LinkList(-1)
        head = dummy_node
        # 根据长度差，将指针移到相同位置
        if l1_length > l2_length:
            while l1_length - l2_length:
                tmp_node = LinkList(l1.val)
                head.next = tmp_node
                head = head.next
                l1 = l1.next
        elif l1_length < l2_length:
            while l2_length - l1_length:
                tmp_node = LinkList(l2.val)
                head.next = tmp_node
                head = head.next
                l2 = l2.next
        else:
            pass
        # 按位求和
        while (l1 is not None) and (l2 is not None):
            sum_val = l1.val + l2.val
            tmp_node = LinkList(sum_val)
            head.next = tmp_node
            head = head.next
            l1 = l1.next
            l2 = l2.next

        '''反转链表 -- 将大于10的节点拆开，构建新的节点及关联 -- 再反转链表'''
        # 反转链表
        reverse_head = self.reverse(dummy_node.next)
        reverse_dummy_node = LinkList(-2)
        reverse_dummy_node.next = reverse_head

        # 将大于10的节点拆开
        reverse_forward = 0  # 进位值
        while reverse_head is not None:
            cur_val = reverse_head.val + reverse_forward
            if cur_val >= 10:
                cur_val -= 10
                reverse_forward = 1
            else:
                reverse_forward = 0

            reverse_head.val = cur_val
        if reverse_forward == 1:
            tmp_node = LinkList(reverse_forward)
            reverse_head.next = tmp_node

        # 反转链表
        head = self.reverse(reverse_dummy_node.next)
        return head






