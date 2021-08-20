# coding:utf-8

'''
date: 2021/08/10
content: 二叉树中序遍历的迭代写法
'''

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def midorder_traversal(self, root):
        if root is None:
            return []

        res = []
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
            else:
                res.append(node.val)
                continue

            if node.right is not None:
                stack.append(node.right)
            stack.append(node)
            if node.left is not None:
                stack.append(node.left)
        return res