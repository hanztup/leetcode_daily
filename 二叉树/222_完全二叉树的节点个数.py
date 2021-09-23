# coding:utf-8

'''
date: 2021/09/23
content:
题目地址:https://leetcode-cn.com/problems/count-complete-tree-nodes/
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：
在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~2^h个节点。

示例 1：


输入：root = [1,2,3,4,5,6]
输出：6
示例 2：

输入：root = []
输出：0
示例 3：

输入：root = [1]
输出：1
 

提示：

树中节点的数目范围是[0, 5 * 104]
0 <= Node.val <= 5 * 104
题目数据保证输入的树是 完全二叉树
 

进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法一
        思路：层序遍历，保存每层的节点数和遍历的层数
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''

        if root is None:
            return 0

        depth = 0
        last_layer_node_num = 0
        q = deque([root])

        while q:
            q_size = len(q)
            depth += 1
            last_layer_node_num = q_size
            for i in range(q_size):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return 2 ** (depth - 1) - 1 + last_layer_node_num


    def countNodes_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法二
        思路：递归， 返回左右子树的节点个数
        时间复杂度：O(n)
        空间复杂度：O(logn)
        '''

        def recurse(root):
            if root is None:
                return 0

            left_num = recurse(root.left)
            right_num = recurse(root.right)

            return left_num + right_num + 1

        return recurse(root)

    def countNodes_3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法三
        思路：进阶做法，降低时间复杂度。根据完全二叉树的特性：只有中间层的满二叉树节点和最后一层节点。
        时间复杂度：O(logn * logn)
        空间复杂度：O(logn)
        '''

        if root is None:
            return 0

        left = root.left
        left_depth = 0
        right = root.right
        right_depth = 0

        while left:
            left = left.left
            left_depth += 1

        while right:
            right = right.right
            right_depth += 1

        if left_depth == right_depth:  # 满二叉树则返回
            return 2 ** (left_depth + 1) - 1

        return self.countNodes_3(root.left) + self.countNodes_3(root.right) + 1  # 不是满二叉树，就往下一层找，直到为满二叉树为止







