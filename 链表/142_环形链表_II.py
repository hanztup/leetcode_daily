# coding:utf-8

'''
date: 2021/6/4
content:
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。

进阶：
你是否可以使用 O(1) 空间解决此题？

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

提示：
链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        解法一
        思路：遍历 + 哈希表
        时间复杂度：
        空间复杂度：O(N)
        '''

        # visit = {}
        # count = 0
        # while head is not None:
        #     if head not in visit:
        #         visit[head] = count
        #         count += 1
        #         head = head.next
        #     else:
        #         return head
        #
        # return

        '''
        解法二
        思路：先用快慢步指针找到重合点，然后分别从头和从重合点出发，再次汇合时即为入口节点。（学会推导过程）
        时间复杂度：
        空间复杂度：
        '''
        f, s = head, head

        # 走到重合点
        while s is not None and f is not None:
            s = s.next
            f = f.next
            if f is not None:
                f = f.next

            if s == f:
                break

        # 重头走
        while head is not None and s is not None:
            if head != s:
                head = head.next
                s = s.next
            else:
                return head

        return




