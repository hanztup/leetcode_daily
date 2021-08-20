# coding: utf-8

'''
date: 2021/7/13
content:
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢? 注意:给定 n 是一个正整数。
示例 1:
输入: 2
输出: 2
解释: 有两种方法可以爬到楼顶。
1. 1阶+1阶 2. 2阶

示例 2:
输入: 3
输出: 3
解释: 有三种方法可以爬到楼顶。
1. 1阶+1阶+1阶 2. 1阶+2阶
3. 2阶+1阶

这道题的进阶版为：
一步一个台阶，两个台阶，三个台阶，.......，直到 m个台阶。
问有多少种不同的方法可以爬到楼顶呢?
'''


class Solution(object):
    def climbStairs(self, n, m):
        '''

        :param n: 到达楼顶需要n阶
        :param m: 每步可以走1到m个台阶
        '''

        '''
        解法一
        思路：动态规划，完全背包，一维dp
        时间复杂度：
        空间复杂度：
        '''
        dp = [0] * (n + 1)
        dp[0] = 1

        # 注意遍历顺序：在此求的是排列
        for j in range(1, n+1):
            for i in range(1, m+1):
                if j < i:
                    continue
                dp[j] += dp[j-i]

        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    ret = s.climbStairs(3, 2)
    print(ret)

    a = 'dsfs'
    c = []
    c.extend(map(list, a[1:]))
    print(c)
