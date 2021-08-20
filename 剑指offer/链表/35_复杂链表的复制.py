# coding:utf-8


'''
date: 2020/5/14
content:
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

'''


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """


        '''
        解法一
        思路：
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''
        if head is None:
            return

        # copy next
        copy_head = head
        while copy_head is not None:
            new = Node(copy_head.val)
            tmp = copy_head.next
            copy_head.next = new
            new.next = tmp
            copy_head = tmp

        # copy random
        copy_head = head
        copy_new = head.next
        while copy_new is not None and copy_head is not None:
            if copy_head.random is None:
                copy_new.random = copy_head.random
            else:
                copy_new.random = copy_head.random.next

            if copy_new.next is None:
                break
            copy_head = copy_new.next
            copy_new = copy_new.next.next

        # delete origin connection
        copy_head = head
        copy_new = head.next
        while copy_head is not None:
            step1 = copy_head.next
            if copy_head.next.next is None:
                copy_head.next = None
                break
            step2 = copy_head.next.next
            copy_head.next = step2
            copy_head = step1

        return copy_new


