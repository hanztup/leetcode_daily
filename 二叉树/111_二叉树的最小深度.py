# coding:utf-8

'''
date: 2021/09/16
content:
题目地址:https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
 

提示：

树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法一
        思路: 递归，后序遍历。这道题需要注意和最大深度的区别是：只有当左右子节点都为空时，才算是有效的叶子节点
        '''

        def recurse(root):
            if root is None:
                return 0

            left_depth = recurse(root.left)
            right_depth = recurse(root.right)

            depth = min(left_depth, right_depth) if left_depth and right_depth else left_depth + right_depth
            depth += 1
            return depth

        min_depth = recurse(root)
        return min_depth

    def minDepth_2(self, root):
        """
                :type root: TreeNode
                :rtype: int
                """

        '''
        解法二
        思路: 层序遍历，这道题更适合用这个方式去做，因为只有当遍历到一个node，其左右子节点均为空时便可以提前返回，同时也
        避免了判断"子节点非叶子节点的错误路径数计算"
        '''

        from collections import deque

        if root is None:
            return 0
        min_depth = 0
        q = deque([root])

        while q:
            q_size = len(q)
            min_depth += 1
            for i in range(q_size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return min_depth
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return min_depth