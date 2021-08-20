# coding:utf-8

'''
date: 2021/6/15
content:
给定一个正整数n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设n不小于 2 且不大于 58。
'''


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划
        （1）确定dp数组：dp[i] 表示n=i时最大的正整数和
        （2）递推公式：dp[i] = max(j * (n-j), dp[j] * (n-j), j * dp[n-j], dp[j] * dp[n-j]), 1 <= j < n
        （3）初始化：dp[0] = 0, dp[1] = 0, dp[2] = 1
        （4）遍历顺序：从2到n
        （5）举例：
        时间复杂度：
        空间复杂度：
        '''

        dp = [0] * (n + 1)
        dp[2] = 1

        for i in range(3, n+1):
            max_value = -1
            for j in range(1, i//2+1):
                tmp_max = max(j*(i - j), dp[j]*(i-j), j*dp[i-j], dp[j]*dp[i-j])
                max_value = tmp_max if tmp_max > max_value else max_value
            dp[i] = max_value

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    ret = s.integerBreak(8)
    print(ret)




