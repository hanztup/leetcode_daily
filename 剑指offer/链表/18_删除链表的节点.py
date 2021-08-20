# coding:utf-8

'''
date: 2021/5/13
content:
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

说明：
题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        '''
        需注意审题：这道题保证链表中节点的值互不相同
        '''

        '''
        解法一
        思路：dummy node
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        dummy_node = ListNode(-1)
        dummy_node.next = head
        new = dummy_node

        while head is not None:
            if head.val == val:
                tmp = head.next
                head.next = None
                new.next = tmp
                break
            head = head.next
            new = new.next

        return dummy_node.next