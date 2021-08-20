# coding:utf-8

'''
date: 2021/5/14
content:
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """


        '''
        解法一
        思路：找到长的链表，先走长度差的，等两个链表等长时，再判断
        时间复杂度：O(a+b) 
        空间复杂度：O(1)
        '''

        # if headA is None or headB is None:
        #     return
        #
        # # 统计两个链表的长度
        # len_a, visit_a = 0, headA
        # len_b, visit_b = 0, headB
        #
        # while visit_a is not None:
        #     len_a += 1
        #     visit_a = visit_a.next
        #
        # while visit_b is not None:
        #     len_b += 1
        #     visit_b = visit_b.next
        #
        # # 长的链表先走"长度差"个step
        # steps = len_a - len_b
        #
        # if steps > 0:
        #     while steps > 0:
        #         headA = headA.next
        #         steps -= 1
        #     return self.travel(headA, headB)
        # elif steps < 0:
        #     while steps < 0:
        #         headB = headB.next
        #         steps += 1
        #     return self.travel(headA, headB)
        # else:
        #     return self.travel(headA, headB)

        '''
        解法二
        思路：双指针法，需要总结
        时间复杂度：O(a+b)
        空间复杂度：O(1)
        '''
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A



    def travel(self, headA, headB):
        while headA is not None:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return
