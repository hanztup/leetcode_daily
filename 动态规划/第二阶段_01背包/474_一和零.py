# coding:utf-8

'''
date: 2021/7/8
content:
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
示例 1:
输入:strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出:4
解释:最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2:
输入:strs = ["10", "0", "1"], m = 1, n = 1 输出:2
解释:最大的子集是 {"0", "1"} ，所以答案是 2 。
提示:
1 <= strs.length <= 600
1 <= strs[i].length <= 100 strs[i] 仅由 '0' 和 '1' 组成 1 <= m, n <= 100
'''

from pprint import pprint

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，三维dp的二维数组实现
        时间复杂度：
        空间复杂度：
        '''

        def count_zero(strs):
            nums_zero = []
            nums_one = []
            for str_num in strs:
                tmp_sum = sum([int(i) for i in list(str_num)])
                nums_zero.append(len(str_num) - tmp_sum)
                nums_one.append(tmp_sum)
            return nums_zero, nums_one

        # 计算每个词元素中0和1的个数
        count_zeros, count_ones = count_zero(strs)

        # 确定dp数组及初始化
        dp = [[0 for k in range(n+1)] for j in range(m+1)]

        '''下面这个没必要这样初始化，可以自行递推得到'''
        # for j in range(m, 0, -1):
        #     tmp_sum = 0
        #     for i in range(len(strs)):
        #         if count_ones[i] != 0:
        #             continue
        #         if tmp_sum + count_zeros[i] <= j:
        #             tmp_sum += count_zeros[i]
        #             dp[j][0] = tmp_sum
        #         else:
        #             dp[j][0] = tmp_sum
        #
        # for k in range(n, 0, -1):
        #     tmp_sum = 0
        #     for i in range(len(strs)):
        #         if count_zeros[i] != 0:
        #             continue
        #         if tmp_sum + count_ones[i] <= k:
        #             tmp_sum += count_ones[i]
        #             dp[0][k] = tmp_sum
        #         else:
        #             dp[0][k] = tmp_sum
        pprint(dp)

        # 确定递推
        for i in range(len(strs)):
            for j in range(m, count_zeros[i]-1, -1):
                for k in range(n, count_ones[i]-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-count_zeros[i]][k-count_ones[i]] + 1)
        pprint(dp)
        return dp[m][n]

if __name__ == '__main__':
    s = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 3
    n = 3
    ret = s.findMaxForm(strs, m, n)
    print(ret)

