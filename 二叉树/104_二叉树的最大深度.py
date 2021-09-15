# coding:utf-8

'''
date: 2021/09/13
content:
题目地址:https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法一
        思路：递归，但需要构建能全局保存的变量，否则在栈中最大值不能保存。从根节点往下计数
        '''
        def recurse(root, depth):
            if root is None:
                return depth

            left_depth = recurse(root.left, depth + 1)
            right_depth = recurse(root.right, depth + 1)

            return max(left_depth, right_depth)

        max_depth = recurse(root, 0)
        return max_depth


    def maxDepth_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法二
        思路：另一种递归的写法, 从叶子节点往上计数
        '''
        def recurse_2(root):
            if root is None:
                return 0

            left_depth = recurse_2(root.left)
            right_depth = recurse_2(root.right)
            depth = 1 + max(left_depth, right_depth)
            return depth
        max_depth = recurse_2(root)
        return max_depth


    def maxDepth_3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法三
        思路：层序遍历
        '''
        if root is None:
            return 0

        max_depth = 0
        q = deque([root])
        while q:
            q_size = len(q)
            for i in range(q_size):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            max_depth += 1
        return max_depth







