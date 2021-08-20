# coding:utf-8

'''
date: 2021/6/16
content:
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：
输入：n = 3
输出：5

示例 2：
输入：n = 1
输出：1

提示：
1 <= n <= 19
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，递推公式初次做时找不到：
        时间复杂度：O(n^2)
        空间复杂度：O(n)
        '''

        # dp = [1] * (n+1)
        #
        # for i in range(1, n+1):
        #     tmp_sum = 0
        #     for j in range(1, i+1):
        #         tmp_sum += dp[j-1] * dp[i-j]
        #     dp[i] = tmp_sum
        #
        # return dp[n]


        dp = [1]
        dp.extend([0]*n)

        for i in range(n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    ret = s.numTrees(5)
    print(ret)
