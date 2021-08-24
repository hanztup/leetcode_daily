# coding:utf-8

'''
date: 2021/08/24
content:
题目链接:https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/

给定一棵二叉树的根节点root ，请找出该二叉树中每一层的最大值。

示例1：
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:
          1
         / \
        3   2
       / \   \
      5   3   9

示例2：
输入: root = [1,2,3]
输出: [1,3]
解释:
          1
         / \
        2   3

示例3：
输入: root = [1]
输出: [1]

示例4：
输入: root = [1,null,2]
输出: [1,2]
解释:
          1
           \
            2

示例5：
输入: root = []
输出: []


提示：
二叉树的节点个数的范围是 [0,104]
-231<= Node.val <= 231- 1
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root is None:
            return res
        q = deque([root])

        while q:
            q_size = len(q)
            max_val = -float('inf')
            for i in range(q_size):
                node = q.popleft()
                max_val = node.val if node.val > max_val else max_val

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(max_val)
        return res

