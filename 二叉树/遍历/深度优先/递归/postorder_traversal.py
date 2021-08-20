# coding:utf-8

'''
date: 2021/08/10
content: 二叉树后序遍历的递归写法
'''

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorder_traversal(self, root):
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return

        self.traverse(root.left, res)
        self.traverse(root.right, res)
        res.append(root.val)
