# coding:utf-8

'''
date: 2021/7/16
content:
题目链接:https://leetcode-cn.com/problems/coin-change/
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的
硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。 你可以认为每种硬币的数量是无限的。

示例 1:
输入:coins = [1, 2, 5], amount = 11 输出:3
解释:11 = 5 + 5 + 1

示例 2:
输入:coins = [2], amount = 3 输出:-1

示例 3:
输入:coins = [1], amount = 0 输出:0

示例 4:
输入:coins = [1], amount = 1 输出:1

示例 5:
输入:coins = [1], amount = 2 输出:2

提示:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
'''

import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX_INT = sys.maxsize
        dp = [MAX_INT] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                if dp[j-coins[i]] != MAX_INT:
                    dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        print(dp)
        if dp[amount] == MAX_INT:
            return -1
        else:
            return dp[amount]


if __name__ == '__main__':
    s = Solution()
    ret = s.coinChange([2], 3)
    print(ret)