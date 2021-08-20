# coding:utf=8

'''
date: 2021/08/19
content:
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        '''
        解法一
        思路：使用collections.deque作为队列，进行层序遍历
        时间复杂度：
        空间复杂度：
        '''

        res = []
        if root is None:
            return []
        q = deque([root])

        while len(q) != 0:
            queue_size = len(q)  # 提前确定size，否则后续pop时q的大小会变
            tmp = []
            for i in range(queue_size):
                node = q.popleft()
                tmp.append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            res.append(tmp)
        return res









