# coding:utf-8

'''
date: 2021/5/21
content:

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

示例 1：
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

示例 2：
输入：n = 2
输出：false

提示：
1 <= n <= 231 - 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''
        解法一
        思路：两个方向解决：（1）怎么判断每一位数字？ -> 转换成字符，按字平方
                         （2）怎么退出无限循环? -> 存储每次得到的数，当重复出现或等于1时退出
        时间复杂度：O(logn) (要明白怎么推导)
        空间复杂度：
        '''

        def count_sum(n):
            char_n_list = list(str(n))
            ret = 0
            for str_num in char_n_list:
                ret += int(str_num) ** 2
            return ret

        def count_sum_new(n):
            ret = 0
            while n > 0:
                n, digit = divmod(n, 10)
                ret + digit ** 2
            return ret



        visit = {}

        while True:
            round_sum = count_sum(n)
            print(round_sum)
            if round_sum in visit:
                return False
            if round_sum == 1:
                return True
            n = round_sum
            visit[round_sum] = True


if __name__ == '__main__':
    s = Solution()
    res = s.isHappy(4)
    print(res)