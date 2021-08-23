# coding:utf-8

'''
date: 2021/08/23
content:
题目链接:https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

提示：
节点值的范围在32位有符号整数范围内。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        '''
        解法一
        思路：广度优先（层序遍历）
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''
        # res = []
        # if root is None:
        #     return res
        # q = deque([root])
        #
        # while q:
        #     q_size = len(q)
        #     tmp_sum = 0.0
        #     for i in range(q_size):
        #         node = q.popleft()
        #         tmp_sum += node.val
        #         if node.left is not None:
        #             q.append(node.left)
        #         if node.right is not None:
        #             q.append(node.right)
        #     res.append(tmp_sum / q_size)
        # return res


        '''
        解法二
        思路：深度优先
        时间复杂度：
        空间复杂度：
        '''

        def recurse(root):
            if root is None:
                return []

            left = recurse(root.left)
            right = recurse(root.right)

            # both sub_node is None
            if (not left) and (not right):
                return [[float(root.val)]]

            # one of sub_node is None
            if not left:
                return [[float(root.val)]] + right
            if not right:
                return [[float(root.val)]] + left

            # both sub_node is not None
            tmp = []
            for left_i, right_i in zip(left, right):
                tmp.append(left_i + right_i)
            # length not equal
            if len(left) > len(right):
                tmp += left[len(right):]
            elif len(right) > len(left):
                tmp += right[len(left):]

            return [[float(root.val)]] + tmp

        list_val = recurse(root)

        # calculate mean value
        res = []
        for l in list_val:
            res.append(sum(l) / len(l))
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)

    s = Solution()
    ret = s.averageOfLevels(root)
    print(ret)





