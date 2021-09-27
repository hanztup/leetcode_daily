# coding:utf-8

'''
date: 2021/09/27
content:
题目地址:https://leetcode-cn.com/problems/balanced-binary-tree/

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true
 

提示：

树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        '''
        解法一
        思路：递归，比较左右子树返回的深度差
        时间复杂度：O(n)
        空间复杂度：O(logn)
        '''

        def recurse(root):
            if root is None:
                return 0

            left_depth = recurse(root.left)
            right_depth = recurse(root.right)

            if left_depth is False or right_depth is False:
                return False

            if abs(left_depth - right_depth) <= 1:
                return max(left_depth, right_depth) + 1
            else:
                return False

        res = recurse(root)
        res = True if res is not False else res
        return res