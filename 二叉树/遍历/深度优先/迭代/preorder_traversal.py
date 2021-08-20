# coding:utf-8

'''
date: 2021/08/10
content: 二叉树前序遍历的迭代写法
'''

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorder_traversal(self, root):
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return res
