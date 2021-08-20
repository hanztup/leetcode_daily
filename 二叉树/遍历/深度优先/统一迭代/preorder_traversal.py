# coding:utf-8

'''
date: 2021/08/17
content: 使用统一迭代的方式实现前序遍历
'''

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorder_traversal(self, root):
        '''
        解法一
        思路：遍历过的节点，往stack中追加一个NULL节点。这个思路和我之前自己在"迭代"中所用的类似，我是通过记录每个节点是否被访问过，
        以空间换了时间。
        时间复杂度：
        空间复杂度：
        '''

        res = []
        stack = [root]

        while root is not None and stack:
            node = stack.pop()
            if node is not None:
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                res.append(node.val)
        return res