# coding:utf-8

'''
date: 2021/08/24
content:
题目地址:https://leetcode-cn.com/problems/invert-binary-tree/

翻转一棵二叉树。
示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        '''
        解法一
        思路：递归，深度优先
        '''
        # def recurse(root):
        #     if root is None:
        #         return
        #
        #     left = recurse(root.left)
        #     right = recurse(root.right)
        #
        #     if left is None and right is None:
        #         return root
        #
        #     root.left, root.right = right, left
        #     return root
        # return recurse(root)

        '''
        解法二
        思路：层序遍历，广度优先
        '''
        if root is None:
            return root
        q = deque([root])
        while q:
            q_size = len(q)
            for i in range(q_size):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                node.left, node.right = node.right, node.left

        return root

