# coding:utf-8

'''
date: 2021/6/10
content:

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划
        时间复杂度：O(N)
        空间复杂度：O(1)
        '''
        dp = [1, 2]
        if n == 1 or n == 2:
            return dp[n-1]

        for i in range(2, n):
            cur_val = dp[-1] + dp[-2]
            dp[-1], dp[-2] = cur_val, dp[-1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ret = s.climbStairs(1)
    print(ret)



