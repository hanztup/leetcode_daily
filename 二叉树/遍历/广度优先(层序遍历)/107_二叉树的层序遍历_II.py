# coding:utf-8

'''
date: 2021/08/19
content:
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        if root is None:
            return res
        q = deque([root])

        while q:
            q_size = len(q)
            tmp = []
            for i in range(q_size):
                node = q.popleft()
                tmp.append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            res.append(tmp)
        return list(reversed(res))


