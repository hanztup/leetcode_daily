# coding:utf-8

'''
date: 2021/5/12
content:
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：
0 <= 节点个数 <= 5000

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        解法一
        思路：利用双指针，原地修改
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        # if head is None:
        #     return None
        #
        # new = head
        # while head is not None:
        #     if head == new:
        #         head = head.next
        #         new.next = None
        #         continue
        #
        #     tmp = head.next
        #     head.next = new
        #     new = head
        #     head = tmp
        # return new


        '''
        解法一优化
        '''
        # cur, pre = head, None
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre

        '''
        解法二
        思路：递归
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''

        def recur(cur, prev):
            if cur is None:
                return prev
            res = recur(cur.next, cur)
            cur.next = prev
            return res

        return recur(head, None)



