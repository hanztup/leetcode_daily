# coding:utf-8

'''
date: 2021/7/19
content:
给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；
换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 104
'''


import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，完全背包，一维dp
        时间复杂度：O(m * n)
        空间复杂度：O(n)
        '''

        # 先找到value <= n时的完全平方数数组
        nums = []
        for i in range(1, n):
            n_square = i ** 2
            if n_square > n:
                break
            else:
                nums.append(n_square)

        # 再使用dp
        MAX_INT = sys.maxsize
        dp = [MAX_INT] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(len(nums)):
            for j in range(nums[i], n+1):
                if dp[j-nums[i]] != MAX_INT:
                    dp[j] = min(dp[j], dp[j-nums[i]] + 1)

        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    ret = s.numSquares(3)
    print(ret)
