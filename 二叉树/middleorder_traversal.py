# coding:utf-8

'''
date: 2021/3/23
content: 二叉树的中序遍历
'''

class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, root, result):

        if root is None:
            return

        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)


if __name__ == '__main__':
    # construct binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    ret = []

    s = Solution()
    s.traversal(root, ret)

    print(ret)
