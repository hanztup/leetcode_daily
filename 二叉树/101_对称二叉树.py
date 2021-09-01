# coding:utf-8

'''
date: 2021/08/27
content:
题目地址:https://leetcode-cn.com/problems/symmetric-tree/

给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        '''
        解法一
        思路：递归法，切记是递归，不能只用遍历后的数组去对比
        '''

        def compare(left, right):
            if left is None and right is None:
                return True
            elif left is not None and right is None:
                return False
            elif left is None and right is not None:
                return False
            elif left.val != right.val:
                return False

            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            return outside & inside

        if root is None:
            return True
        res = compare(root.left, root.right)
        return res


    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        '''
        解法二
        思路：迭代法(堆)
        '''
        # if root is None:
        #     return True
        #
        # q = deque([root.left])
        # q.append(root.right)
        #
        # while q:
        #     left = q.popleft()
        #     right = q.popleft()
        #
        #     if left is None and right is None:
        #         continue
        #
        #     if (left is None) or (right is None) or (left.val != right.val):
        #         return False
        #
        #     q.append(left.left)
        #     q.append(right.right)
        #     q.append(left.right)
        #     q.append(right.left)
        # return True

        '''
        解法二
        思路：迭代法(栈)，思路及写法与堆一致
        '''






if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2, left=TreeNode(2))
    root.right = TreeNode(2, left=TreeNode(2))
    # root.right = TreeNode(2, right=TreeNode(2))

    s = Solution()
    ret = s.isSymmetric1(root)
    print(ret)
