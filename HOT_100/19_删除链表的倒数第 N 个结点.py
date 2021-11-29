# coding:utf-8

'''
date: 2021/11/29
content:
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

进阶：你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        '''
        解法一
        思路：双指针，使用一趟遍历完成删除。
        时间复杂度：O(N)
        空间复杂度：O(1)
        '''

        dummy_node = ListNode(-1, next=head)
        front = head
        rear = dummy_node

        # front指针先走n步
        # while front.next is not None and n > 1:
        #     front = front.next
        #     n -= 1
        # update:
        for i in range(n):
            front = front.next

        # front和rear同时走，直到front到达末尾，此时rear指向待删除节点的前一节点
        # while front.next is not None:
        #     front = front.next
        #     rear = rear.next
        # update:
        while front:
            front = front.next
            rear = rear.next

        # 删除rear的后一节点
        rear.next = rear.next.next
        return dummy_node.next

