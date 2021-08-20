# coding:utf-8

'''
date: 2021/5/13
content:
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """


        '''
        解法一
        思路：递归
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''
        def recur(cur, visit):
            if cur is None:
                return

            recur(cur.next, visit)
            visit.append(cur.val)

        ret_list = []
        recur(head, ret_list)
        return ret_list

