# coding:utf-8


'''
date: 2021/6/9
content:
斐波那契数，通常用F(n) 表示，形成的序列称为 斐波那契数列 。
该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。


示例 1：
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3

提示：
0 <= n <= 30
'''


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，注意使用学到的五部曲来练习
        时间复杂度：O(N)
        空间复杂度：O(1)
        '''
        # dp = [0, 1]
        # if n <= 1:
        #     return dp[n]
        #
        # for i in range(2, n+1):
        #     cur_val = dp[-1] + dp[-2]
        #     dp[-1], dp[-2] = cur_val, dp[-1]
        # return dp[-1]


        '''
        解法二
        思路：递归
        时间复杂度：O(2^n)  -- 相当于构建一个二叉树，节点数为2*(n-1)
        空间复杂度：O(n)  --二叉树层高为n，对应的内存栈的使用
        '''
        def recurse(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            return recurse(n-1) + recurse(n-2)

        return recurse(n)


if __name__ == '__main__':
    s = Solution()
    ret = s.fib(8)
    print(ret)


