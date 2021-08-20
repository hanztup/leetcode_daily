# coding:utf-8

'''
date: 2021/3.23
content: 二叉树的前序遍历
'''

class TreeNode(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def traversal(self, tree_node, result):
        if tree_node is None:
            return

        result.append(tree_node.val)
        self.traversal(tree_node.left, result)
        self.traversal(tree_node.right, result)


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


