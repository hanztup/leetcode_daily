# coding:utf-8

'''
date：2021/09/15
content:
题目地址:https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

 

示例 1：



输入：root = [1,null,3,2,4,null,5,6]
输出：3
示例 2：



输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：5
 

提示：

树的深度不会超过 1000 。
树的节点数目位于 [0, 104] 之间。
'''

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        '''
        解法一
        思路：递归，需要从"左子树和右子树"转换为"孩子子树"
        '''
        def recurse(root):
            if root is None:
                return 0

            depth = 0
            for child in root.children:
                child_depth = recurse(child)
                depth = child_depth if child_depth > depth else depth
            depth += 1

            return depth

        max_depth = recurse(root)
        return max_depth


    def maxDepth_2(self, root):
        """
        :type root: Node
        :rtype: int
        """

        '''
        解法二
        思路：层次遍历
        '''
        if root is None:
            return 0

        max_depth = 0
        q = deque([root])

        while q:
            q_size = len(q)
            max_depth += 1
            for i in range(q_size):
                node = q.popleft()
                if node.children is not None:
                    q.extend(node.children)  # 积累: deque扩展一个list的方法是extend
        return max_depth