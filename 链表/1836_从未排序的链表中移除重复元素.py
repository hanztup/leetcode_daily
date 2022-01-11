# coding:utf-8

'''
date: 2022/01/07
content: https://leetcode-cn.com/problems/remove-duplicates-from-an-unsorted-linked-list/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        解法一
        思路：两遍循环，第一遍记录重复的值，第二遍进行实质性删除
        '''
        if head is None:
            return

        dummy_node = ListNode(-1)
        dummy_node.next = head

        # 第一遍遍历
        visited = {}
        firsth = dummy_node.next
        while firsth is not None:
            if firsth.val not in visited:
                visited[firsth.val] = 1
            else:
                visited[firsth.val] += 1

            firsth = firsth.next

        # 第二遍遍历，进行删除
        secondh = dummy_node
        while secondh.next is not None:
            if visited[secondh.next.val] <= 1:
                secondh = secondh.next
            else:
                tmp = secondh.next.next
                secondh.next = tmp
        return dummy_node.next

