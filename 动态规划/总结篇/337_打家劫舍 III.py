# coding:utf-8

'''
date: 2021/7/29
content:
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释:小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释:小偷一晚能够盗取的最高金额= 4 + 5 = 9.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        解法一
        思路：递归(后序遍历)加动态规划
             每次遍历返回两个值（a，b），a表示不偷该节点能达到的最大值，b表示偷该节点能达到的最大值（相当于左子节点和右子节点的最大值和）
        时间复杂度：O(n)
        空间复杂度：O(logn)，递归回溯占用
        '''

        def recurse(root):
            if root is None:
                return 0, 0

            left_val = recurse(root.left)
            right_val = recurse(root.right)
            print(left_val)
            print(right_val)
            print('------')

            w_layer_val = root.val + left_val[1] + right_val[1]
            wo_layer_val = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])
            return w_layer_val, wo_layer_val

        ret_list = recurse(root)
        print(ret_list)
        return max(ret_list)


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(4, left=TreeNode(1), right=TreeNode(3))
    tree.right = TreeNode(5, right=TreeNode(1))
    ret = s.rob(tree)
    print(ret)
